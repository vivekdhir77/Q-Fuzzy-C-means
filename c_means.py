import numpy as np 
import pandas as pd 
import random
import sklearn.datasets
import sklearn.cluster
from sklearn.metrics import normalized_mutual_info_score
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import f1_score
import time
from utils import *

class Cmeans:
    def __init__(self, df, labelsTrue, epsilon=1, distType=0, m=2):
        self.df = df
        self.labelsTrue = labelsTrue
        self.k = len(set(labelsTrue)) # number of centroids
        self.distType = distType # euclidean-0 | projection-1
        self.m = m # membership value
        self.epsilon = epsilon
        self.dataSize = len(self.df) # no of data points
        self.c = random.sample(self.df, self.k) # random k centroids
        self.dist = [[0 for i in range(self.dataSize)] for j in range(self.k)] # 2d Distance matrix
        self.mem = [[0 for i in range(self.dataSize)] for j in range(self.k)] #initializing memebership matrix
        self.labels = [0 for i in range(self.dataSize)] # predicted
        self.X = np.array(self.df) # dataframe in numpy (without self.labels)

    def c_means(self):
        while True:
            self.dist = calcDistMatrix(self.dist, self.c, self.df, self.distType) # calculating distance values
            self.mem = caclMembershipMatrix(self.mem ,self.dist ,self.dataSize ,self.k, self.m) # calculating membership values
            #mem_final = [self.mem[0][i]+self.mem[1][i]+self.mem[2][i] for i in range(len(self.mem[0]))] 
            new_centroids = calcNewCentroid(self.df, self.mem, self.dataSize, self.k, self.m)
            obj_func = calcObjFunction(self.df,self.mem, new_centroids, self.dataSize, self.k, self.m) # objective funtion between new centroids and datapoints
            old_obj_func = calcObjFunction(self.df,self.mem, self.c, self.dataSize, self.k, self.m) # objective function between old centroids and datapoints
            norm_obj_fun = abs(old_obj_func-obj_func)
            center_diff = [math.sqrt(norm_square(new_centroids[i], self.c[i])) for i in range(self.k)]
            if stoppingCriteria2(center_diff) or norm_obj_fun<self.epsilon:
                break
            self.c = new_centroids
        for i in range(self.dataSize):
            mx = max(row[i] for row in self.mem)
            for j in range(self.k):
                if mx == self.mem[j][i]:
                    self.labels[i] = j+1
                    break

    def getARI(self):
        nplabelsTrue = np.array(self.labelsTrue)
        ari = adjusted_rand_score(nplabelsTrue, self.labels)
        return ari
    def getF1_score(self):
        nplabelsTrue = np.array(self.labelsTrue)
        F1_score = f1_score(nplabelsTrue, self.labels, average='macro')
        return F1_score
    def getNMI(self):
        nplabelsTrue = np.array(self.labelsTrue)
        nmi = normalized_mutual_info_score(nplabelsTrue, self.labels)
        return F1_score 
    def getSI(self):
        nplabels = np.array(self.labels) # predicted self.labels
        score1 = sklearn.metrics.silhouette_score(self.X, nplabels, metric='euclidean')
        return score1
    def getDBS(self):
        nplabels = np.array(self.labels) # predicted self.labels
        score2 = sklearn.metrics.davies_bouldin_score(self.X,nplabels)
        return score2

