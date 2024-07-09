from tkinter import *
from tkinter import ttk
root=Tk()

root.title("translater")
root.geometry("500x700")
root.config(bg="red")
lab_txt=Label(root,text="Translator",font=("Times New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)
frame=Frame(root).pack(side=BOTTOM)
Sor_txt=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=140,height=200,width=480)














root.mainloop()