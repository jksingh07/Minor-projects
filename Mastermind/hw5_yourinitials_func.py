import numpy as np
from itertools import combinations
import random



#############     FUNCTIONS     #############################
def gen_vector(C,D):
    global guess_vector,answer,r_guess
    a_C=[]
    
    for i in range(C):
       a_C.append(i+1) 
    guess_vector = list(combinations(a_C,D))
    answer = random.choice(guess_vector)
    r_guess = random.choice(guess_vector)
    ###   ####   ####print(answer)
##    while(True):
##        if answer == r_guess:
##            r_guess = random.choice(guess_vector)
##        else:
##            break

    TF = []
    for i in range(len(guess_vector)):
        TF.append(True)

    return guess_vector,answer,r_guess,TF


def check_matches(ans,guess):
    correct = 0

    for i in range(len(ans)):
        if ans[i] == guess[i]:
            correct+=1

    return correct




def Mastermind_Guess_Game(Color=0,Digit=0,comp=0):
    global C,D,guess_vector
    

################  CODE MAKER       ####################################
    if comp == 0:
        print("\t\t\tMASTERMIND\n\n")
        print("\t\tCode Maker's Turn\n")
    if Color!=0 and Digit!=0:
        C=Color
        D=Digit
        flag = 1
    else:
        C = int(input("With How Many Colors you want to play : "))
        D = int(input("With How Many Digits you want to make Code : "))
    
    #return C,D

    R = 8      # NO. of Rounds
    

    colors = ['Red','White','Green','Violet','Orange','Indigo','Black','Blue','Yellow']
    ##index = []
    ##print("\nEnter a unique Digit(1-%d) for the colors below:-\n"%C)
    ##for i in range(D):
    ##    print(colors[i],end='')
    ##    ind = int(input('->'))
    ##    index.append(ind)
    if comp==0:
        option = int(input("\nWant to Make your own code press 1\nWant to generate a random code press 2\n>>"))

    comb,ans,r_guess,TF = gen_vector(C,D)
    ans = list(ans)
    
    if comp == 0:
        if option == 1:
            print("Available Colors :\n",colors[:C],"\nNote:\n 1.Use only 1-%d numbers for making the code\n2.Remember Code is the Index value of Colors Starting from 1 ="%(C))
            ans = input("\nMake The Code of %d digits : "%D)
            ans = [int(x) for x in list(ans)]

    ##############    CODE BREAKER      ##################################
    if comp==0:
        print('\n'*100)
        print("\n\t\tLet's Play The Game !!!\n\t\tCode Breaker's Turn\n")
        print("\n List Of Colors :\n",colors[:C],"\nGuess a Code of %d Digits(1-%d) Which are index values of colors starting from 1"%(D,C))

        hint = int(input("\n\nHINT\nON - 1\nOFF - 2\n>>"))
    guess_vector = np.array(guess_vector)
    while(True):
        if comp==0:
            print("\nCHANCES LEFT :",R)
            guess = input("Guess The Code : ")
            guess = [int(x) for x in list(guess)]
        else:
            guess = list(random.choice(guess_vector))
            ###   ####   ####print(guess)
        if comp==0:
            while(True):
                if len(guess)!=D:
                    print("\nEnter %d digits code"%D)
                    guess = input("Guess The Code : ")
                    guess = [int(x) for x in list(guess)]
                else:
                    break

        score = check_matches(ans,guess)
        if comp==0:
            print("\nCORRECT MATCHES ARE ",score)
        

        for i in range(len(guess_vector)):
            if check_matches(guess,list(guess_vector[i])) == score:
                TF[i] = True
            else:
                TF[i] = False
        guess_vector = guess_vector[TF]
        
        TF = []
        for i in range(len(guess_vector)):
            TF.append(True)
        R-=1
        if comp==0:
            if hint == 1:
                print("HINT : Combinations Which have exactly %d match with your guess are given below :\n"%score,guess_vector,'\nAdvice: Try combinations shown above may be one of them is correct \n')
        if ans == guess:
            if comp == 0:
                print("\t\tCONGRATULATIONS!!!\n\t\tYOU WON")
            break

        if R == 0:
            if comp == 0:
                print("\n\t\tGAME OVER\n\t\t YOU LOSE")
            R=8
            break

    if comp==0:            
        print("Correct Code is ",ans)
        for i in ans:
            print(colors[i-1],end=', ')

    R = 8-R
    return R



if __name__ == '__main__':
    
    Rounds = Mastermind_Guess_Game()
    print("\n\nTotal Rounds Taken",Rounds)
