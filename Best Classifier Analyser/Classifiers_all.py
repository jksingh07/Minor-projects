import numpy as np
from sklearn import datasets,metrics,tree,svm,ensemble
from sklearn.neural_network import MLPClassifier
import random
from Datasets_all import *


##iris = datasets.load_iris()
##
##data = iris.data
##target = iris.target

# BY SHUFFLING

##data_2 = data.copy()
##target_2 = []
##random.shuffle(data_2)
##
##for x in range(data.shape[0]):
##
##    i = np.where(data_2[x][0]==data[:,0])[0]
##    j = np.where(data_2[x][1]==data[:,1])[0]
##    k = np.where(data_2[x][2]==data[:,2])[0]
##    l = np.where(data_2[x][3]==data[:,3])[0]
##
##    index =''
##    n = min(len(i),len(j),len(k),len(l))
##
##    for c in range(n):
##        if j[i[0]==j] == k[i[0] == k]:
##            if j[i[0]==j] == l[i[0] == l]:
##                    index = i[0]
####        print(index)
##        if index != '':
##            break
##    if index == '':
##        index=0
####    print(index,target[index])
##    
##    target_2.append(target[index])


#########   BY SLICING   ##################
##
##xtrain = data[:30];xtrain = np.vstack((xtrain,data[50:80],data[100:130]))
##xtest = data[30:50];xtest = np.vstack((xtest,data[80:100],data[130:150]))
##ytrain = target[:30];ytrain = np.hstack((ytrain,target[50:80],target[100:130]))
##ytest = target[30:50];ytest = np.hstack((ytest,target[80:100],target[130:150]))


def Decision_Tree(xtrain,xtest,ytrain,ytest):
    # Creatng A decision tree model
    dec = tree.DecisionTreeClassifier()

    # Training Model
    train_dec = dec.fit(xtrain,ytrain)

    # Testing
    predict = train_dec.predict(xtest)

    #Accuracy Score

    accuracy = metrics.accuracy_score(ytest,predict)

    # Report
    report = metrics.classification_report(ytest,predict)
   # print(report,'\n\t\tACCURACY : ',accuracy)
    return report,accuracy

    

def Random_Forest(xtrain,xtest,ytrain,ytest):
    # Creatng A decision tree model
    rf_model =  ensemble.RandomForestClassifier()

    # Training Model
    train_rf = rf_model.fit(xtrain,ytrain)

    # Testing
    predict = train_rf.predict(xtest)

    #Accuracy Score

    accuracy = metrics.accuracy_score(ytest,predict)

    # Report
    report = metrics.classification_report(ytest,predict)
    #print(report,'\n\t\tACCURACY : ',accuracy)
    return report,accuracy

    


def SvM(xtrain,xtest,ytrain,ytest):
    # Creatng A decision tree model
    svm_model = svm.SVC()

    # Training Model
    train_svm = svm_model.fit(xtrain,ytrain)

    # Testing
    predict = train_svm.predict(xtest)

    #Accuracy Score

    accuracy = metrics.accuracy_score(ytest,predict)

    # Report
    report = metrics.classification_report(ytest,predict)
    #print(report,'\n\t\tACCURACY : ',accuracy)
    return report,accuracy

    

def Neural_Networks(xtrain,xtest,ytrain,ytest):
    # Creatng A decision tree model
    neural_model = MLPClassifier()

    # Training Model
    train_neural = neural_model.fit(xtrain,ytrain)

    # Testing
    predict = train_neural.predict(xtest)

    #Accuracy Score

    accuracy = metrics.accuracy_score(ytest,predict)

    # Report
    report = metrics.classification_report(ytest,predict)
   # print(report,'\n\t\tACCURACY : ',accuracy)
    return report,accuracy

    

xtrain,xtest,ytrain,ytest = IRIS()
##
##
report,accuracy=SvM(xtrain,xtest,ytrain,ytest)
print(report,'\n\t\tACCURACY : ',accuracy)
