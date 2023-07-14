from tkinter import *

#Window details
window = Tk()
window.title("Calculator")
window.geometry("320x360")
window.configure(bg="#3498DB")
equation = StringVar()
value =""

#Inputting numbers
def press(num):
    global value
    value = value + str(num)
    equation.set(value)

#Operations
def equal_to(val):
    try:
        global value
        total = str(eval(value))
        equation.set(total)
        value = ""
    except ZeroDivisionError:
        equation.set("Error")
        value = ""


#Clear Operation
def clear():
    global value
    value = ""
    equation.set("")

#Input Label

input_label = Entry(window,bg="#5DADE2",textvariable=equation,fg="#fff",width=15,font=("CALIBRI",30)).grid(columnspan=4,padx=9,pady=13)

#Buttons
btnclr = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="C",width=4,font=("CALIBRI",15),command=lambda: clear()).grid(row=1,column=0)
btndiv = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="/",width=4,font=("CALIBRI",15),command=lambda: press("/")).grid(row=1,column=1)
btnmultiply = Button(window,padx=5,bg="#4460FF",pady=3,fg="#fff",text="*",width=4,font=("CALIBRI",15),command=lambda: press("*")).grid(row=1,column=2)
btnsub = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="-",width=4,font=("CALIBRI",15),command=lambda: press("-")).grid(row=1,column=3)

btn7 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="7",width=4,font=("CALIBRI",15),command=lambda: press(7)).grid(row=3,column=0,pady=10)
btn8 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="8",width=4,font=("CALIBRI",15),command=lambda: press(8)).grid(row=3,column=1)
btn9 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="9",width=4,font=("CALIBRI",15),command=lambda: press(9)).grid(row=3,column=2)


btn4 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="4",width=4,font=("CALIBRI",15),command=lambda:press(4)).grid(row=4,column=0)
btn5 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="5",width=4,font=("CALIBRI",15),command=lambda:press(5)).grid(row=4,column=1)
btn6 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="6",width=4,font=("CALIBRI",15),command=lambda:press(6)).grid(row=4,column=2)

btn1 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="1",width=4,font=("CALIBRI",15),command=lambda:press(1)).grid(row=5,column=0,pady=10)
btn2 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="2",width=4,font=("CALIBRI",15),command=lambda:press(2)).grid(row=5,column=1)
btn3 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="3",width=4,font=("CALIBRI",15),command=lambda:press(3)).grid(row=5,column=2)


btn0 = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="0",height=1,width=13,font=("CALIBRI",13),command=lambda:press(0)).place(x=11,y=306)
btnpoint = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text=".",height=1,width=4,font=("CALIBRI",15)).grid(row=6,column=2)

btnadd = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="+",height=3,width=4,font=("CALIBRI",16),command=lambda: press("+")).place(x=250,y=135)
btnans = Button(window,padx=5,pady=3,bg="#4460FF",fg="#fff",text="=",height=3,width=4,font=("CALIBRI",16),command=lambda: equal_to("=")).place(x=250,y=246)




window.mainloop()