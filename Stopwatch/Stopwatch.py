from tkinter import *
##root=Tk()
##
##
##def hello():
##    print('hello world')
##    l.config(text='hello')
##    l.after(1000,hello)
##
##    
##
##f=Frame(root)
##f.pack(side=TOP,fill=BOTH,expand=YES)
##l=Label(f,text='one',bg='cyan')
##l.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
##l=Label(f,text='two',bg='lightgreen')
##l.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
##
##f=Frame(root)
##f.pack(side=TOP,fill=BOTH,expand=YES)
##l=Label(f,text='three',bg='cyan')
##l.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
##l=Label(f,text='four',bg='lightgreen')
##l.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)
##
##f=Frame(root)
##f.pack(side=TOP,fill=BOTH,expand=YES)
##l=Label(f,text='three',bg='cyan')
##l.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
##l=Label(f,text='four',bg='lightgreen')
##l.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)
##
##
##b=Button(root,text='CLICK',command=hello)
##b.pack(side=TOP,fill=BOTH,expand=YES,padx=5,pady=5)
##
##b=Button(root,text='close',command=root.destroy)
##b.pack(side=TOP,fill=BOTH,expand=YES,padx=5,pady=5)
##
##
##
##
##
##
##





#STOPWATCH
import time
from tkinter import messagebox
root=Tk()
root.title("STOPWATCH")


stop_time=0
absolute_start_time=0
flag=0
flag2=0
def start():
    global flag
    global stop_time
    global absolute_start_time
    global flag2
    #print(stop_time)
    
    absolute_start_time=time.time()
    
##    if flag2==0:
##        absolute_start_time=s_time
##        flag2=1
    
    start_time=time.time()
    #print(s_time)
    l11.config(text=time.ctime(absolute_start_time).split()[3])
   # l4.config(text=time.ctime(start_time).split()[3])
    #l4.after(1000,start)
   # if flag==1:
    #    stop_time=s_time


def stop():
    global flag
    global stop_time
    global absolute_start_time
    flag=1
    #start()
    #print(stop_time)
    stop_time=time.time()
    l12.config(text=time.ctime(stop_time).split()[3])
    total_time_taken()


    
def total_time_taken():
    global absolute_start_time
    global flag2
    global stop_time
##    time_diff_hrs=time.localtime(stop_time)[3]-time.localtime(absolute_start_time)[3]
##    time_diff_min=time.localtime(stop_time)[4]-time.localtime(absolute_start_time)[4]
##    time_diff_sec=time.localtime(stop_time)[5]-time.localtime(absolute_start_time)[5]
##    l2.config(text=str(time_diff_hrs)+":"+str(time_diff_min)+":"+str(time_diff_sec))

    time_diff_hrs=time.localtime(stop_time)[3]-time.localtime(absolute_start_time)[3]
    time_diff_min=time.localtime(stop_time)[4]-time.localtime(absolute_start_time)[4]
    time_diff_sec=time.localtime(stop_time)[5]-time.localtime(absolute_start_time)[5]
    if time_diff_sec<0:
        time_diff_min-=1
        time_diff_sec+=60
        l2.config(text=str(time_diff_hrs)+":"+str(time_diff_min)+":"+str(time_diff_sec))
    else :
        l2.config(text=str(time_diff_hrs)+":"+str(time_diff_min)+":"+str(time_diff_sec))


def reset():
    #global absolute_start_time
    #global stop_time
    l11.config(text="00:00:00")
    l12.config(text="00:00:00")
    l2.config(text="00:00:00")


    
def close():
    msg=messagebox.showinfo("Quit","Are you sure you want to close")
    if msg=='ok':
        root.destroy()


def clock():
    start_time=time.time()
    l4.config(text=time.ctime(start_time).split()[3])
    l4.after(1000,clock)

f1=Frame(root)
l11=Label(f1,text="START TIME",fg='yellow',bg='red',width=30,height=5,font='algerian',bd=5,relief=GROOVE,cursor='dot')
l12=Label(f1,text="END TIME",fg='yellow',bg='red',width=30,height=5,font='algerian',bd=5,relief=GROOVE,cursor='dot')
f1.pack(side=TOP,fill=BOTH,expand=YES)
l11.pack(side=LEFT,padx=10,pady=10,expand=YES)
l12.pack(side=RIGHT,padx=10,pady=10,expand=YES)



f2=Frame(root)
l2=Label(f2,text="TOTAL TIME TAKEN",fg='yellow',bg='red',width=30,height=5,font='algerian',bd=5,relief=RIDGE,cursor='dot')
f2.pack(side=TOP,fill=BOTH,expand=YES)
l2.pack(side=LEFT,padx=10,pady=10,expand=YES)


f3=Frame(root)
b1=Button(f3,text="START",command=start,fg='cyan',bg='black',activebackground='cyan',width=10,height=5,bd=5,relief=RAISED)
b2=Button(f3,text="STOP",command=stop,fg='cyan',bg='black',activebackground='cyan',width=10,height=5,bd=5,relief=RAISED)
b3=Button(f3,text="RESET",command=reset,fg='cyan',bg='black',activebackground='cyan',width=10,height=5,bd=5,relief=RAISED)
b4=Button(f3,text="CLOSE",command=close,fg='cyan',bg='black',activebackground='cyan',width=10,height=5,bd=5,relief=RAISED)
f3.pack(side=TOP,fill=BOTH,expand=YES)
b1.pack(side=LEFT,padx=5,pady=5,expand=YES)
b2.pack(side=LEFT,padx=5,pady=5,expand=YES)
b3.pack(side=LEFT,padx=5,pady=5,expand=YES)
b4.pack(side=LEFT,padx=5,pady=5,expand=YES)



f4=Frame(root)
l4=Label(f4,text="START CLOCK",bg='white',fg='black',bd=5,relief=RIDGE,font='calgiri',wraplength=90)
f4.pack(side=TOP,expand=YES,fill=BOTH)
l4.pack(side=TOP,fill=BOTH,expand=YES,padx=10,pady=10)
clock()

##f5=Frame(root,bd=5,bg='yellow')
##b51=Button(f5,image='http://pluspng.com/img-png/png-stopwatch-stopwatch-png-image-1496.png',height=50,width=80)
##b51.pack(side=TOP,fill=BOTH,expand=YES,padx=5,pady=5)
##f5.pack(side=TOP,fill=BOTH,expand=YES)

root.mainloop()
