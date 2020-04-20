import numpy as np
from sklearn import datasets


##################       DATASETS  TRAINING/TESTING DATA    ################################

def IRIS():
    iris = datasets.load_iris()

    data = iris.data
    target = iris.target

    xtrain = data[:30];xtrain = np.vstack((xtrain,data[50:80],data[100:130]))
    xtest = data[30:50];xtest = np.vstack((xtest,data[80:100],data[130:150]))
    ytrain = target[:30];ytrain = np.hstack((ytrain,target[50:80],target[100:130]))
    ytest = target[30:50];ytest = np.hstack((ytest,target[80:100],target[130:150]))

    return xtrain,xtest,ytrain,ytest


def DIABETES():
    diabetes = datasets.load_diabetes()

    data = diabetes.data
    target = diabetes.target

    xtrain = data[:330]
    xtest = data[330:]
    ytrain = target[:330]
    ytest = target[330:]

    return xtrain,xtest,ytrain,ytest

def DIGITS():
    digit = datasets.load_digits()

    data = digit.data
    target = digit.target

    xtrain = data[:1330]
    xtest = data[1330:]
    ytrain = target[:1330]
    ytest = target[1330:]

    return xtrain,xtest,ytrain,ytest


def BREAST_CANCER():
    cancer = datasets.load_breast_cancer()

    data = cancer.data
    target = cancer.target

    xtrain = data[:430]
    xtest = data[430:]
    ytrain = target[:430]
    ytest = target[430:]

    return xtrain,xtest,ytrain,ytest


def WINE():
    wine = datasets.load_wine()

    data = wine.data
    target = wine.target

    xtrain = data[:45];xtrain = np.vstack((xtrain,data[59:120],data[130:168]))
    xtest = data[45:59];xtest = np.vstack((xtest,data[120:130],data[168:178]))
    ytrain = target[:45];ytrain = np.hstack((ytrain,target[59:120],target[130:168]))
    ytest = target[45:59];ytest = np.hstack((ytest,target[120:130],target[168:178]))

    return xtrain,xtest,ytrain,ytest


def BOSTON():
    boston = datasets.load_boston()

    data = boston.data
    target = boston.target

    xtrain = data[:380]
    xtest = data[380:]
    ytrain = target[:380]
    ytest = target[380:]

    return xtrain,xtest,ytrain,ytest
