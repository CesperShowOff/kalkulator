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

def tambah():
    angka_pertama = e.get()
    global n_awal
    global mtk
    mtk = 'penjumlahan'
    n_awal = int(angka_pertama)
    e.delete(0,END)
    
def kurang():
    angka_pertama = e.get()
    global n_awal
    global mtk
    mtk = 'pengurangan'
    n_awal = int(angka_pertama)
    e.delete(0,END)

def kali():
    angka_pertama = e.get()
    global n_awal
    global mtk
    mtk = 'perkalian'
    n_awal = int(angka_pertama)
    e.delete(0,END)
    
def bagi():
    angka_pertama = e.get()
    global n_awal
    global mtk
    mtk = 'pembagian'
    n_awal = int(angka_pertama)
    e.delete(0,END)
    
def hapus():
    e.delete(0,END)
    
def samadengan():
    angka_akhir = e.get()
    e.delete(0,END)
    if mtk == 'penjumlahan':
        e.insert(0,n_awal + int(angka_akhir))
    elif mtk == 'pengurangan':
        e.insert(0,n_awal - int(angka_akhir))
    elif mtk == 'perkalian':
        e.insert(0,n_awal * int(angka_akhir))
    elif mtk == 'pembagian':
        try :
            hitung = n_awal / int(angka_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError :
            e.insert(0,'Undefined')
            
        

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
tamb= Button(root,text='+',padx=30,pady=20,command=tambah)
kur= Button(root,text='-',padx=30,pady=20,command=kurang)
kal= Button(root,text='*',padx=30,pady=20,command=kali)
defined= Button(root,text='/',padx=30,pady=20,command=bagi)
delete= Button(root,text='C',padx=30,pady=20,command=hapus)
hasil= Button(root,text='=',padx=30,pady=20,command=samadengan)

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
tamb.grid(row=1,column=3,pady=2)
kur.grid(row=2,column=3,pady=2)
kal.grid(row=3,column=3,pady=2)
defined.grid(row=4,column=3,pady=2)
delete.grid(row=4,column=0,pady=2)
hasil.grid(row=4,column=2,pady=2)



root.mainloop()