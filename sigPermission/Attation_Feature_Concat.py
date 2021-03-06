import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras import layers,Sequential
import pandas as pd
import numpy as np
from library.AutoSetSeed import *
from indicator import indicator
from library.AutoSetSeed import *
import torch.nn as nn
#import math
#try:
#    from torch.hub import load_state_dict_from_url
#except ImportError:
#    from torch.utils.model_zoo import load_url as load_state_dict_from_url
import torch
import os
from sklearn.model_selection import train_test_split
size=14
data=pd.read_csv('service145权限和可疑API特征数据集合成顺序有标签删除特征和为1.csv', header=None)
train_label=data.values[:,0]
train_data=data.values[:,1:197]
train_data=train_data.astype(np.float32)
print(train_data.shape)
train_data=train_data.reshape(-1,size,size)
x_train,x_test,y_train,y_test=train_test_split(train_data,train_label,random_state=8)
print("145权限和可疑API特征合成的数据集有标签删除特征和为1Size",x_train.shape,y_train.shape,x_test.shape)

size2=14
data2=pd.read_csv('service145权限和Hardware特征数据集合成顺序有标签删除特征和为1.csv', header=None)
train_label2=data2.values[:,0]
train_data2=data2.values[:,1:197]
train_data2=train_data2.astype(np.float32)
print(train_data2.shape)
train_data2=train_data2.reshape(-1,size2,size2)
x_train2,x_test2,y_train2,y_test2=train_test_split(train_data2,train_label2,random_state=8)
print("145权限和Hardware特征合成的数据集有标签删除特征和为1Size",x_train2.shape,y_train2.shape,x_test2.shape)

# size3=365
# filename = 'D:/fh/机器学习/服务器上代码/Intent和四大组件的数据集标签.csv'
# data3 = pd.read_csv(filename, sep=',', engine='python', iterator=True, header=None)
# loop = True
# chunkSize = 1000
# chunks = []
# index = 0
# while loop:
#     try:
#         print(index)
#         chunk = data3.get_chunk(chunkSize)
#         chunks.append(chunk)
#         index += 1
#
#     except StopIteration:
#         loop = False
#         print("Iteration is stopped.")
# print('开始合并')
# data3 = pd.concat(chunks, ignore_index=True)
# array = data3.values
# print(np.shape(array))
# train_label3=data3.values[:,0]
# # train_data=data.values[:,1:133226]
# train_data3=data3.values[:,1:133226]
size3=187
data3=pd.read_csv('Intent和四大组件的数据集标签删除特征和为1.csv', header=None)
train_label3=data3.values[:,0]
train_data3=data3.values[:,1:34970]
train_data3=train_data3.astype(np.float32)
print(train_data3.shape)
train_data3=train_data3.reshape(-1,size3,size3)
x_train3,x_test3,y_train3,y_test3=train_test_split(train_data3,train_label3,random_state=8)
print("Intent和四大组件的数据集标签删除特征和为1Size",x_train3.shape,y_train3.shape,x_test3.shape)
# x_train2=tf.convert_to_tensor(x_train2)
# x_test2=tf.convert_to_tensor(x_test2)
# y_train2=tf.convert_to_tensor(y_train2)
# y_test2=tf.convert_to_tensor(y_test2)

#通道注意力机制
class ChannelAttention(nn.Module):
    def __init__(self, in_planes, ratio=16):
        super(ChannelAttention, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)
 
        self.fc1= nn.Conv2d(in_planes, in_planes // 16, 1, bias=False)
        self.relu1 = nn.ReLU()
        self.fc2= nn.Conv2d(in_planes // 16, in_planes, 1, bias=False)
 
        self.sigmoid = nn.Sigmoid()
 
    def forward(self, x):
        avg_out = self.fc2(self.relu1(self.fc1(self.avg_pool(x))))
        max_out = self.fc2(self.relu1(self.fc1(self.max_pool(x))))
        out = avg_out + max_out
        return self.sigmoid(out)

#空间注意力机制

class SpatialAttention(nn.Module):
    def __init__(self, kernel_size=7):
        super(SpatialAttention, self).__init__()
 
        assert kernel_size in (3, 7), 'kernel size must be 3 or 7'
        padding = 3 if kernel_size == 7 else 1
 
        self.conv1 = nn.Conv2d(2, 1, kernel_size, padding=padding, bias=False)
        self.sigmoid = nn.Sigmoid()
 
    def forward(self, x):
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        x = torch.cat([avg_out, max_out], dim=1)
        x = self.conv1(x)
        return self.sigmoid(x)


class SELayer(layers.Layer):
    def __init__(self, channel, reduction=16):
        super().__init__()
        self.fc = Sequential()
        self.fc.add(layers.GlobalAveragePooling1D())
        self.fc.add(layers.Dense(channel // reduction, activation='relu'))
        self.fc.add(layers.Dense(channel))
        self.fc.add(layers.Activation('sigmoid'))

    def call(self, inputs):
        y = self.fc(inputs)
        output = layers.Multiply()([inputs, y])
        return output

class SEBlock(layers.Layer):
    def __init__(self, filter_num, channel, stride=1, reduction=16):
        super().__init__()
        self.conv1 = layers.Conv1D(filter_num, 3, strides=stride, padding='same')
        self.bn1 = layers.BatchNormalization()
        self.relu = layers.Activation('relu')

        self.conv2 = layers.Conv1D(filter_num, 3, strides=1, padding='same')
        self.bn2 = layers.BatchNormalization()

        self.add = layers.Add()
        self.se = SELayer(channel, reduction)
        self.se2 = SELayer(channel, reduction)
        if stride != 1:
            self.downsample = Sequential()
            self.downsample.add(layers.Conv1D(filter_num, 1, strides=stride))
            self.downsample.add(layers.BatchNormalization())
        else:
            self.downsample = lambda x: x

    def call(self, inputs, training=True):
        out = self.conv1(inputs)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.se2(out)

        identity = self.downsample(inputs)
        identity = self.se(identity)

        output = self.add([out, identity])
        output = self.relu(output)
        return output

class ConvBNRelu(keras.Model):
    def __init__(self,ch,kernel_size=3,strides=1,padding='same'):
        super().__init__()
        self.model=keras.Sequential([
        layers.Conv1D(ch,kernel_size,strides=strides,padding='same'),
        # layers.Dropout(0.1),
        layers.BatchNormalization(),
        layers.Activation('relu')
        ])
    def call(self,x):
        return self.model(x)
class InceptionBlock(keras.Model):
    def __init__(self,ch,strides=1):
        super().__init__()
        self.ch=ch
        self.strides=strides
        self.c1=ConvBNRelu(ch,1,strides)
        # self.c1_2 = ConvBNRelu(ch, 1, strides)
        self.c2_1=ConvBNRelu(ch,1,strides)
        self.c2_2=ConvBNRelu(ch,3,1)
        # self.c2_3 = ConvBNRelu(ch, 1, strides)
        self.c3_1=ConvBNRelu(ch,1,strides)
        self.c3_2=ConvBNRelu(ch,5,1)
        # self.c3_3 = ConvBNRelu(ch, 1, strides)
        self.c4_1=ConvBNRelu(ch,1,strides)
        self.c4_2=ConvBNRelu(ch,7,1)
        # self.c4_3 = ConvBNRelu(ch, 1, strides)
        self.p5_1=keras.layers.MaxPool1D(3,strides=1,padding='same')
        self.c5_2=ConvBNRelu(ch,1,strides)
        # self.c5_3 = ConvBNRelu(ch, 1, strides)
        # self.p4_1=keras.layers.MaxPool1D(3,strides=1,padding='same')
        # self.c4_2=ConvBNRelu(ch,1,strides)
    def call(self,x):
        x1=self.c1(x)
        # x1_2=self.c1_2(x1)
        # print("x1", x1_2.shape)
        x2_1=self.c2_1(x)
        x2_2=self.c2_2(x2_1)
        # x2_3 = self.c2_3(x2_2)
        # print("x2_3",x2_3.shape)
        x3_1=self.c3_1(x)
        x3_2=self.c3_2(x3_1)
        # x3_3 = self.c3_3(x3_2)
        # print("x3_3", x3_3.shape)
        x4_1=self.c4_1(x)
        x4_2=self.c4_2(x4_1)
        # x4_3 = self.c4_3(x4_2)
        # print("x4_3", x4_3.shape)
        x5_1=self.p5_1(x)
        x5_2=self.c5_2(x5_1)
        # x5_3 = self.c5_3(x5_2)
        x=tf.concat([x1,x2_2,x3_2,x4_2,x5_2],axis=-1)
        # x = tf.concat([x1, x2_2, x3_2, x5_2], axis=-1)
        return x

class Inception10(keras.Model):
    def __init__(self,num_blocks,num_classes,init_ch=128,inplanes=64):
        super().__init__()
        self.in_channels=init_ch
        self.concate = layers.Concatenate(axis=-1)
        self.out_channels=init_ch
        self.num_blocks=num_blocks
        # self.Conv1=layers.Conv1D(filters=128,kernel_size=3,strides=1,padding='same')
        # self.norm=layers.BatchNormalization()
        # self.active=layers.Activation('relu')
        self.Fal=layers.Flatten()
        self.Fal_f1=keras.layers.Dense(196,activation='relu')
        # self.AdapAvgPool=torch.nn.AdaptiveAvgPool2d((14,14))
        self.c1=ConvBNRelu(init_ch)
        self.ca = ChannelAttention(self.inplanes)
        self.sa = SpatialAttention()
        self.totensor=torch.Tensor()
        self.blocks=tf.keras.Sequential()
        self.blocks2 = tf.keras.Sequential()
        self.blocks3 = tf.keras.Sequential()
        for block_id in range(num_blocks):
            for layer_id in range(2):
                if layer_id==0:
                    block=InceptionBlock(self.out_channels,strides=2)
                    block2=InceptionBlock(self.out_channels,strides=2)
                    block3=InceptionBlock(self.out_channels,strides=2)
                else:
                    block=InceptionBlock(self.out_channels,strides=1)
                    block2=InceptionBlock(self.out_channels,strides=1)
                    block3=InceptionBlock(self.out_channels,strides=1)
                self.blocks.add(block)
                self.blocks2.add(block2)
                self.blocks3.add(block3)
            self.out_channels*=2
        self.SEnet_block=tf.keras.Sequential()
        self.SEnet_block.add(SEBlock(filter_num=128,channel=128,stride=2))

        self.ca1 = ChannelAttention(self.inplanes)
        self.sa1 = SpatialAttention()

        self.p1=keras.layers.GlobalAveragePooling1D()
        self.f1=keras.layers.Dense(num_classes,activation='softmax')
    def call(self,x):
        x1 = self.c1(x[0])
        x2 = self.c1(x[1])
        # x2=self.AdapAvgPool(x[1].eval(session=self.sess))
        # x2=tf.convert_to_tensor(x2)
        x3 = self.Fal(x[2])
        print(x3.shape)
        x3 = self.Fal_f1(x3)
        x3 = tf.reshape(x3, [-1, 14, 14])
        x3 = self.c1(x3)

        x1 = self.totensor(x1)
        x2 = self.totensor(x2)
        x3 = self.totensor(x3)

        x1 = self.ca(x1) * x1
        x1 = self.sa(x1) * x1
        x2 = self.ca(x2) * x2
        x2 = self.sa(x2) * x2
        x3 = self.ca(x3) * x3
        x3 = self.sa(x3) * x3

        x1 = self.blocks(x1)
        x2 = self.blocks2(x2)
        x3 = self.blocks3(x3)
        print("x1.shape",x1.shape)
        print("x2.shape", x2.shape)
        print("x3.shape", x3.shape)
        x = self.concate([x1, x2])
        x = self.concate([x, x3])
        x=  self.SEnet_block.call(x)

        x = self.ca1(x) * x
        x = self.sa1(x) * x

        x = self.p1(x)
        y = self.f1(x)
        return y
def getGoogleNet(input_shape1,input_shape2,num_blocks=3,num_classes=2):
    model=Inception10(num_blocks,num_classes)
    #model.build(input_shape=(None,input_shape[0],input_shape[-1]))
    return model
# class EnsembelNet(keras.Model):
#     def __init__(self,Nets,channel,num_classes=2):
#         super().__init__()
#         self.Nets=Nets
#         self.concate=layers.Concatenate(axis=-1)
#         '''这个卷积盒的H 可以改'''
#         self.conv=layers.Conv1D(channel,1,strides=1,padding='same')
#         self.avg=layers.GlobalAveragePooling1D()
#         self.fc=layers.Dense(num_classes,activation='softmax')
#         self.bn=layers.BatchNormalization()
#         self.relu=layers.Activation('relu')
#     def call(self,inputs):
#         x=inputs
#         out=[]
#         for i in range(len(self.Nets)):
#             self.Nets[i].build(x.shape)
#             out.append(self.Nets[i](x))
#         output=self.concate(out)
#         output=self.conv(output)
#         output=self.bn(output)
#         output=self.relu(output)
#         output=self.avg(output)
#         output=self.fc(output)
#         return output
input_shape1=(14,14)
input_shape2=(14,14)
setup_seed("Tf",seed=1)
model = getGoogleNet(input_shape1,input_shape2)
adam=keras.optimizers.Adam(lr=0.001,beta_1=0.9,beta_2=0.99,epsilon=1e-08,decay=0.0)
# adam=keras.optimizers.Adam(lr=0.001)
model.compile(optimizer=adam, loss='sparse_categorical_crossentropy', metrics=['acc'])
model.build(input_shape=[(None, size, size),(None, size2, size2),(None, size3, size3)])

# model.fit([x_train,x_train2],y_train,validation_data = ([x_test,x_test2],y_test),
#           batch_size=128, epochs=50, verbose=2)

model.fit([x_train,x_train2,x_train3],y_train,batch_size=500, epochs=100, verbose=2)

# model2=getGoogleNet(input_shape2)
# adam=keras.optimizers.Adam(lr=0.001)
# model2.compile(optimizer=adam, loss='sparse_categorical_crossentropy', metrics=['acc'])
# model2.build(input_shape=(None, size2, size2))
# model2.fit(x_train2, y_train2, batch_size=64, epochs=20, verbose=2)

# EnsembelNet_model=EnsembelNet([model,model2],1)
# EnsembelNet_model.compile(optimizer=adam, loss='sparse_categorical_crossentropy', metrics=['acc'])
# EnsembelNet_model.build(input_shape=(None, size2, size2))
# EnsembelNet_model.fit(x_train2, y_train2, batch_size=64, epochs=50, verbose=2)

pred = model.predict([x_test,x_test2,x_test3])
pred = np.argmax(pred, axis=1)
score = indicator(pred,y_test)
Accuracy, Precision, Recall, F_meature = score.getMetrics()
Specific = score.getSpecific()
TPR, FPR = score.getfprtpr()
AUC, x, y = score.getAuc()
MCC = score.getMCC()
print("Accuracy:", Accuracy)
print("Precison:",Precision )
print("Recall:", Recall)
print("F-meature:",F_meature)
print("Specific:", Specific)
print("MCC:",MCC)
print("AUC:", AUC)
print("TPR:", TPR)
print("FPR:", FPR)

# pred2 = EnsembelNet_model.predict(x_test2 )
# pred2 = np.argmax(pred2, axis=1)
# score2 = indicator(pred2,y_test2)
# Accuracy, Precision, Recall, F_meature = score2.getMetrics()
# Specific = score2.getSpecific()
# TPR, FPR = score2.getfprtpr()
# AUC, x, y = score2.getAuc()
# MCC = score2.getMCC()
# print("Accuracy:", Accuracy)
# print("Precison:",Precision )
# print("Recall:", Recall)
# print("F-meature:",F_meature)
# print("Specific:", Specific)
# print("MCC:",MCC)
# print("AUC:", AUC)
# print("TPR:", TPR)
# print("FPR:", FPR)

# pred2 = model2.predict(x_test2 )
# pred2 = np.argmax(pred2, axis=1)
# score2 = indicator(pred2,y_test2)
# Accuracy, Precision, Recall, F_meature = score2.getMetrics()
# Specific = score2.getSpecific()
# TPR, FPR = score2.getfprtpr()
# AUC, x, y = score2.getAuc()
# MCC = score2.getMCC()
# print("Accuracy:", Accuracy)
# print("Precison:",Precision )
# print("Recall:", Recall)
# print("F-meature:",F_meature)
# print("Specific:", Specific)
# print("MCC:",MCC)
# print("AUC:", AUC)
# print("TPR:", TPR)
# print("FPR:", FPR)