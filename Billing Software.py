from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Billing Software...")

text_Input = StringVar()
operator = ""

head=Frame(root,width=1600,height=100,relief=SUNKEN)
head.pack()
header=Label(head, text="Eat Repeat....", font=('Bodoni MT Black',30,'bold'))
header.place(x=615, y=20)


f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=300, height=700,bg="black", relief=SUNKEN)
f2.pack(side=RIGHT)





def btnclick(numbers):
    global operator
    operator =operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(f2,font=('arail', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="white", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="7", bg="black", command=lambda:

btnclick(7))
btn7.grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="8", bg="black", command=lambda:

btnclick(8))
btn8.grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="9", bg="black", command=lambda:

btnclick(9))
btn9.grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="+", bg="black", command=lambda: btnclick("+"))
Addition.grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="4", bg="black", command=lambda: btnclick(4))
btn4.grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="5", bg="black", command=lambda: btnclick(5))
btn5.grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="6", bg="black", command=lambda: btnclick(6))
btn6.grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="-", bg="black", command=lambda: btnclick("-"))
Subtraction.grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="1", bg="black", command=lambda: btnclick(1))
btn1.grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="2", bg="black", command=lambda:

btnclick(2))
btn2.grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="3", bg="black", command=lambda:
btnclick(3))
btn3.grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="*", bg="black", command=lambda: btnclick("*"))
Multiply.grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="0", bg="black", command=lambda: btnclick(0))
btn0.grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="C", bg="black", command=btnClearDisplay)
btnClear.grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="=", bg="black", command=btnEqualsInput)
btnEquals.grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16, fg="white", font=('arail',20,'bold'),text="/", bg="black", command=lambda: btnclick("/"))
Division.grid(row=5,column=3) 


#=========================================================
#                  		BILL CALCULATIONS
#=========================================================

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Noodle.get()==""):
        CoNoodle=0
    else:
        CoNoodle=float(Noodle.get())
   
    if (ChocolateShake.get()==""):
        CoChocolateShake=0
    else:
        CoChocolateShake=float(ChocolateShake.get())

    if (IceCream.get()==""):
        CoIceCream=0
    else:
        CoIceCream=float(IceCream.get())
    if (Pulav.get()==""):
        CoPulav=0
    else:
        CoPulav=float(Pulav.get())
        
    if (Tea.get()==""):
        CoTea=0
    else:
        CoTea=float(Tea.get())
     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())
                   
    CostofNoodle = CoNoodle * 25
    CostofDrinks= CoD * 20
    CostofChocolateShake = CoChocolateShake* 25
    CostofIceCream = CoIceCream * 30
    CostPulav = CoPulav* 50
    CostTea = CoTea * 5

    Central_GST= (((CostofNoodle+CostofDrinks+CostofChocolateShake+CostofIceCream+CostPulav+CostTea)* 2.5)/100)

    State_GST =(((CostofNoodle+CostofDrinks+CostofChocolateShake+CostofIceCream+CostPulav+CostTea)* 2.5)/100)

    Total_cost = (CostofNoodle+CostofDrinks+CostofChocolateShake+CostofIceCream+CostPulav+CostTea)

    CostofMeal= "Rs", str('%.2f' % (CostofNoodle+CostofDrinks+CostofChocolateShake+CostofIceCream+CostPulav+CostTea))
    C_gst = "Rs", str ('%.2f' % Central_GST)
    S_gst = "Rs", str ('%.2f' % State_GST)
    OverAllCost ="Rs", str ('%.2f' % (Total_cost+Central_GST+State_GST))
    Sgst.set(S_gst)
    Cost.set(CostofMeal)
    Cgst.set(C_gst)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    Tea.set("")
    Noodle.set("")
    ChocolateShake.set("")
    IceCream.set("")
    Pulav.set("")
    Drinks.set("")

    rand.set("")

    Total.set("")
    Sgst.set("")
    Cgst.set("")
    Cost.set("")
#=========================================================
#                  RESTAURANT MENU
#=========================================================

Tea=StringVar()
Noodle=StringVar()
ChocolateShake=StringVar()
IceCream=StringVar()
Pulav=StringVar()
Drinks=StringVar()
rand = StringVar()
Cost=StringVar()
Sgst=StringVar()
Cgst=StringVar()
Total=StringVar()

lblTea= Label(f1, font=('arial', 16, 'bold'),text="Tea",bd=16,anchor="w")
lblTea.grid(row=0, column=0)
lblTea=Entry(f1, font=('arial',16,'bold'),textvariable=Tea,bd=10,insertwidth=4,bg="white",justify='right')
lblTea.grid(row=0,column=1)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=1, column=0)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="white",justify='right')
txtDrinks.grid(row=1,column=1)

lblIceCream= Label(f1, font=('arial', 16, 'bold'),text="Ice-Cream",bd=16,anchor="w")
lblIceCream.grid(row=2, column=0)
lblIceCream=Entry(f1, font=('arial',16,'bold'),textvariable=IceCream,bd=10,insertwidth=4,bg="white",justify='right')
lblIceCream.grid(row=2,column=1)

lblNoodle= Label(f1, font=('arial', 16, 'bold'),text="Noodle",bd=16,anchor="w")
lblNoodle.grid(row=3, column=0)
txtNoodle=Entry(f1, font=('arial',16,'bold'),textvariable=Noodle,bd=10,insertwidth=4,bg="white",justify='right')
txtNoodle.grid(row=3,column=1)

lblChocolateShake= Label(f1, font=('arial', 16, 'bold'),text="Chocolate-Shake",bd=16,anchor="w")
lblChocolateShake.grid(row=4, column=0)
txtChocolateShake=Entry(f1, font=('arial',16,'bold'),textvariable=ChocolateShake,bd=10,insertwidth=4,bg="white",justify='right')
txtChocolateShake.grid(row=4,column=1)

lblPulav= Label(f1, font=('arial', 16, 'bold'),text="Rice-Plate",bd=16,anchor="w")
lblPulav.grid(row=5, column=0)
txtPulav=Entry(f1, font=('arial',16,'bold'),textvariable=Pulav,bd=10,insertwidth=4,bg="white",justify='right')
txtPulav.grid(row=5,column=1)


#=========================================================
#                  RESTAURANT BILL INFO
#=========================================================

lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=2)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblSgst= Label(f1, font=('arial', 16, 'bold'),text="SGST",bd=16,anchor="w")
lblSgst.grid(row=2, column=2)
txtSgst=Entry(f1, font=('arial',16,'bold'),textvariable=Sgst,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSgst.grid(row=2,column=3)


lblCgst= Label(f1, font=('arial', 16, 'bold'),text="CGST",bd=16,anchor="w")
lblCgst.grid(row=3, column=2)
txtCgst=Entry(f1, font=('arial',16,'bold'),textvariable=Cgst,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCgst.grid(row=3,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=4, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=4,column=3)

#=========================================================
#                  BUTTONS
#=========================================================

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

root.mainloop()

