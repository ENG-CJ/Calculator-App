from tkinter import *
root=Tk()

#Window Design
root.title("Calculator |Developed By ENGCJ")
root.config(bg="#003e53")
root.geometry("354x460")
root.resizable(False,False)

operator=""

#Functions
def click(number):
    global operator
    operator=operator+str(number)
    textin.set(operator)

def clear():
    global operator
    operator=""
    textin.set("0")

def equal():
    try:
        global operator
        add=str(eval(operator))
        textin.set(add)
        operator=""
    except:
        textin.set("Error")
        operator=""


textin=StringVar()
textin.set("Developer ENGCJ")
#ALL LABLES
Cal=Label(root,text="Calculator",bg="#003e53",fg="white",
          font=("Verdana",18,"bold"))
Cal.pack(side=TOP)

textEntry=Entry(root,font=("Verdana",16,"bold"),justify=RIGHT,textvariable=textin,width=21,bd=18,
                bg="white",relief="sunken")
textEntry.pack()

btn1=Button(root,text="1",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(1))
btn1.place(x=10,y=100)

btn2=Button(root,text="2",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(2))
btn2.place(x=10,y=170)

btn3=Button(root,text="3",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(3))
btn3.place(x=10,y=240)

btn4=Button(root,text="4",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(4))
btn4.place(x=75,y=100)

btn5=Button(root,text="5",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(5))
btn5.place(x=75,y=170)

btn6=Button(root,text="6",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(6))
btn6.place(x=75,y=240)

btn7=Button(root,text="7",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(7))
btn7.place(x=140,y=100)

btn8=Button(root,text="8",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(8))
btn8.place(x=140,y=170)

btn9=Button(root,text="9",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(9))
btn9.place(x=140,y=240)

btn0=Button(root,text="0",bg="white",fg="black",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click(0))
btn0.place(x=10,y=310)

dot=Button(root,text=".",bg="#8c001a",fg="white",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=47,pady=14,command=lambda:click("."))
dot.place(x=75,y=310)
plus=Button(root,text="+",bg="#000080",fg="white",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click("+"))
plus.place(x=205,y=100)
minus=Button(root,text="-",bg="#151b8d",fg="white",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click("-"))
minus.place(x=205,y=170)

mult=Button(root,text="*",bg="#571b7e",fg="white",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click("*"))
mult.place(x=205,y=240)

div=Button(root,text="/",bg="#f70d1a",fg="white",bd=4,relief="groove",
           font=("Verdana",16,"bold"),padx=14,pady=14,command=lambda:click("/"))
div.place(x=205,y=310)

clear=Button(root,text="CE",bg="#9f000f",fg="white",bd=4,relief="groove",
           font=("Verdana",16,"bold"),pady=119,padx=14,command=clear)
clear.place(x=270,y=100)

equal=Button(root,text="=",bg="#4b0082",fg="white",bd=4,relief="groove",
          font=("Verdana",16,"bold"),padx=151,pady=14,command=equal)
equal.place(x=10,y=380)
root.mainloop()