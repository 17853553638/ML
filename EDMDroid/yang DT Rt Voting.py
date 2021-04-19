import pandas as pd
from indicator import indicator
from collections import Counter
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.naive_bayes import  GaussianNB
import random
from sklearn.preprocessing import StandardScaler
import numpy as np




def MaxMinNormalization(x):
    """[0,1] normaliaztion"""
    x = (x - np.min(x)) / (np.max(x) - np.min(x))
    return x

# def sigmoid(x):
#     return 1.0 / (1 + np.exp(x))

def weights(scores):
    # avg = sum(scores)/len(scores)
    # weights=[i/len(scores) for i in scores]
    weights = MaxMinNormalization(scores)
    weights=[i/len(weights) for i in weights]
    print(weights)
    return weights

if __name__ == '__main__':
    sumPrecision = 0
    sumRecall = 0
    sumF_meature = 0
    sumAUC = 0
    sumAccuracy = 0
    sumSpecific = 0
    sumMCC = 0
    sumTPR = 0
    sumFPR = 0
    sumx = 0
    sumy = 0


    for i in range(1, 6):
        print("第%d折的结果" % i)
        oob_scores = []
        pred = []
        y_test_sets = []
        for j in range(1, 21):

            model = DecisionTreeClassifier(max_depth=9,random_state=66)
            # model = BaggingClassifier(SVC(kernel='rbf'), max_samples=0.7, max_features=0.8)
            #读入训练集
            data = pd.read_csv('A Rotation/' + str(i) + '/train/' + str(j) + '.csv',header=None)

            # print(type(idx))
            array = data.values
            dataInfo = data.shape[1]
            X_train = array[:, 1:dataInfo]
            y_train = array[:, 0]


            model.fit(X_train,y_train)

            oob_score = metrics.precision_score(y_train, model.predict(X_train))
            oob_scores.append(oob_score)
            #读入测试集
            data = pd.read_csv('A Rotation/' + str(i) + '/test/' + str(j) + '.csv',header=None)
            array = data.values
            dataInfo2 = data.shape[1]
            X_test = array[:, 1:dataInfo2]
            y_test= array[:, 0]


            y_test_sets.append(y_test)
            pred.append(model.predict(X_test))
            print(metrics.accuracy_score(y_test, model.predict(X_test)))
        y_test_sets_mean = np.mean(y_test_sets,axis=0)
        p=np.shape(y_test_sets_mean)[0]

        for i in range(p):
            if y_test_sets_mean[i]>0.5 or y_test_sets_mean[i]==0.5:
                y_test_sets_mean[i]=1
            else :
                y_test_sets_mean[i]=0

        W = weights(oob_scores)

        pred = np.vstack(pred)

        pred = np.transpose(pred)


        result = []

        # 加权投票
        L = len(pred)
        M = len(pred[0])
        result = []
        for j in range(L):
            tmp = {0: 0, 1: 0}
            for k in range(M):
                tmp[pred[j][k]]+=W[k]
            if(tmp[0]>tmp[1]):
                result.append(0)
            elif(tmp[0]<tmp[1]):
                result.append(1)
            else:
                result.append(random.choice([0,1]))


        #硬投票
        result1=[]
        for item in pred:
            result1.append(np.argmax(np.bincount(item.astype('int'))))

        pred = np.array(result1).astype('float')


        score = indicator(pred,y_test_sets_mean)
        Accuracy,Precision,Recall,F_meature = score.getMetrics()
        Specific = score.getSpecific()
        TPR,FPR = score.getfprtpr()
        AUC,x,y = score.getAuc()
        MCC = score.getMCC()

        print("Accuracy:", Accuracy)
        print("Precison:", Precision)
        print("Recall:", Recall)
        print("F-meature:", F_meature)
        print("Specific:", Specific)
        print("MCC:",metrics.matthews_corrcoef(y_true=y_test_sets_mean,y_pred=pred))
        print("AUC:",AUC)
        print("TPR:",TPR)
        print("FPR:",FPR)
        sumAccuracy += Accuracy
        sumPrecision += Precision
        sumRecall += Recall
        sumF_meature += F_meature
        sumAUC += AUC
        sumSpecific += Specific
        sumMCC += MCC
        sumTPR += TPR
        sumFPR += FPR
    print("Average Accuracy:", sumAccuracy / 5)
    print("Average Precision:", sumPrecision / 5)
    print("Average Recall:", sumRecall / 5)
    print("Average F-meature:", sumF_meature /5)
    print("Average Specific:", sumSpecific / 5)
    print("Average MCC:", sumMCC / 5)
    print("Average AUC:", sumAUC / 5)
    print("Average TPR:", sumTPR / 5)
    print("Average FPR:", sumFPR / 5)





