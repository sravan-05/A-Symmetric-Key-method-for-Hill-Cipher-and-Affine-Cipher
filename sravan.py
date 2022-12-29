from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import random
 
def raise_frame(f):
    f.tkraise()
 
def finish():
    r.destroy()
    
def fr1():
    raise_frame(Fr1)
    clearE1()
    clearE2()
    clearD1()
    clearD2()
def fr2():
    raise_frame(Fr2)
    clearE1()
    clearD1()
def fr3():
    raise_frame(Fr3)
    clearE1()
    clearE2()
def fr4():
    raise_frame(Fr4)
def fr5():
    raise_frame(Fr5)
    clearD1()
    clearD2()
def fr6():
    raise_frame(Fr6) 
def fr7():
    raise_frame(Fr7)
def fr8():
    raise_frame(Fr8)
def fr9():
    raise_frame(Fr9)
def fr10():
    raise_frame(Fr10)    


#------------------------------------------------Encryption Page-1 coding ---------------------------------------------------------
tik=0
def fun1():
    global t2,codes,tik
    t1=e1.get()
    if(tik==0 and len(t1)!=0):
        tik=1
        codes=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
                   'R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h',
                   'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                   '0','1','2','3','4','5','6','7','8','9','_','@','!']
                    
            
        t2=t1
        t3=''
        if(len(t1)%2==1):
            t1+='@'
        for i in range(len(t1)):
            t3+=str(codes.index(t1[i]))+' '
        e1.configure(state='disabled')
        x1.set(t3)
    else:
        messagebox.showinfo('Message Box','Please enter plain text  ')    
def fun2():
    global k1,k2,k3,sk3,kk3,tik
    if(tik==1):
        tik=2
        k1=7
        k2=2
        k3=[3,7,5,12]
        kk3='3 7 5 12' 
        sk3='3  7\n 5  12'
        
        x2.set(str(k1))
        x3.set(str(k2))
        x4.set(str(sk3))
    else:
        messagebox.showinfo('Message Box','Please enter previous button ')
def fun3():
    global t2,k1,k2,codes,t4,t5,tik
    if(tik==2):
        tik=3
        t3=''
        t4=''
        t5=''
        for i in range(len(t2)):
            t3+=str((codes.index(t2[i]))*k1)+' '
            t4+=str(((codes.index(t2[i]))*k1)+k2)+' '
            t5+=str((((codes.index(t2[i]))*k1)+k2) % 27)+' '
        x5.set(t3)
    else:
        messagebox.showinfo('Message Box','Please enter previous button ')
def fun4():
    global t4,tik
    if(tik==3):
        tik=4
        x6.set(t4)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun5():
    global t5,tik
    if(tik==4):
        tik=5
        x7.set(t5)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
#------------------------------------------------Encryption Page-2 coding ---------------------------------------------------------    
def fun6():
    global t5,sk3,p,k3,tik
    if(tik==5):
        tik=6
        p=t5.split(' ')
        p=p[:-1]
        t6=''
        for i in range(len(p)):
            t6+=p[i]+' '
            if(i%2==1):
                t6+='\n'            
        x8.set(t6)
        x9.set(sk3)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun7():
    global p,k3,MOD,CP,tik
    if(tik==6):
        tik=7
        rs=int(len(p)/2)
        M1 = [[0 for x in range(2)] for y in range(rs)]  
        k=0
        for i in range(rs):
            for j in range(2):
                M1[i][j] =int(p[k])
                k+=1
        A=''
        for i in range(rs):
            for j in range(2):
                A+=str(M1[i][j])+" "
            A+='\n'
        x10.set(A)

        M2 = [[0 for x in range(2)] for y in range(2)]  
        k=0
        for i in range(2):
            for j in range(2):
                M2[i][j] =int(k3[k])
                k+=1
        B=''
        for i in range(2):
            for j in range(2):
                B+=str(M2[i][j])+" "
            B+='\n'
        x10.set(B)

        M3 = [[0 for x in range(2)] for y in range(rs)]  
        M4 = [[0 for x in range(2)] for y in range(rs)]  
        k=0
        for i in range(rs):
            for j in range(2):
                M3[i][j]=0
                M4[i][j]=0
                for q in range(2):
                    M3[i][j] += M1[i][q] * M2[q][j]
                M4[i][j] = M3[i][j] % 27
                
        B=''
        MOD=''
        CP=''
        for i in range(rs):
            for j in range(2):
                B+=str(M3[i][j])+" "
                MOD+=str(M4[i][j])+" "
                CP+=str(chr(M4[i][j]+64))
            B+='\n'
            MOD+='\n'
        x10.set(B)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun8():
    global MOD,tik
    if(tik==7):
        tik=8
        x11.set(MOD)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun9():
    global CP,tik
    if(tik==8):
        tik=9
        x12.set(CP)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def SaveKeys():
    global k1,k2,kk3,tik
    if(tik==9):
        tik=10
        keys=str(k1)+'\n'+str(k2)+'\n'+str(kk3)
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        f.write(keys)
        f.close()
        messagebox.showinfo('Message Box','Keys are saved successfully')
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def Save():
    global CP,tik
    if(tik==10):
        tik=0
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        f.write(CP)
        f.close()
        messagebox.showinfo('Message Box','Cipher text is saved successfully')
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
#------------------------------------------------Decryption Page-1 coding ---------------------------------------------------------
kik=0
def OpenCode():
    global CP,kik
    if(kik==0):
        kik=1
        file=askopenfile(mode='r',filetypes=[('All files','*.txt')])
        if file is not None:
            CP=file.read()        
            x13.set(CP)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')      
def fun10():
    global CP,cp1,kik
    if(kik==1):
        kik=2
        cp1=''
        for i in range(len(CP)):
            cp1+=str(ord(CP[i])-64)+' '
        x14.set(cp1)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')      
def OpenKeys():
    global Key,k1,k2,kik
    if(kik==2):
        kik=3
        file=askopenfile(mode='r',filetypes=[('All files','*.txt')])
        if file is not None:
            Key=file.read()
            Keys=Key.split('\n')
            k1=Keys[0]
            k2=Keys[1]
            k3=''
            kk3=Keys[2].split(' ')
            
            for i in range(len(kk3)):
                k3+=kk3[i]+' '
                if(i%2==1):
                    k3+='\n'
            k3=k3[:-1]        
            x15.set(k1)
            x16.set(k2)
            x17.set(k3)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')      
def fun11():
    global k1,kik
    if(kik==3):
        kik=4
        k1=4
        x18.set(str(k1))
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun12():
    global IK3,kik
    if(kik==4):
        kik=5
        IK3='12 -7\n-5 3' 
        x19.set(IK3)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
#------------------------------------------------Decryption Page-2 coding ---------------------------------------------------------
def fun13():
    global cp1,IK3,kik
    if(kik==5):
        kik=6
        cp1=cp1.split(' ')
        cp2=''
        for i in range(len(cp1)):
            cp2+=cp1[i]+' '
            if(i%2==1):
                cp2+='\n'
        x20.set(cp2)
        x21.set(IK3)
        IK3=[12,-7,-5,3]
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun14():
    global p,k3,MOD,CP,cp1,IK3,kik
    if(kik==6):
        kik=7
        rs=int(len(cp1)/2)
        M1 = [[0 for x in range(2)] for y in range(rs)]  
        k=0
        for i in range(rs):
            for j in range(2):
                M1[i][j] =int(cp1[k])
                k+=1

        M2 = [[0 for x in range(2)] for y in range(2)]  
        k=0
        for i in range(2):
            for j in range(2):
                M2[i][j] =int(IK3[k])
                k+=1

        M3 = [[0 for x in range(2)] for y in range(rs)]  
        M4 = [[0 for x in range(2)] for y in range(rs)]  
        k=0
        for i in range(rs):
            for j in range(2):
                M3[i][j]=0
                M4[i][j]=0
                for q in range(2):
                    M3[i][j] += M1[i][q] * M2[q][j]
                M4[i][j] = M3[i][j] % 27
                
        B=''
        MOD=''
        CP=''
        
        for i in range(rs):
            for j in range(2):
                B+=str(M3[i][j])+" "
                MOD+=str(M4[i][j])+" "
                CP+=str(M4[i][j])+" "
            B+='\n'
            MOD+='\n'
        x22.set(B)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun15():
    global MOD,kik
    if(kik==7):
        kik=8
        x23.set(MOD)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')                     
#------------------------------------------------Decryption Page-3 coding ---------------------------------------------------------
    
def fun16():
    global k1,k2,kik
    if(kik==8):
        kik=9
        x24.set(str(k1))
        x25.set(str(k2))
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun17():
    global CP,k2,cp2,cp3,cp4,kik
    if(kik==9):
        kik=10
        CP=CP.split(' ')
        CP=CP[:-1]
        cp1=''
        cp2=''
        cp3=''
        cp4=''
        for i in range(len(CP)):
            y=int(CP[i])-int(k2)
            cp1+=str(y)+' '
            y=y*int(k1)
            cp2+=str(y)+' '
            x=y%27
            cp3+=str(x)+' '
            cp4+=str(chr(x+64))+' '

        x26.set(cp1)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun18():
    global cp2,kik
    if(kik==10):
        kik=11
        x27.set(cp2)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun19():
    global cp3,kik
    if(kik==11):
        kik=12
        x28.set(cp3)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')
def fun20():
    global cp4,kik
    if(kik==12):
        kik=13
        cp4=cp4.replace('@','')
        x29.set(cp4)
    else:
        messagebox.showinfo('Message Box','Please enter previous button')

#------------------------------------------------XXXXXX ---------------------------------------------------------
    

r = Tk()
Fr0 = Frame(r)
Fr1 = Frame(r)
Fr2 = Frame(r)
Fr3 = Frame(r)
Fr4 = Frame(r)
Fr5 = Frame(r)
Fr6 = Frame(r)
Fr7 = Frame(r)
Fr8 = Frame(r)
Fr9 = Frame(r)
Fr10 = Frame(r)

Fr0.place(x =0,y = 0,height=1000, width=1500)
Fr1.place(x = 0,y = 0,height=1000, width=1500)
Fr2.place(x = 0,y =0,height=1000, width=1500)
Fr3.place(x = 0,y = 0,height=1000, width=1500)
Fr4.place(x = 0,y = 0,height=1000, width=1500)
Fr5.place(x = 0,y = 0,height=1000, width=1500)
Fr6.place(x = 0,y = 0,height=1000, width=1500)
Fr7.place(x = 0,y = 0,height=1000, width=1500)
Fr8.place(x = 0,y = 0,height=1000, width=1500)
Fr9.place(x = 0,y = 0,height=1000, width=1500)
Fr10.place(x = 0,y = 0,height=1000, width=1500)


Fr1.config(bg='white'),Fr2.config(bg='white'),Fr3.config(bg='white'),Fr4.config(bg='white'),
Fr5.config(bg='white'),Fr6.config(bg='white'),Fr7.config(bg='white'),Fr8.config(bg='white'),
Fr9.config(bg='white'), Fr10.config(bg='white')

def clearE1():
    e1.configure(state='normal')
    e1.delete(0,END)
    
    x01.set('')
    x1.set('')
    x2.set('')
    x3.set('')
    x4.set('')
    
def clearE2():
    x5.set('')
    x6.set('')
    x7.set('')
    x8.set('')
    x9.set('')
    x10.set('')
    x11.set('')
    x12.set('')
    
def clearD1():
    xoc.set('')
    x13.set('')
    x14.set('')
    x15.set('')
    x16.set('')
    x17.set('')
    x18.set('')
    x19.set('')
    
def clearD2():
    xok.set('')
    x20.set('')
    x21.set('')
    x22.set('')
    x23.set('')
    
def clearD3():
    x24.set('')
    x25.set('')
    x26.set('')
    x27.set('')
    x28.set('')
    x29.set('')    

x01=StringVar()
x1=StringVar()
x2=StringVar()
x3=StringVar()
x4=StringVar()
x5=StringVar()
x6=StringVar()
x7=StringVar()
x8=StringVar()
x9=StringVar()
x10=StringVar()
x11=StringVar()
x12=StringVar()
x13=StringVar()
x14=StringVar()
x15=StringVar()
x16=StringVar()
x17=StringVar()
x18=StringVar()
x19=StringVar()
x20=StringVar()
x21=StringVar()
x22=StringVar()
x23=StringVar()
x24=StringVar()
x25=StringVar()
x26=StringVar()
x27=StringVar()
x28=StringVar()
x29=StringVar()
xoc=StringVar()
xok=StringVar()


#HeadingPage


#------------------StartPage Fr1---------------------------------------------------------------------------
ph01=ImageTk.PhotoImage(Image.open("9.jpg "))
lab1 = Label(Fr1,image=ph01).place(x = 0, y = 0)



lab2 = Label(Fr1, justify="left",text = '''A SYMMETRIC KEY METHOD FOR HILL CIPHER AND AFFINE CIPHER''',
                 fg="black",bg='white', font = "TimesNewRoman 27 bold",height=1).place(x = 150,y=30)

ph010=ImageTk.PhotoImage(Image.open("8.jpg"))
lab1=Label(Fr1,image=ph010,height=450,width=1189).place(x=150,y=100)
lab4 = Label(Fr1, text = """UNDER THE GUIDENCE
Mrs. V. LAKSHMI
Assistant Professor""",
                 font = "TimesNewRoman 12 bold",bg='white',height=5,width=30).place(x =915,y=650)

lab5 = Label(Fr1,justify="center", text = """
Designed By
P.SRAVAN KUMAR
M.C.A 4th SEM
20131F0043
""",
                 fg = "black",
                 
		 font = "TimesNewRoman 12 bold",bg='white',height=5,width=30).place(x = 300,y=650)

but1 = Button(Fr1, text = "Proceed",
            fg="black",bg="white",bd=7, font = "TimesNewRoman 12 bold",height=1,width=15, command = fr10).place(x = 550, y = 580)
but2 = Button(Fr1, text = "Close",
            fg="black",bg="white",bd=7,font = "TimesNewRoman 12 bold",height=1,width=15,command=finish).place(x = 800, y = 580)


#----------------Abstract Page Fr-10 -------------------------------------------------------------------------

ph029=ImageTk.PhotoImage(Image.open("9.JPG "))
lab1 = Label(Fr10,image=ph029).place(x = 0, y = 0)


lab2 = Label(Fr10, justify="left",text = "A Symmetric Key Method for Hill cipher and Affine Cipher",
                 fg="black",bg='white', font = "TimesNewRoman 25 bold",height=1).place(x = 320,y=100)
l3= Label(Fr10,text="""ABSTRACT

In general, confidentiality is the same as privacy because it focuses on keeping private information

away from unauthorized persons. There are many methods to provide secrecy to the normal text but

the system uses high secret key generation methods for transfer of data in the highly secured manner.

Sometimes, it is required to send or exchange private information in non-secure channel in that

channel anyone can access the data easily. Where use of secure channel is bit costly. So to full fill the

 basic requirement in any channel, one can use many techniques such as Stenography, Virtual Private
 
 Networks etc. The other common method that ensures confidentiality is cryptography, in which data
 
encryption is performed to generate ciphers. Here the Symmetric key cryptographic system uses the

property of both Affine Cipher and Hill cipher for the better security of data . Affine cipher uses the

property of additive and multiplicative for encryption and decryption whereas hill cipher uses the

property of multiplication of matrices. 
""", justify="left",fg="black", font = "TimesNewRoman 12 bold",bg='white',height=26).place(x = 380, y =175)


b8 = Button(Fr10, text = "Prev",fg="black",bg="white",bd=7, font = "TimesNewRoman 10 bold",width=6,command = fr1).place(x = 450, y = 725)
b7 = Button(Fr10, text = "Next",fg="black",bg="white",bd=7, font = "TimesNewRoman 10 bold",width=6,command=fr2).place(x = 1045, y = 725)

#----------------Menu Page Fr-2 -------------------------------------------------------------------------

ph02=ImageTk.PhotoImage(Image.open("9.JPG "))
lab2 = Label(Fr2,image=ph02).place(x = 0, y = 0)


lab2 = Label(Fr2, justify="left",text = "A Symmetric key Method for Hill Cipher and Affine Cipher",
                 fg="black",bg='white', font = "TimesNewRoman 25 bold",height=1).place(x = 280,y=125)

ph020=ImageTk.PhotoImage(Image.open("1.png"))
lab2=Label(Fr2,image=ph020,height=250,width=500).place(x=450,y=250)

but3 = Button(Fr2, text = "Back",
            fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fr10).place(x = 300, y = 390)
but4 = Button(Fr2, text = "Encryption",
            fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fr3).place(x = 300, y = 300)
but5 = Button(Fr2, text = "Decryption",
            fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fr5).place(x = 990, y = 300)
but6 = Button(Fr2, text = "Next",
            fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fr8).place(x = 990, y = 390)

but2 = Button(Fr2, text = "Home",
            fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fr1).place(x = 550, y = 550)
but7 = Button(Fr2, text = "Close",
            fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = finish).place(x = 750, y = 550)


#--------------------Encryption Page-1  ----Fr-3---------------------------------------------------------------------------------

ph03=ImageTk.PhotoImage(Image.open("9.JPG "))
lab3 = Label(Fr3,image=ph03).place(x = 0, y = 0)


lab2 = Label(Fr3, justify="left",text = "A Symmetric key Method for Hill Cipher and Affine Cipher",
                 fg="black",bg='white', font = "TimesNewRoman 30 bold",height=1).place(x = 199,y=125)

l1 = Label(Fr3, text = "Encryption",fg="black",font = "TimesNewRoman 16 bold",bg='white',height=1,width=10).place(x = 150,y=200)

l1 = Label(Fr3, text = "Plain Text",fg="black", bd=5,font = "TimesNewRoman 14 bold",bg='white',height=1,width=14).place(x = 150, y =250)
e1= Entry(Fr3, fg="black",textvariable=x01, bg='white',font = "TimesNewRoman 18 bold",width=80)
e1.place(x = 350,y=250)

b1 = Button(Fr3, text = "Convert to Digits",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun1).place(x = 150, y =300)
l3= Label(Fr3, textvariable=x1,fg="black",bg="white", bd=2,font = "TimesNewRoman 16 bold",width=80).place(x = 350,y=300)

b2 = Button(Fr3, text = "Select Random Keys",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun2).place(x =150, y =350)
l3= Label(Fr3,text="K1",fg="black",bg="white",font = "TimesNewRoman 16 bold").place(x = 370,y=360)
l3= Label(Fr3, textvariable=x2,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=3).place(x = 420,y=360)

l3= Label(Fr3,text="K2",fg="black",bg="white",font = "TimesNewRoman 16 bold").place(x = 470,y=360)
l3= Label(Fr3, textvariable=x3,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=3).place(x = 520,y=360)

l3= Label(Fr3, text="K3",fg="black",bg="white", font = "TimesNewRoman 16 bold").place(x = 600,y=360)
l3= Label(Fr3, textvariable=x4,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=8,height=2).place(x = 650,y=360)
 
b2 = Button(Fr3, text = "P*K1",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun3).place(x =150, y =420)
l3= Label(Fr3, textvariable=x5,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=80,height=1).place(x = 350,y=420)

b1 = Button(Fr3, text = "(P*K1)+K2",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun4).place(x = 150, y =470)
l3= Label(Fr3, textvariable=x6,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=80).place(x = 350,y=470)

b2 = Button(Fr3, text = "(P*K1)+K2 MOD 27",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun5).place(x =150, y =520)
l3= Label(Fr3,textvariable=x7,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=80).place(x = 350,y=520)

b7 = Button(Fr3, text = "Home",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",height=1,width=10,command=fr1).place(x = 650, y = 590)
b8 = Button(Fr3, text = "Clear",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = clearE1).place(x = 930, y = 590)
b8 = Button(Fr3, text = "Prev",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = fr2).place(x = 150, y = 590)
b7 = Button(Fr3, text = "Next",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command=fr4).place(x = 1330, y = 590)

#--------------------Encryption Page - 2  ----Fr-4---------------------------------------------------------------------------------

ph04=ImageTk.PhotoImage(Image.open("9.JPG "))
lab4 = Label(Fr4,image=ph04).place(x = 0, y = 0)

lab2 = Label(Fr4, justify="left",text = "A Symmetric key Method for Hill Cipher and Affine Cipher",
                 fg="black",bg='white', font = "TimesNewRoman 30 bold",height=1).place(x = 199,y=125)

l1 = Label(Fr4, text = "Encryption",fg="black",font = "TimesNewRoman 16 bold",bg='white',height=1,width=10).place(x = 150,y=200)

b2 = Button(Fr4, text = "P * K3 ",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fun6).place(x =150, y =255)
l3= Label(Fr4, textvariable=x8,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=8,height=5).place(x = 400,y=230)
l3= Label(Fr4, text='*',fg="black",bg="white", font = "TimesNewRoman 20 bold").place(x = 550,y=255)
l3= Label(Fr4, textvariable=x9,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=8,height=3).place(x = 600,y=230)

b4 = Button(Fr4, text = "Calculate",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fun7).place(x =150,y=370)
l3= Label(Fr4, textvariable=x10,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=10,height=5).place(x = 400,y=370)

b4 = Button(Fr4, text = "MOD 27",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fun8).place(x =580,y=395)
l3= Label(Fr4, textvariable=x11,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=8,height=5).place(x = 750,y=370)

b5 = Button(Fr4, text = "Cipher Text",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fun9).place(x =150,y=530)
l3= Label(Fr4, textvariable=x12,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=68,height=1).place(x = 400,y=530)

b5 = Button(Fr4, text = "Save Keys",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",height=1,width=10,command=SaveKeys).place(x = 350, y = 600)
b7 = Button(Fr4, text = "Home",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",height=1,width=10,command=fr1).place(x = 550, y = 600)
b6 = Button(Fr4, text = "Save Cipher Text",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",height=1,width=15,command=Save).place(x = 750, y = 600)

b8 = Button(Fr4, text = "Clear",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = clearE2).place(x = 1050, y = 600)
b8 = Button(Fr4, text = "Prev",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = fr3).place(x = 150, y = 600)
b7 = Button(Fr4, text = "Next",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command=fr5).place(x = 1200, y = 600)

#-------------------------Decryption Page-1 --------Fr-5--------------------------------------------------------------------------------------------------------

ph06=ImageTk.PhotoImage(Image.open("9.JPG "))
lab6 = Label(Fr5,image=ph06).place(x = 0, y = 0)


lab2 = Label(Fr5, justify="left",text = "A Symmetric key Method for Hill Cipher and Affine Cipher",
                 fg="black",bg='white', font = "TimesNewRoman 30 bold",height=1).place(x = 199,y=125)

l1 = Label(Fr5, text = "Decryption",fg="black",font = "TimesNewRoman 16 bold",bg='white',height=1,width=12).place(x = 150,y=200)

b1 = Button(Fr5, text = "Browse Cipher Text",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = OpenCode).place(x = 150, y =250)
l3= Label(Fr5, textvariable=x13,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=65).place(x = 400,y=250)

b1 = Button(Fr5, text = "Convert to Digits",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun10).place(x = 150, y =300)
l3= Label(Fr5, textvariable=x14,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=65).place(x = 400,y=300)

b2 = Button(Fr5, text = "Browse Keys",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = OpenKeys).place(x =150, y =350)
l3= Label(Fr5,text="K1",fg="black",bg="white", font = "TimesNewRoman 16 bold").place(x = 400,y=350)
l3= Label(Fr5, textvariable=x15,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=3).place(x = 450,y=350)

l3= Label(Fr5,text="K2",fg="black",bg="white", font = "TimesNewRoman 16 bold").place(x = 510,y=350)
l3= Label(Fr5, textvariable=x16,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=3).place(x = 560,y=350)

l3= Label(Fr5, text="K3",fg="black",bg="white", font = "TimesNewRoman 16 bold").place(x = 610,y=350)
l3= Label(Fr5, textvariable=x17,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=8,height=2).place(x = 660,y=350)

b2 = Button(Fr5, text = "Mul.Inv of K2",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun11).place(x =150, y =420)
l3= Label(Fr5, text="K2'",fg="black",bg="white", font = "TimesNewRoman 16 bold").place(x = 400,y=420)
l3= Label(Fr5, textvariable=x18,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=3).place(x = 450,y=420)
l3= Label(Fr5, text="Multiplicative inverse of modulo 27",fg="black",bg="white", font = "TimesNewRoman 16 bold").place(x = 510,y=420)

b2 = Button(Fr5, text = "Inverse of K3",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun12).place(x =150, y =470)
l3= Label(Fr5, text="IK3",fg="black",bg="white", font = "TimesNewRoman 16 bold").place(x = 400,y=470)
l3= Label(Fr5, textvariable=x19,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=8,height=2).place(x = 450,y=470)

b7 = Button(Fr5, text = "Home",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",height=1,width=10,command=fr1).place(x = 650, y = 580)
b8 = Button(Fr5, text = "Clear",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = clearD1).place(x = 950, y = 580)
b8 = Button(Fr5, text = "Prev",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = fr4).place(x = 150, y = 580)
b7 = Button(Fr5, text = "Next",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command=fr6).place(x = 1250, y = 580)

#-------------------------Decryption Page-2 --------Fr-6--------------------------------------------------------------------------------------------------------

ph07=ImageTk.PhotoImage(Image.open("9.JPG "))
lab7 = Label(Fr6,image=ph07).place(x = 0, y = 0)


lab2 = Label(Fr6, justify="left",text = "A Symmetric key Method for Hill Cipher and Affine Cipher",
                 fg="black",bg='white', font = "TimesNewRoman 30 bold",height=1).place(x = 199,y=125)

l1 = Label(Fr6, text = "Decryption",fg="black",font = "TimesNewRoman 16 bold",bg='white',height=1,width=12).place(x = 150,y=200)

b2 = Button(Fr6, text = "P * IK3",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fun13).place(x =150, y =250)
l3= Label(Fr6, textvariable=x20,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=10,height=7).place(x = 400,y=230)
l3= Label(Fr6, text='*',fg="black",bg="white", font = "TimesNewRoman 20 bold").place(x = 560,y=260)
l3= Label(Fr6, textvariable=x21,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=8,height=3).place(x = 610,y=230)

b4 = Button(Fr6, text = "Calculate",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fun14).place(x =150,y=450)
l3= Label(Fr6, textvariable=x22,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=10,height=7).place(x = 400,y=410)

b4 = Button(Fr6, text = "MOD 27",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=10,command = fun15).place(x =600,y=440)
l3= Label(Fr6, textvariable=x23,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=10,height=7).place(x = 750,y=410)

b7 = Button(Fr6, text = "Home",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",height=1,width=10,command=fr1).place(x = 650, y = 650)
b8 = Button(Fr6, text = "Clear",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = clearD2).place(x = 930, y = 650)
b8 = Button(Fr6, text = "Prev",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = fr5).place(x = 150, y = 650)
b7 = Button(Fr6, text = "Next",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command=fr7).place(x = 1150, y = 650)

#-------------------------Decryption Page-3 --------Fr-7--------------------------------------------------------------------------------------------------------

ph08=ImageTk.PhotoImage(Image.open("9.JPG "))
lab8 = Label(Fr7,image=ph08).place(x = 0, y = 0)


lab2 = Label(Fr7, justify="left",text = "A Symmetric key Method for Hill Cipher and Affine Cipher",
                 fg="black",bg='white', font = "TimesNewRoman 30 bold",height=1).place(x = 199,y=125)

l1 = Label(Fr7, text = "Decryption",fg="black",font = "TimesNewRoman 16 bold",bg='white',height=1,width=12).place(x = 150,y=200)

b2 = Button(Fr7, text = "Select Random Keys",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun16).place(x =150, y =250)
l3= Label(Fr7,text="K1",fg="black",bg="white", font = "TimesNewRoman 16 bold").place(x = 400,y=250)
l3= Label(Fr7, textvariable=x24,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=3).place(x = 450,y=250)

l3= Label(Fr7,text="K2",fg="black",bg="white", font = "TimesNewRoman 16 bold").place(x = 570,y=250)
l3= Label(Fr7, textvariable=x25,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=3).place(x = 620,y=250)

b2 = Button(Fr7, text = "P-K2",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun17).place(x =150, y =320)
l3= Label(Fr7, textvariable=x26,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=65,height=1).place(x = 400,y=320)

b1 = Button(Fr7, text = "(P-K2)*K1",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun18).place(x = 150, y =390)
l3= Label(Fr7, textvariable=x27,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=65).place(x = 400,y=390)

b2 = Button(Fr7, text = "(P-K2)*K1 MOD 27",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun19).place(x =150, y =440)
l3= Label(Fr7,textvariable=x28,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=65).place(x = 400,y=440)

b2 = Button(Fr7, text = "Plain Text ",fg="black",bg="white",bd=5, font = "TimesNewRoman 12 bold",height=1,width=16,command = fun20).place(x =150, y =490)
l3= Label(Fr7,textvariable=x29,fg="black",bg="white", font = "TimesNewRoman 16 bold",width=65).place(x = 400,y=490)

b7 = Button(Fr7, text = "Home",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",height=1,width=10,command=fr1).place(x = 650, y = 600)
b8 = Button(Fr7, text = "Clear",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = clearD3).place(x = 930, y = 600)
b8 = Button(Fr7, text = "Prev",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = fr6).place(x = 150, y = 600)
b7 = Button(Fr7, text = "Next",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command=fr8).place(x = 1250, y = 600)

#------------------------Conclusion-----Fr-8--------------------
ph09=ImageTk.PhotoImage(Image.open("9.JPG "))
lab= Label(Fr8,image=ph09).place(x = 0, y = 0)

lab2 = Label(Fr8, justify="left",text = "A Symmetric key Method for Hill Cipher and Affine Cipher",
                 fg="black",bg='white', font = "TimesNewRoman 27 bold",height=1).place(x = 200,y=125)

l5= Label(Fr8,text="""Conclusion

The proposed symmetric cryptography system with the combination of Affine cipher and Hill cipher technique

is able to provide better security. The matrix property of the hill cipher technique provides the required

robustness for the system. It is simple to understand and it is of average complexity. It can be easily

implemented in various platforms which leads to faster conversion of text. The generation of the shared

symmetric key will serve the purpose of the session key in an e-mail application having PGP in place.

It can be used for encryption and decryption purposes in different fields such as chat systems, file

transfer systems, etc. that uses sessions. The key will serve the purpose of a shared symmetric session key. 

 """, justify="left",fg="black", font = "TimesNewRoman 12 bold",bg='white').place(x = 250, y =220)


b8 = Button(Fr8, text = "Prev",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command = fr7).place(x = 280, y = 590)
b7 = Button(Fr8, text = "Next",fg="black",bg="white",bd=5, font = "TimesNewRoman 10 bold",width=6,command=fr9).place(x = 995, y = 590)

#-----------------------Thank U------Fr-9--------------------

ph10=ImageTk.PhotoImage(Image.open("9.JPG "))
lab10 = Label(Fr9,image=ph10).place(x = 0, y = 0)

lab2 = Label(Fr9, justify="left",text = "A Symmetric key Method for Hill Cipher and Affine Cipher",
                 fg="black",bg='white', font = "TimesNewRoman 27 bold",height=1).place(x = 220,y=125)

ph030=ImageTk.PhotoImage(Image.open("10.jpg"))
lab10=Label(Fr9,image=ph030,height=350,width=500).place(x=450,y=250)

b9 = Button(Fr9, text = "Home",fg="black",bg="white",bd=5, font = "TimesNewRoman 14 bold",height=1,width=9,command=fr1).place(x = 390, y = 650)
b10 = Button(Fr9, text = "Close",fg="black",bg="white",bd=5, font = "TimesNewRoman 14 bold",height=1,width=9,command = finish).place(x = 890, y = 650)
#------------------------------------------------------------------------

raise_frame(Fr1)
r.geometry("1920x1080")
r.title("A Symmetric key Method for Hill Cipher and Affine Cipher")
r.mainloop()



