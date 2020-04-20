from Classifiers_all import *
from Datasets_all import *

if __name__=='__main__':
    temp =''
    option = int(input("SELECT ANY ONE DATASET TO FIND IT'S BEST CLASSIFIER\n\
            1 - IRIS\n\
            2 - DIGITS\n\
            3 - BREAST CANCER\n\
            4 - WINE\n\
            5 - DIABETES\n\
            >>"))

    if option == 1:
        xtrain,xtest,ytrain,ytest = IRIS()
        temp = 'IRIS'
    elif option == 2:
        xtrain,xtest,ytrain,ytest = DIGITS()
        temp = 'DIGITS'
    elif option == 3:
        xtrain,xtest,ytrain,ytest = BREAST_CANCER()
        temp = 'BREAST CANCER'
    elif option == 4:
        xtrain,xtest,ytrain,ytest = WINE()
        temp = 'WINE'
    elif option == 5:
        xtrain,xtest,ytrain,ytest = DIABETES()
        temp = 'DIABETES'
    else :
        print("\n\n\t\tINVALID OPTION")

    Classifiers_name = ['SvM','Decision_Tree','Random_Forest','Neural_Networks']
    score = []
    reports = []

    report,accuracy=SvM(xtrain,xtest,ytrain,ytest)
    score.append(accuracy)
    reports.append(report)

    report,accuracy=Decision_Tree(xtrain,xtest,ytrain,ytest)
    score.append(accuracy)
    reports.append(report)

    report,accuracy=Random_Forest(xtrain,xtest,ytrain,ytest)
    score.append(accuracy)
    reports.append(report)

    report,accuracy=Neural_Networks(xtrain,xtest,ytrain,ytest)
    score.append(accuracy)
    reports.append(report)
    

##    for i in Classifiers_name: 
##        report,accuracy=i(xtrain,xtest,ytrain,ytest)
##        score.append(accuracy)
##        reports.append(report)

    max_index = score.index(max(score))
    min_index = score.index(min(score))
    
    best_classifier = Classifiers_name[max_index]
    worst_classifier = Classifiers_name[min_index]

    print("\n\nRESULT :-\n\nFor The Dataset %s Best Classifier is %s with the Accuracy of %d"%(temp,best_classifier.upper(),score[max_index]*100))
    print("\nWorst Classifier is %s with Accuracy of %d"%(worst_classifier.upper(),score[min_index]*100))
    print(reports[max_index],'\n\t\tACCURACY : ',score[max_index])

