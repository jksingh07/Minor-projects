import numpy as np
import matplotlib.pyplot as plt
from hw5_yourinitials_func import *

test_comb = np.array([6,4,8,5,9,6]).reshape(3,2) # COMBINATION FOR TESTING
n = int(input("No. of Testing for Each Combination : ")) # NO. OF ITERATIONS
rounds = np.zeros((3,n)) # TRACKS THE ROUND IN EVERY ITERATION FOR ALL COMB.
R_avg = np.zeros((3,1)) # AVERAGE OF ROUNDS IN EACH COMBINATION
win_perc = np.zeros((3,1)) # WIN PERCENTAGE IN EACH COMBINATIION


for i in range(3):
    win = 0
    for j in range(n):
        r=Mastermind_Guess_Game(test_comb[i][0],test_comb[i][1],1)
        rounds[i][j] = r

        if r!=0:
            win+=1
    win_perc[i] = (win/n)*100

for i in range(3):
    R_avg[i] = (int(sum(rounds[i]))/(8*n))*100

print("\n\nTest Combination\n",test_comb,'\n\nRounds:\n',rounds,'\n\nWin Percentage:\n',win_perc,'\n\nAverage Rounds\n',R_avg)

######   PLOTTING HISTOGRAM ##############
plt.figure(0)

plt.subplot(1,3,1)
plt.title('C=6 D=4')
plt.ylabel('No. Of Times(n) -->')
plt.xlabel('No. of Rounds(R) -->')
plt.hist(rounds[0])

plt.subplot(1,3,2)
plt.title('C=8 D=5')
plt.xlabel('No. of Rounds(R) -->')
plt.hist(rounds[1])

plt.subplot(1,3,3)
plt.title('C=9 D=6')
plt.xlabel('No. of Rounds(R) -->')
plt.hist(rounds[2])

plt.show()

