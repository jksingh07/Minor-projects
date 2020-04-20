import random
print("\n\t\tMultiple Choice Questions\n\n")

Questions=[('Q. Who is the Prime Minister of India in 2016'),('Q: What is 2*3+10/5-2'),
           ('Q. Who is the National Animal of India'),('Q. What is 2+2 ?'),('Q. Which Color has Highest wavelength ?'),
           ("Q. How many Seconds are there in a Minute "),('Q. _____ is the first woman to head a public sector bank.'),
           ("Q. Where is Bose institute ?"),("Q. World Tourism Day is celebrated on- "),
           ('Q. When is the International Yoga Day celebrated ?'),("Q. The motif of 'Hampi with Chariot' is printed on the reverse of which currency note ? "),
           ("Q. 'Line of Blood' is a book written by whom?"),("Q. The two-day festival 'North East Calling', is organized by which ministry ?"),
           ("Q. A major in-stream use of water is for -"),('Q.  1+1 =__ ?')]

Options=[('Manmohan Singh','Narendra Modi','Sonia gandhi','indira gandhi'),
         ('1.5','1','6','0'),
         ('Peacock','Tiger','lion','Monkey'),
         ('4','22','2','2+2'),
         ('Blue','Violet','Yellow','Red'),
         ('60s','1s','120s','30s'),
         ('Shikha Sharma','Chanda Kochar','Usha Anan','Arundhati Bhattacharya'),
         ('Dispur','Kolkata','Mumbai','New Delhi'),
         ('September 12','September 25','September 27','September 29'),
         ('June 21 ','March 21 ','April 22 ','May 31'),
         (' One Rupee Note','Rs. 500 note',' Rs. 50 note','Rs. 1000 note'),
         ('Ursula Vernon','Amal EI-Mohtar','Diksha Basu','Bairaj Khanna'),
         ('Ministry of DoNER','Ministry of External Affairs','Ministry of Home Affairs','Ministry of Defence'),
         ('dissolving industrial wastes','agricultural irrigation','domestic use','producing hydroelectric power'),
         ('11','1','2','0')]

Answers = [('Narendra Modi'),('6'),('Tiger'),('4'),('Red'),('60s'),('Arundhati Bhattacharya'),
           ('Kolkata'),('September 27'),('June 21 '),(' Rs. 50 note'),('Bairaj Khanna'),
           ('Ministry of DoNER'),('producing hydroelectric power'),('2')]


right=0
wrong=0
score=0
ch='y'
while ch=='y':
    
    shuffle_i=[]
    shuffle_j=[]
    right=0
    wrong=0
    for i in range(100):
        
        index_i=random.randint(0,14)
        index_j=random.randint(0,3)
        if index_i not in shuffle_i:
                shuffle_i.append(index_i)
        if index_j not in shuffle_j:
                shuffle_j.append(index_j)

    for i in shuffle_i:
        print(Questions[i])
        for j in shuffle_j:
            print(Options[i][j])
        choose = input('>> ')
        if choose == Answers[i]:
            right+=1
        else:
            wrong+=1
        print()

    score=right-wrong

    if score<0:
        score=0
    print("\t\t Your Score : %d \n Right Answers :%d\n Wrong Answers :%d"%(score,right,wrong))
    ch=input("\n\nDo you want to Play Again y/n  :")

if ch!='y':
    print("\n\t\tThank You For Playing!!!\n\n")

input("press ENTER to EXIT")
##    shuffle_i=[]
##    shuffle_j=[]
##    for i in range(10):
##	index_i=random.randint(0,1)
##	index_j=random.randint(0,2)
##	if index_i not in shuffle_i:
##		shuffle_i.append(index_i)
##	if index_j not in final_j:
##		shuffle_j.append(index_j)
