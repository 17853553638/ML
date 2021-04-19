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


def main():
    oob_scores = []
    pred = []
    y_test_sets =[]
    for i in range(1,6):
        print(i)
        # model = SVC(kernel='rbf')
        # model = LogisticRegression()

        # model = RandomForestClassifier(n_estimators=20)
        # model=SVC(gamma='auto', kernel='poly', degree=1, max_iter=-1, probability=True)
        model = DecisionTreeClassifier(max_depth=9,random_state=66)
        # model = BaggingClassifier(SVC(kernel='rbf'), max_samples=0.7, max_features=0.8)
        #读入训练集
        data = pd.read_csv('AB/'+str(i)+'/train.csv',header=None)

        # print(type(idx))
        array = data.values
        dataInfo = data.shape[1]
        X_train = array[:, 1:dataInfo]
        y_train = array[:, 0]


        model.fit(X_train,y_train)

        oob_score = metrics.precision_score(y_train, model.predict(X_train))
        oob_scores.append(oob_score)
        #读入测试集
        data = pd.read_csv('AB/'+str(i)+'/test.csv',header=None)
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


    print("Accuracy:", Accuracy)
    print("Precison:", Precision)
    print("Recall:", Recall)
    print("F-meature:", F_meature)
    print("Specific:", Specific)
    print("MCC:",metrics.matthews_corrcoef(y_true=y_test_sets_mean,y_pred=pred))
    print("AUC:",AUC)
    print("TPR:",TPR)
    print("FPR:",FPR)

if __name__ == '__main__':
    main()






