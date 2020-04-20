from tkinter import *
from tkinter import messagebox,ttk




flag=0
def show_sign_up():
    root.state('normal')
    top.state('withdrawn')

def show_log_in():
    global flag
    
    if flag==1:
        root.state("withdrawn")
        top.state("normal")
        flag=0

    else:
        root2.state('normal')
        top.state('withdrawn')


def submit():
    global flag
    file=open("sign_in_data.txt",'a+')
    if agree.get()=='Yes':
        email_id=E1.get()
        password=E2.get()
        name=E3.get()
        age=E4.get()
        address=E5.get()
        c_no=E6.get()
        gender=data.get()
        flag=1

        
        if email_id=='' or email_id.find('@')==-1:
            flag=0
            if email_id.find('@')==-1 and email_id!='':
                c=messagebox.showinfo("Error","Invalid Email Id")
                E1.delete(0,END)
                flag=0
            E1.config(bg='IndianRed')

        if password=='':
            E2.config(bg='IndianRed')
            flag=0

        if name=='' or type(name)==int:
            if type(name)==int and name!='':
                d=messagebox.showinfo("Error","Invalid Name")
                E3.delete(0,END)
                flag=0

            E3.config(bg='IndianRed')
            flag=0

        if age=='' or not age.isdigit() :
            if type(age)!=int and age!='':
                e=messagebox.showinfo("Error","Invalid Age")
                E4.delete(0,END)
                flag=0

            E4.config(bg='IndianRed')
            flag=0

        if c_no=='' or not c_no.isdigit():
            if type(c_no)!=int and c_no!='' and len(c_no) != 10:
                f=messagebox.showinfo("Error"," Invalid Contact No.")
                E6.delete(0,END)
                flag=0
            
            E6.config(bg='IndianRed')
            flag=0
        if len(c_no) != 10:
                f=messagebox.showinfo("Error"," Max Contact No. length should be 10")
                flag=0

        if address=='':
            E5.config(bg='IndianRed')
            flag=0

        if gender=='None':
            flag=0
            c1.config(bg='IndianRed')
            c2.config(bg='IndianRed')


        if E11.get()!=password:
            flag=0
            msg=messagebox.showinfo("Error","Password does not Match\nTry Again!!!")
            E11.delete(0,END)

        
            
        if flag==1:
            E1.delete(0,len(email_id))
            E1.config(bg='white')
            E2.delete(0,len(password))
            E2.config(bg='white')
            E3.delete(0,len(name))
            E3.config(bg='white')
            E4.delete(0,len(age))
            E4.config(bg='white')
            E5.delete(0,len(address))
            E5.config(bg='white')
            E6.delete(0,len(c_no))
            E6.config(bg='white')
            E11.delete(0,END)
            E11.config(bg='white')
            c1.deselect()
            c1.config(bg='white')
            c2.deselect()
            c2.config(bg='white')
            c3.deselect()
            c3.config(bg='white')
            msg=messagebox.showinfo("Sign Up",'SUBMIT SUCCESFULLY')
            show_log_in()
            file.write(name+'#'+age+'#'+address+'#'+c_no+'#'+email_id+'#'+password+'#'+gender+'\n')
            

    else:
        msg2=messagebox.showinfo("Sign Up","Do you Agree All terms and conditions ?")
        if msg2=='ok':
            c3.select()
    file.close()
    


root=Tk()
root.geometry("800x600+100+100")
root2=Tk()
root2.geometry("800x600+100+100")
root.title("SIGN UP")
root2.title("LOG IN")
root.state('withdrawn')
root2.state('withdrawn')
top=Toplevel(root)
top.geometry('800x600+100+100')
top.title("JK SECURE VAULT")
#f_top =Frame(top,width= 800,height =600,bg='darkslateblue',fg='powderblue').pack()
b1_top=Button(top,text="Sign UP",command=show_sign_up,bg='lavender',fg='black',width=20,height=3).pack(side=LEFT,expand=YES)
b1_top=Button(top,text="Log In",command=show_log_in,bg='lavender',fg='black',width=20,height=3).pack(side=LEFT,expand=YES)


###FRAME DESIGN OF SIGN UP PAGE

f10=Frame(root,height=20,bg='darkslateblue')
l10=Label(f10,text='SIGN  UP',width=20,height=3,padx=3,pady=3,fg='red',bg='yellow',font='broadway')
l10.pack(side=TOP)
f10.pack(side=TOP,expand=YES,fill=BOTH)


f3=Frame(root,bg='darkslateblue')
l3=Label(f3,text="Name",font='algerian',bg="powderblue",fg="black",width=10)
E3=Entry(f3,bd=10,relief=GROOVE,selectbackground='blue',selectforeground='yellow',width=90)
l3.pack(side=LEFT,padx=15,pady=5,expand=YES,fill=BOTH)
E3.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
f3.pack(side=TOP,expand=YES,fill=BOTH)

f4=Frame(root,bg='darkslateblue')
l4=Label(f4,text="Age",font='algerian',bg="powderblue",fg="black",width=10)
E4=Entry(f4,bd=10,relief=GROOVE,selectbackground='blue',selectforeground='yellow',width=90)
l4.pack(side=LEFT,padx=15,pady=5,expand=YES,fill=BOTH)
E4.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
f4.pack(side=TOP,expand=YES,fill=BOTH)

f5=Frame(root,bg='darkslateblue')
l5=Label(f5,text="Address",font='algerian',bg="powderblue",fg="black",width=10)
E5=Entry(f5,bd=10,relief=GROOVE,selectbackground='blue',selectforeground='yellow',width=90)
l5.pack(side=LEFT,padx=15,pady=5,expand=YES,fill=BOTH)
E5.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
f5.pack(side=TOP,expand=YES,fill=BOTH)

f6=Frame(root,bg='darkslateblue')
l6=Label(f6,text="Contact No.",font='algerian',bg="powderblue",fg="black",width=10)
E6=Entry(f6,bd=10,relief=GROOVE,selectbackground='blue',selectforeground='yellow',width=90)
l6.pack(side=LEFT,padx=15,pady=5,expand=YES,fill=BOTH)
E6.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
f6.pack(side=TOP,expand=YES,fill=BOTH)

f1=Frame(root,bg='darkslateblue')
l1=Label(f1,text="Email Id",font='algerian',bg="powderblue",fg="black",width=10)
E1=Entry(f1,bd=10,relief=GROOVE,selectbackground='blue',selectforeground='yellow',width=90)
l1.pack(side=LEFT,padx=15,pady=5,expand=YES,fill=BOTH)
E1.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
f1.pack(side=TOP,expand=YES,fill=BOTH)


f2=Frame(root,bg='darkslateblue')
l2=Label(f2,text="Password",font='algerian',bg="powderblue",fg="black",width=10)
E2=Entry(f2,bd=10,relief=GROOVE,selectbackground='blue',selectforeground='yellow',show="*",width=90)
l2.pack(side=LEFT,padx=15,pady=5,expand=YES,fill=BOTH)
E2.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
f2.pack(side=TOP,expand=YES,fill=BOTH)

f11=Frame(root,bg='darkslateblue')
l11=Label(f11,text=" Re-Type Pass",font='algerian',bg="powderblue",fg="black",width=10)
E11=Entry(f11,bd=10,relief=GROOVE,selectbackground='blue',selectforeground='yellow',show="*",width=90)
l11.pack(side=LEFT,padx=15,pady=5,expand=YES,fill=BOTH)
E11.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
f11.pack(side=TOP,expand=YES,fill=BOTH)

f7=Frame(root,bg='darkslateblue')
data=StringVar()
data.set('None')
l7=Label(f7,text="Gender",font='algerian',bg="powderblue",fg="black",width=10)
l7.pack(side=LEFT,padx=25,pady=5,fill=BOTH)
c1=Checkbutton(f7,text='Male',variable=data,onvalue='Male',offvalue='None')
c1.pack(side=LEFT,expand=YES,padx=5,pady=5)
c2=Checkbutton(f7,text='Female',variable=data,onvalue='Female',offvalue='None')
c2.pack(side=LEFT,expand=YES,padx=5,pady=5)
f7.pack(side=TOP,expand=YES,fill=BOTH)

f8=Frame(root,bg='darkslateblue')
agree=StringVar()
agree.set("No")
c3=Checkbutton(f8,text='I agree all the terms and conditions',variable=agree,onvalue='Yes',offvalue='No')
c3.pack(side=LEFT)
f8.pack(side=TOP)

f3=Frame(root,bg='darkslateblue')
b3=Button(f3,text="Submit",command=submit,bg='lavender',fg='black',width=20,height=3)
b3.pack(side=TOP)
f3.pack(side=TOP,expand=YES,fill=BOTH)



###FRAME DESIGN OF LOG IN PAGE


F1=Frame(root2,height=20,bg='darkslateblue')
L1=Label(F1,text='LOG IN',width=20,height=3,padx=3,pady=3,fg='red',bg='yellow',font='broadway')
L1.pack(side=TOP)
F1.pack(side=TOP,expand=YES,fill=BOTH)



F2=Frame(root2,bg="darkslateblue")
L2=Label(F2,text="Username",font='algerian',bg="powderblue",fg="black",width=10)
e2=Entry(F2,bd=10,relief=GROOVE,selectbackground='blue',selectforeground='yellow',width=90)
L2.pack(side=LEFT,padx=15,pady=5,expand=YES,fill=BOTH)
e2.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
F2.pack(side=TOP,expand=YES,fill=BOTH)

F3=Frame(root2,bg="darkslateblue")
L3=Label(F3,text="Password",font='algerian',bg="powderblue",fg="black",width=10)
e3=Entry(F3,bd=10,relief=GROOVE,show="*",selectbackground='blue',selectforeground='yellow',width=90)
L3.pack(side=LEFT,padx=15,pady=5,expand=YES,fill=BOTH)
e3.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
F3.pack(side=TOP,expand=YES,fill=BOTH)

F4=Frame(root2,bg='darkslateblue')
B1=Button(F4,text="Submit",bg='lavender',fg='black',width=20,height=3)
B1.pack(side=TOP)
F4.pack(side=TOP,expand=YES,fill=BOTH)

root.mainloop()
root2.mainloop()
