b=[]
cmp=[]
import random
from tkinter import *

sum=IntVar
#for i in range(0, len(cmp)):
    #print("cmp=", cmp[i])

def chose1():


    def a():
        cmp.append(1)

    def b():
        cmp.append(2)
    def c():
        cmp.append(3)
    def d():
        cmp.append(4)
    def e():
        cmp.append(5)

    def f():
        cmp.append(6)
    def g():
        cmp.append(7)
    def h():
        cmp.append(8)

    def i():
        cmp.append(9)

    def j():
        cmp.append(10)
    windo=Tk()
    wi.destroy()

    windo.geometry("500x500")
    windo.title("YOUR SCORE")

    button=Button(windo,text="Android",command=a).grid(row=0,column=3)

    button=Button(windo,text="Goat",command=b).grid(row=1,column=3)

    button=Button(windo,text="Teddy Bear",command=c).grid(row=2,column=3)

    button=Button(windo,text="Laptop",command=d).grid(row=3,column=3)

    button=Button(windo,text="Emoji",command=e).grid(row=4,column=3)

    button=Button(windo,text="Java",command=f).grid(row=5,column=3)

    button=Button(windo,text="QR code",command=g).grid(row=6,column=3)

    button=Button(windo,text="Frame",command=h).grid(row=7,column=3)

    button=Button(windo,text="Twitter logo",command=i).grid(row=8,column=3)

    button=Button(windo,text="Star",command=j).grid(row=9,column=3)

    button=Button(windo,text="submit",command=showdata).grid(row=5, column=8)

    windo.mainloop()




def showdata():
    new = Tk()
    new.geometry("500x500")
    arr=[]
    for i in range(0,len(cmp)):
        arr.append(cmp[i])
    for i in range(len(cmp),10):
        arr.append(0)

    ans=0
    '''for i in range(0,10):
        print("arr=",arr[i])
    for i in range(0,len(b)):
        print("b=",b[i])
    print("\n")'''

    for i in range(0,10):
        for j in range(0,10):
            if(b[i]==arr[j] and b[i]!=0):
                ans=ans+1
                break
    sum=ans
    answer_label = Label(new, text=sum)
    answer_label.grid(row=0, column=0)
    new.mainloop()


class my():
    def __init__(self,win):
        i = 0
        r = 0
        c = 0

        self.fram=Frame(win)
        a=[]
        lis=[]
        m=random.randint(5,7)
        for j in range(1,m):

            i = random.randint(1, 10)
            for k in range(0,len(lis)):
                if(lis[k]==i):
                    i=random.randint(1,10)
            lis.append(i)

            a.append(i)
            if (i == 1):
                self.photo1 = PhotoImage(file="11.png")
                self.label1 = Label(self.fram, image=self.photo1)
                self.label1.grid(row=r, column=c)

                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0
            if (i == 2):
                self.photo2 = PhotoImage(file="7.png")
                self.label2 = Label(self.fram, image=self.photo2)
                self.label2.grid(row=r, column=c)


                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0
            if (i == 3):
                self.photo3 = PhotoImage(file="10.png")
                self.label3 = Label(self.fram, image=self.photo3)
                self.label3.grid(row=r, column=c)


                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0
            if (i == 4):
                self.photo4 = PhotoImage(file="deepak2.png")
                self.label4 = Label(self.fram, image=self.photo4)
                self.label4.grid(row=r, column=c)

                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0
            if (i == 5):
                self.photo5 = PhotoImage(file="0001.png")
                self.label5 = Label(self.fram, image=self.photo5)
                self.label5.grid(row=r, column=c)


                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0
            if (i == 6):
                self.photo6 = PhotoImage(file="011.png")
                self.label6 = Label(self.fram, image=self.photo6)
                self.label6.grid(row=r, column=c)


                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0
            if (i == 7):
                self.photo7 = PhotoImage(file="b8.png")
                self.label7 = Label(self.fram, image=self.photo7)
                self.label7.grid(row=r, column=c)


                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0
            if (i == 8):
                self.photo8 = PhotoImage(file="1.png")
                self.label8 = Label(self.fram, image=self.photo8)
                self.label8.grid(row=r, column=c)


                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0
            if (i == 9):
                self.photo9 = PhotoImage(file="b9.png")
                self.label9 = Label(self.fram, image=self.photo9)
                self.label9.grid(row=r, column=c)

                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0
            if (i == 10):
                self.photo10 = PhotoImage(file="b10.png")
                self.label10 = Label(self.fram, image=self.photo10)
                self.label10.grid(row=r, column=c)


                c = c + 1
                if (c >= 2):
                    r = r + 1
                    c = 0


        self.fram.pack()
        self.button = Button(win, text="REFRESH", bg="yellow", fg="black", width="20", height="2",command=lol)
        self.button.pack(side=LEFT)
        self.button = Button(win, text="OK", bg="yellow", fg="black", width="20", height="2",command=chose1)
        self.button.pack(side=RIGHT)
        for i in range(0,len(a)):
            b.append(a[i])
        for i in range(len(a),10):
            b.append(0)
            #print("a=",a[i])
        win.mainloop()
        for i in range(0, len(b)):
           print(b[i], " ")
def lol():
    wi.destroy()
    new=Tk()

    rs=my(new)
    new.mainloop()

wi = Tk()
b=my(wi)
wi.mainloop()
