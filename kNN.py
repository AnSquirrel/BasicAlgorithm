
import numpy as np

trainset = [[0.2, 0.2, 0.2, 0.2],
            [0.4, 0.4, 0.4, 0.4],
            [0.6, 0.6, 0.6, 0.6],
            [1.0, 1.0, 1.0, 1.0],
            [1.2, 1.2, 1.2, 1.2],
            [1.4, 1.4, 1.4, 1.4],
            [2.0, 2.0, 2.0, 2.0],
            [2.2, 2.2, 2.2, 2.2],
            [2.4, 2.4, 2.4, 2.4]]

target = [0, 0, 0, 1, 1, 1, 2, 2, 2]
target_names = ['A', 'B', 'C']
new = [2.0, 2.0, 2.0, 2.0]

class KNeighborsClassifier(object):
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors

    def predict(self, test, train):
        test = np.array(test)
        train = np.array(train)
        dis = list()
        d = 0
        
        for i in range(len(train)):
            d = np.sum(np.square(test - train[i]))
            d = np.sqrt(d)
            dis.append(d)
        # test = np.mat(test)
        # train = np.mat(train)
        # for i in range(len(train)):
        #     d = np.sqrt((test - train[i]) * (test - train[i]).T)
        #     dis.append(d)
        sorts = np.sort(dis, axis=0)
        usort = np.argsort(dis)
        neighbors = list()
        neighbors = sorts[:self.n_neighbors]
        indx = list()
        indx = usort[:self.n_neighbors]     
        # print(dis)
        print(neighbors)
        # print(indx)
        sumindex = 0
        for j in range(len(indx)):
            sumindex = sumindex + indx[j]

        return target[int(sumindex / self.n_neighbors)]


kNN = KNeighborsClassifier(n_neighbors=2)

y_pred = kNN.predict(new, trainset)
target_name = target_names[y_pred]
print(target_name)
