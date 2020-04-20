######################## Wireless Sensor Network#########################################
# Total energy at eacch iteration Graph
# Graph of alive sensors at each iteration
# 




import numpy as np
import matplotlib.pyplot as plt
import random
import time
from math import *


class knn:
    def __init__(self,pos=0,Energy=0):
        if(pos==0):
            self.pos = np.random.randint(100,size=[10,2])
            self.copy_pos = self.pos
        else:
            self.pos = pos
            self.copy_pos = pos
        if(Energy==0):
            self.Energy = np.ones((10,1))*1000
        else:
            self.Energy = Energy
        self.count = 0
        self.count_iter=0
        self.iter=[]
        self.Dead_sensor =np.zeros((10,2))
        self.TotalEnergy=[]
        self.contribution = dict.fromkeys([i for i in range(10)],0)
        #self.T_Energy=np.array(10000)
        #self.Dead_sensor = np.array([0,0])
        print(self.pos,self.Energy)

    def randomNode(self):
        self.r_sensor=random.choice(self.pos)
        if self.r_sensor not in self.Dead_sensor:
            self.r_index = np.where(self.pos==self.r_sensor)[0][0]
        else:
            self.randomNode()
        print(self.r_sensor,self.r_index)
        

    def distance(self):
        self.contribution[self.r_index]+=1
        #self.dist = np.zeros((len(self.pos),1))
        self.dist = np.zeros((10,1))
        for i in range(len(self.pos)):
            if self.pos[i] not in self.Dead_sensor:
                self.dist[i]= sqrt((pow(self.pos[i][0] -self.r_sensor[0],2))+(pow(self.pos[i][1]-self.r_sensor[1],2)))
            else:
                self.dist[i]=10000
        return self.dist

    def neighbours(self):
        #self.index=np.zeros((len(self.pos),1))
        self.index=np.zeros((10,1))
        self.neigh=np.zeros((3,2))
        count=0
        count2=0
        for i in range(len(self.dist)):
            c=np.where(self.dist==np.min(self.dist))[0][0]
            if c!=self.r_index:
                self.index[count2] = np.where(self.dist==np.min(self.dist))[0][0]
                count2+=1
            
##            print("c=",c)
        
            if c!=self.r_index and count!=3 and count<3:
                self.neigh[count] = self.pos[int(c)]
                count+=1
            self.dist[c] = 100
##        print(self.neigh)
##        print(self.dist)
##        print(self.index)
        return self.neigh


    def plotting(self):
        plt.figure(0)
        plt.cla()
        plt.title('Wireless sensor Network')
        plt.plot(self.pos[:,0],self.pos[:,1],'yx')
        for i in range(self.pos.shape[0]):
            plt.text(self.pos[i,0],self.pos[i,1],i+1)
        plt.plot(self.neigh[:,0],self.neigh[:,1],'kx')
        plt.plot(self.r_sensor[0],self.r_sensor[1],'bx')
        plt.plot(self.Dead_sensor[:,0],self.Dead_sensor[:,1],'rx')
        plt.grid(True)
        plt.xlabel("X -->")
        plt.ylabel("Y -->")
        plt.show()

    def PieChart(self):
        self.d = self.contribution
        keys = list(self.d.keys())
        values = list(self.d.values())
        plt.figure(3)
        plt.title('Contribution of Sensors')
        
        plt.pie(values,labels=keys,autopct='%1.1f%%',shadow=True)
        plt.legend(keys)
        plt.show()

    def TotalEnergy(self):
        
        
        np.vstack([self.T_Energy,sum(self.Energy)])
        
        return self.T_Energy

    def EnergyLoss(self):
        self.Energy[self.r_index]-=100+(250-100)*np.random.rand()
        counter=0
        i=0
        while i!=9 and counter!=2:
            if self.pos[i] not in self.Dead_sensor:
                self.Energy[int(self.index[i][0])]-=100+(150-100)*np.random.rand()
                counter+=1
            i+=1
        self.TotalEnergy.append(sum(self.Energy))
        return self.Energy

    def DeadSensor(self):
        
        
        if self.r_sensor not in self.Dead_sensor:
            for i  in range(10):
                
                if self.Energy[i] <=0 and self.pos[i] not in self.Dead_sensor:
                    j=np.where(self.copy_pos==self.pos[i])[0][0]
                    self.Dead_sensor[self.count] = self.pos[i]
                    self.iter.append(self.count_iter)
                    #self.Dead_sensor = np.vstack([self.Dead_sensor,self.pos[i]])
                    self.count+=1
                    self.Energy[i] = 0
                    print(self.pos,"\nDEAD ",self.pos[i])
                    #self.pos = np.delete(self.pos ,(np.where(self.pos==self.pos[i])[0][0]),axis=0)
                    #print(self.pos)
                    #self.pos = self.pos.reshape(int(len(self.pos)/2),2)

        self.count_iter+=1
        print("\nDEAD SENSOR\n",self.Dead_sensor)
                    
##        else:
##            self.randomNode()
##            self.DeadSensor()

    def getSequence(self):
##        self.sequence = []
##        for i in range(self.Dead_sensor.shape[0]):
##            self.sequence.append(np.where(self.Dead_sensor[i] == self.pos)[0][0])
        self.sequence = np.zeros([8])
        count=0
        for i in range(8):
            self.sequence[count]=np.where(self.Dead_sensor[i]==self.pos)[0][0]+1
            count+=1
        return self.sequence

        
    def getDeadSensor(self):
        return self.Dead_sensor

    def check_All_dead(self):
        if all(self.Dead_sensor[i]!=[0,0] for i in self.Dead_sensor):
            return 1
        else:
            return 0
  

if __name__=="__main__":
    sensor = knn()
    
    flag=0
    
    while sensor.count<=7:
    #for i in range(30):
        sensor.randomNode()
        sensor.DeadSensor()
        print("\n\nDistance ",sensor.distance())
        print("\n\n Neigh",sensor.neighbours())
        print("\n\n Energy Loss",sensor.EnergyLoss())
        #print("\n\n Total Energy",sensor.TotalEnergy())
        print("\n\nCount\n\n",sensor.count)
        plt.ion()
        plt.cla
        sensor.plotting()
        plt.pause(1)
        
     #   print(sensor.Dead_sensor[0])
     #   flag = sensor.check_All_dead()
    dead = sensor.getDeadSensor()

##    plt.plot(dead[1:,0],dead[1:,1],'rx')
    print(sensor.getDeadSensor())
##    for i in range(1,(sensor.count+1)):
##        plt.plot(sensor.Dead_sensor[i,0],sensor.Dead_sensor[i,1],'rx')
##        plt.text(dead[i][0],dead[i][1],str(i))
    plt.ioff()
    for i in range(8):
       # print(sensor.Dead_sensor[i][0]-1,sensor.Dead_sensor[i][0]-1,i+1)
        plt.text(sensor.Dead_sensor[i][0]-2,sensor.Dead_sensor[i][1]-2,i+1)
    
    print('\nSEQUENCE OF DEAD SENSORS\n',sensor.getSequence())

    plt.figure(1)
    
    y=20
    c=0
    plt.ion()
    for i in range(len(sensor.TotalEnergy)):
        plt.subplot(1,2,1)
        plt.title('Total Energy Graph')
        plt.grid(True)
        plt.xlabel('Iterations -->')
        plt.ylabel('Total Energy -->')
        plt.xlim([-5,len(sensor.TotalEnergy)+5])
        plt.ylim([min(sensor.TotalEnergy)-100,max(sensor.TotalEnergy)+100])
        plt.plot(i,sensor.TotalEnergy[i],'bo')
        plt.text(i,sensor.TotalEnergy[i],int(sensor.TotalEnergy[i]))
        plt.pause(0.1)

        plt.subplot(1,2,2)
        plt.grid(True)
        plt.title('Rounds Covered by Dead Sensors')
        plt.xlabel('Iterations -->')
        plt.ylabel('Rounds of Dead Sensors -->')
        plt.xlim([-5,len(sensor.TotalEnergy)+5])
        plt.ylim([-2,25])
        if i in sensor.iter:
            y-=1
            plt.text(i,y,sensor.iter[c])
            c+=1
        plt.plot(i,y,'ro')
        plt.pause(0.1)
        
        
    plt.ioff()

    sensor.PieChart()
    
        
        
    
