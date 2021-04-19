import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree.tree import DTYPE
from sklearn.ensemble.forest import ForestClassifier
from sklearn.utils import resample, gen_batches, check_random_state
# from sklearn.utils.extmath import fast_dot
from sklearn.decomposition import PCA
import pandas as pd
import os
from sklearn.decomposition import NMF
# from _exceptions import NotFittedError

def random_feature_subsets(array, batch_size, random_state=134):
    """ Generate K subsets of the features in X """
    random_state = check_random_state(random_state)
    features = list(range(array.shape[1]))
    # print(features)
    random_state.shuffle(features)
    for batch in gen_batches(len(features), batch_size):
        yield features[batch]




class RotationTreeClassifier(DecisionTreeClassifier):
    def __init__(self,
                 n_features_per_subset=140,
                 rotation_algo='nmf',
                 criterion="gini",
                 splitter="best",
                 max_depth=None,
                 min_samples_split=2,
                 min_samples_leaf=1,
                 min_weight_fraction_leaf=0.,
                 max_features=1.0,
                 random_state=None,
                 max_leaf_nodes=None,
                 class_weight=None,
                 presort=False):

        self.n_features_per_subset = n_features_per_subset
        self.rotation_algo = rotation_algo

        super(RotationTreeClassifier, self).__init__(
            criterion=criterion,
            splitter=splitter,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            min_weight_fraction_leaf=min_weight_fraction_leaf,
            max_features=max_features,
            max_leaf_nodes=max_leaf_nodes,
            class_weight=class_weight,
            random_state=random_state,
            presort=presort)

    def rotate(self, X):
        # if not hasattr(self, 'rotation_matrix'):
        #     raise NotFittedError('The estimator has not been fitted')
        # print(self.rotation_matrix)
        # print(self.rotation_matrix.shape)
        return np.dot(X, self.rotation_matrix)

    def nmf_algorithm(self):
        """ Deterimine PCA algorithm to use. """
        if self.rotation_algo == 'randomized':
            return NMF()
        elif self.rotation_algo == 'nmf':
            return NMF()
        else:
            raise ValueError("`rotation_algo` must be either "
                             "'nmf' or 'randomized'.")

    def _fit_rotation_matrix(self, X):
        random_state = check_random_state(self.random_state)
        n_samples, n_features = X.shape
        self.rotation_matrix = np.zeros((n_features, n_features),
                                        dtype=int)
        for i, subset in enumerate(
                random_feature_subsets(X, self.n_features_per_subset,
                                       random_state=self.random_state)):
            # take a 75% bootstrap from the rows
            x_sample = resample(X, n_samples=int(n_samples*0.75),
                                random_state=10*i)
            nmf = self.nmf_algorithm()
            W=nmf.fit_transform(x_sample[:, subset])

            self.rotation_matrix[np.ix_(subset, subset)] = nmf.components_

    def get_subsets(self, trainX, trainy,testX,testy):
        self._fit_rotation_matrix(trainX)
        tranX = self.rotate(trainX)
        trany = trainy
        tstX = self.rotate(testX)
        tsty = testy
        return tranX, trany,tstX,tsty

    def write_to_csv(self, X, y,filename):
        Xn = pd.DataFrame(X)
        y = np.reshape(y, [-1, 1])
        yn = pd.DataFrame(y)
        pd_data = pd.concat([yn,Xn], axis=1)
        pd_data.to_csv(filename,header=0,index=0)

    def fit(self, X, y, sample_weight=None, check_input=True):
        self._fit_rotation_matrix(X)
        super(RotationTreeClassifier, self).fit(self.rotate(X), y,
                                                sample_weight, check_input)


    def predict_proba(self, X, check_input=True):
        return  super(RotationTreeClassifier, self).predict_proba(self.rotate(X),
                                                                  check_input)

    def predict(self, X, check_input=True):
        return super(RotationTreeClassifier, self).predict(self.rotate(X),
                                                           check_input)

    def apply(self, X, check_input=True):
        return super(RotationTreeClassifier, self).apply(self.rotate(X),
                                                         check_input)

    def decision_path(self, X, check_input=True):
        return super(RotationTreeClassifier, self).decision_path(self.rotate(X),
                                                                 check_input)

class RotationForestClassifier(ForestClassifier):
    def __init__(self,
                 n_estimators=10,
                 criterion="gini",
                 n_features_per_subset=3,
                 rotation_algo='pca',
                 max_depth=None,
                 min_samples_split=2,
                 min_samples_leaf=1,
                 min_weight_fraction_leaf=0.,
                 max_features=1.0,
                 max_leaf_nodes=None,
                 bootstrap=False,
                 oob_score=False,
                 n_jobs=1,
                 random_state=None,
                 verbose=0,
                 warm_start=False,
                 class_weight=None):
        super(RotationForestClassifier, self).__init__(
            base_estimator=RotationTreeClassifier(),
            n_estimators=n_estimators,
            estimator_params=("n_features_per_subset", "rotation_algo",
                              "criterion", "max_depth", "min_samples_split",
                              "min_samples_leaf", "min_weight_fraction_leaf",
                              "max_features", "max_leaf_nodes",
                              "random_state"),
            bootstrap=bootstrap,
            oob_score=oob_score,
            n_jobs=n_jobs,
            random_state=random_state,
            verbose=verbose,
            warm_start=warm_start,
            class_weight=class_weight)

        self.n_features_per_subset = n_features_per_subset
        self.rotation_algo = rotation_algo
        self.criterion = criterion
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.min_weight_fraction_leaf = min_weight_fraction_leaf
        self.max_features = max_features
        self.max_leaf_nodes = max_leaf_nodes

if __name__ =='__main__':
    import random
    randomNums = random.sample(range(1000, 1200), 20)
    # dt = DecisionTreeClassifier()
    for i in range(1,6):
        filename = 'AB/' + str(i) + '/train.csv'
        data = pd.read_csv(filename, header=None)
        array = data.values
        dataInfo = data.shape[1]
        print(dataInfo)
        trainX = array[:, 1:dataInfo]
        trainy = array[:, 0]

        filename2 = 'AB/' + str(i) + '/test.csv'
        data2 = pd.read_csv(filename2, header=None)
        array2 = data2.values
        dataInfo2 = data2.shape[1]
        testX = array2[:, 1:dataInfo2]
        testy = array2[:, 0]

        k = 1
        for seed in randomNums:
            print(seed)
            RTC = RotationTreeClassifier(random_state=seed)
            tranX, trany,tstX,tsty = RTC.get_subsets(trainX,trainy,testX,testy)
            if not os.path.exists("AB Rotation/"+str(i)+"/train/"):
                os.makedirs("AB Rotation/"+str(i)+"/train/")
            if not os.path.exists("AB Rotation/"+ str(i) + "/test/"):
                os.makedirs("AB Rotation/" + str(i) + "/test/")
            RTC.write_to_csv(filename="AB Rotation/"+str(i)+"/train/"+str(k)+".csv",X=tranX,y=trany)
            RTC.write_to_csv(filename="AB Rotation/" + str(i) + "/test/" + str(k) + ".csv", X=tstX, y=tsty)
            k += 1
        print("数据集生成完毕！")
