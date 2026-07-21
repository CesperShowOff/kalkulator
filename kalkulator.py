from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("KALKULATOR")
root.geometry("310x400")
root["bg"] = "#d1d1d1"

myfont = font.Font(size=15)

e = Entry(root,width=25,borderwidth = 0)
e["font"] = myfont
e["bg"] = "#d1d1d1"
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

def angka(nilai):
    sebelum = e.get()
    e.delete(0,END)
    e.insert(0,str(sebelum)+str(nilai))


button1= Button(root,text='1',padx=30,pady=20,command=lambda:angka(1))
button2= Button(root,text='2',padx=30,pady=20,command=lambda:angka(2))
button3= Button(root,text='3',padx=30,pady=20,command=lambda:angka(3))
button4= Button(root,text='4',padx=30,pady=20,command=lambda:angka(4))
button5= Button(root,text='5',padx=30,pady=20,command=lambda:angka(5))
button6= Button(root,text='6',padx=30,pady=20,command=lambda:angka(6))
button7= Button(root,text='7',padx=30,pady=20,command=lambda:angka(7))
button8= Button(root,text='8',padx=30,pady=20,command=lambda:angka(8))
button9= Button(root,text='9',padx=30,pady=20,command=lambda:angka(9))
button0= Button(root,text='0',padx=30,pady=20,command=lambda:angka(0))


button1.grid(row=3,column=0,pady=2)
button2.grid(row=3,column=1,pady=2)
button3.grid(row=3,column=2,pady=2)
button4.grid(row=2,column=0,pady=2)
button5.grid(row=2,column=1,pady=2)
button6.grid(row=2,column=2,pady=2)
button7.grid(row=1,column=0,pady=2)
button8.grid(row=1,column=1,pady=2)
button9.grid(row=1,column=2,pady=2)
button0.grid(row=4,column=1,pady=2)
root.mainloop()