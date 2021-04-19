from sklearn import metrics
import numpy as np

class indicator(object):
    def __init__(self,pred,y_test):
        self.pred = pred
        self.y_test = y_test
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        self.Accuracy = 0
        self.Precison = 0
        self.Recall = 0
        self.F_meature=0
        self.Specific = 0
        self.mcc = 0
        self.tpr = 0
        self.fpr = 0
        self.auc = 0

        #计算TP,TN,FP,FN
        for i in range(len(self.pred)):
            if (self.pred[i] == self.y_test[i] and self.y_test[i] == 1):
                self.TP += 1
            elif (self.pred[i] == self.y_test[i] and self.y_test[i] == 0):
                self.TN += 1
            elif (self.pred[i] != self.y_test[i] and self.y_test[i] == 0):
                self. FP += 1
            elif (self.pred[i] != self.y_test[i] and self.y_test[i] == 1):
                self.FN += 1
        #计算分类指标
        self.Precision = metrics.precision_score(y_true=self.y_test, y_pred=self.pred)
        self.Recall = metrics.recall_score(y_true=self.y_test, y_pred=self.pred)
        self.F_meature = metrics.f1_score(y_true=self.y_test, y_pred=self.pred)
        self.Accuracy = metrics.accuracy_score(self.y_test,y_pred=self.pred)

        #计算specific
        self.Specific = Specific = 100*(self.TN/(self.TN + self.FP))

        #计算fpr，tpr
        self.TPR = self.TP / (self.TP + self.FN)
        self.FPR = self.FP / (self.FP + self.TN)

        #计算MCC
        self.MCC= metrics.matthews_corrcoef(y_true=y_test.astype('int'),y_pred=pred)



    def getMetrics(self):
        return self.Accuracy,self.Precision,self.Recall,self.F_meature

    def getSpecific(self):
        return self.Specific

    def getfprtpr(self):
        return self.TPR,self.FPR

    def getMCC(self):
        return self.MCC
    def getAuc(self):
        AUC = 0
        m = self.y_test.shape[0]
        pos_num = (self.TP + self.FN)
        neg_num = (self.TN + self.FP)
        x = np.zeros([m + 1])

        y = np.zeros([m + 1])

        x[0] = 1
        y[0] = 1

        for i in range(1, m):
            TP = 0
            FP = 0
            for j in range(i, m):
                if (self.pred[j] == self.y_test[j] and self.y_test[j] == 1):
                    TP += 1
                elif (self.pred[j] != self.y_test[j] and self.y_test[j] == 0):
                    FP += 1
            # print(TP)
            x[i] = FP / neg_num
            y[i] = TP / pos_num
            AUC += (y[i] + y[i - 1]) * (x[i - 1] - x[i]) / 2

        x[m] = 0
        y[m] = 0
        AUC += y[m - 1] * x[m - 1] / 2

        self.auc=AUC
        return self.auc,x,y #返回auc和x,y用于计算



