import matplotlib.pyplot as plt
import  numpy as np
from math import *

class transform:
    def __init__(self,shape=0,x=0,y=0):
        
        
        if shape==0:
            self.shape = input("Enter The shape : ")
            self.shape = self.shape.capitalize()
            if self.shape == 'Polygon':
                
                self.x = input("Enter The X-Axis Dimensions by seperating with comma  :").split(',')
                self.x = [int(x) for x in self.x]

                self.y = input("Enter The Y-Axis Dimensions by seperating with comma  :").split(',')
                self.y = [int(y) for y in self.y]
                self.Dim = np.zeros((2,len(self.x)+1))
                self.x.append(self.x[0])
                self.y.append(self.y[0])
                self.Dim[0] = self.x;
                self.Dim[1] = self.y;
                
            elif self.shape=='Disc':
                self.Dim = np.zeros((2,1))
                self.cx = int(input("Enter the X - coordinate :"))
                self.cy = int(input("Enter the Y - coordinate :"))
                self.theta = np.arange(0,2*np.pi,0.1)
                self.x = self.cx + self.r*sin(theta)
                self.y = self.cy + self.r*cos(theta)
                self.Dim[0] = self.cx; self.Dim[1] = self.cy;
                self.r = int(input("Enter the Radius"))

            else :
                print("\n\nSorry, Our Software is not designed to transform this figure!!!\nSelect Either Polygon OR Disc\nThank You")
                exit
        else :
            self.shape = shape
            self.x = x
            self.y = y
            self.Dim = np.zeros((2,len(self.x)+1))
            self.x.append(self.x[0])
            self.y.append(self.y[0])
            self.Dim[0] = self.x;
            self.Dim[1] = self.y;
    

    def TransForm_Polygon(self):
        self.S = np.zeros((2,2))
        print("\n\n\tENTER THE INFORMATION FOR TRANSFORMATION BELOW\n")
        self.R_theta = int(input("\n\nEnter the degree of Rotation :"))
        self.s = input("\nEnter The SCALE(x,y) :").split(',')
        self.t = input("\nEnter The Translation(x,y) :").split(',')
        self.s = [int(x) for x in self.s]
        self.t = [int(x) for x in self.t]

        ##########  Doing Scaling ##################
        self.S[0][0] = self.s[0];self.S[1][1] = self.s[1];

        self.new_S = np.zeros((2,len(self.x)))

        for i in range(self.S.shape[0]):
            for j in range(self.Dim.shape[1]):
                for k  in range(self.S.shape[1]):
                    self.new_S[i][j] += self.S[i][k]*self.Dim[k][j];
        self.Dim = self.new_S
        print("\n\nAFTER SCALING DIMENSIONS ARE :\n",self.Dim[:,:self.Dim.shape[1]-1])

        ##############  Doing Rotation  #################

        self.R = np.zeros((2,2))
        self.R[0][0] = cos((np.pi/180)*self.R_theta)
        self.R[0][1] = -1*sin((np.pi/180)*self.R_theta)
        self.R[1][0] = sin((np.pi/180)*self.R_theta)
        self.R[1][1] = cos((np.pi/180)*self.R_theta)

        self.new_R = np.zeros((2,len(self.x)))
        for i in range(self.R.shape[0]):
            for j in range(self.Dim.shape[1]):
                for k  in range(self.R.shape[1]):
                    self.new_R[i][j] += self.R[i][k]*self.Dim[k][j];
        self.Dim = self.new_R

        print("\n\nAFTER ROTATION DIMENSIONS ARE :\n",self.Dim[:,:self.Dim.shape[1]-1])

        
        ######## Doing Translation ##############
        self.Dim[0]+=self.t[0]
        self.Dim[1]+=self.t[1]

        print("\n\nAFTER TRANSLATION DIMENSIONS ARE :\n",self.Dim[:,:self.Dim.shape[1]-1])


        


        


    def TransForm_Disc(self):
        print("\n\n\tENTER THE INFORMATION FOR TRANSFORMATION BELOW\n")
        self.R_theta = int(input("\n\nEnter the degree of Rotation :"))
        self.s = int(input("\nEnter The SCALE :"))
        self.t = input("\nEnter The Translation(x,y) :").split(',')
        self.t = [int(x) for x in self.t]

        ############ DOING SCALING  ########################
        self.r*=self.x

    def plotting(self):
        #plt.figure(0)
        plt.grid(True)
        plt.xlim(-50,50)
        plt.ylim(-50,50)
        #plt.title("2D Transformation Geometry")
        plt.plot(self.Dim[0,:],self.Dim[1,:])
        #plt.show()


if __name__=="__main__":
    
    #fig = transform('polygon',[1,6,6,1],[2,2,5,5])
    fig = transform()
    print("\n\nORIGINAL DIMENSIONS ARE :\n",fig.Dim[:,:fig.Dim.shape[1]-1])
    plt.figure(0)
    plt.subplot(1,2,1)
    plt.title('Original')
    fig.plotting()
    if fig.shape=='Polygon':
        fig.TransForm_Polygon()
        plt.subplot(1,2,2)
        plt.title('After Transformation')

        fig.plotting()
    elif fig.shape =='Disc':
        fig.TransForm_Disc()
    plt.show()
