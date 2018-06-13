#!/usr/bin/python3
import numpy
import sklearn
from sklearn import tree
#features about apple and orange
#where 0 means smoooth and 1 means bumpy

data=[[100,0],[130,0],[135,1],[150,1]]
output=["apple","apple","orange","orange"]

#decision tree algo call
algo = tree.DecisionTreeClassifier()

#trained algo
trained_algo = algo.fit(data,output)

#testing phase
predict = trained_algo.predict([[100,1]])

print(predict)

