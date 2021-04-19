import tensorflow as tf
import numpy as np
import pandas as pd
from indicator import indicator
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from library.AutoSetSeed import *
setup_seed("Tf",seed=1)
print(tf.__version__)
data1=pd.read_csv("权限和Hardware删除特征和为1转换01标签.csv", header=None)
y=data1.values[:,0]
X=data1.values[:,1:]
x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=8)

data2=pd.read_csv("权限和可疑API删除特征和为1转换01标签.csv", header=None)
y2=data2.values[:,0]
X2=data2.values[:,1:]
x_train2,x_test2,y_train2,y_test2=train_test_split(X2,y2,random_state=8)

data3=pd.read_csv("Intent和四大组件删除特征和为1与质心的欧式距离相似度转换01标签.csv",header=None)
y3=data3.values[:,0]
X3=data3.values[:,1:]
x_train3,x_test3,y_train3,y_test3=train_test_split(X3,y3,random_state=8)

input = Input(shape=(196,))   #单条数据维度，不包括数据总数
#构建多层神经网络
d_1 = Dense(5000,activation='relu')(input)
d_1=keras.layers.Dropout(0.2)(d_1)
d_2 = Dense(2500,activation='relu')(d_1)

d_3 = Dense(1000,activation='relu')(d_2)


input2= Input(shape=(196,))
d_1_2 = Dense(5000,activation='relu')(input2)
d_1_2=keras.layers.Dropout(0.2)(d_1_2)
d_2_2= Dense(2500,activation='relu')(d_1_2)
d_3_2= Dense(1000,activation='relu')(d_2_2)

input3= Input(shape=(35117,))
d_1_3 = Dense(5000,activation='relu')(input3)
d_1_3=keras.layers.Dropout(0.2)(d_1_3)
d_2_3= Dense(2500,activation='relu')(d_1_3)
d_3_3= Dense(1000,activation='relu')(d_2_3)

x_concat=tf.keras.layers.Concatenate(axis=-1)([d_3,d_3_2,d_3_3])

d_3_Merg = Dense(500,activation='relu')(x_concat)
d4 = Dense(100,activation='relu')(d_3_Merg)
d5 = Dense(10,activation='relu')(d4)
y = Dense(2,activation='sigmoid')(d5)  #最后一层sigmoid分类

model = Model([input,input2,input3],y)
model.summary()
model.compile(loss="sparse_categorical_crossentropy",optimizer = "adam",metrics=["accuracy"])
model.fit([x_train,x_train2,x_train3],y_train,batch_size=100,epochs=10,verbose=2)
pred =model.predict([x_test,x_test2,x_test3])
pred=np.argmax(pred,axis=1)
score=indicator(pred,y_test)
Accuracy,Precision,Recall,F_meature=score.getMetrics()
Specific =score.getSpecific()
TPR,FPR=score.getfprtpr()
AUC,x,y=score.getAuc()
MCC=score.getMCC()
print ("Accuracy",Accuracy)
print ("Precision",Precision)
print ("Recall",Recall)
print ("F_meature",F_meature)
print ("Specific",Specific)
print ("MCC",MCC)
print ("AUC",AUC)
print ("TPR",TPR)
print ("FPR",FPR)