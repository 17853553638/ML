from sklearn.svm import SVC
from indicator import indicator
from sklearn.model_selection import train_test_split
import pandas as pd
# i=6
# while(i<=120):
#     print(i)
filename ='第三轮30个权限数据集.csv'
data = pd.read_csv(filename,header=None)
array = data.values
dataInfo = data.shape[1]
X = array[:,1:dataInfo]
y = array[:,0]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state=66)
svm=SVC()
svm.fit(x_train,y_train)
pred=svm.predict(x_test)
score=indicator(pred,y_test)
Accuracy, Precision, Recall, F_meature = score.getMetrics()
TPR, FPR = score.getfprtpr()
print("Accuracy:", Accuracy)
print("Precison:", Precision)
print("Recall:", Recall)
print("F-meature:", F_meature)
print("TPR:", TPR)
print("FPR:", FPR)
    # i=i+6