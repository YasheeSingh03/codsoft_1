from tkinter import *
from tkinter import font
from tkinter import messagebox

WIND= Tk()
WIND.title("To-Do List App")
WIND.geometry("400x320")
p=Label(WIND,text="To Do List",font=("Algerian", 40, "bold"))
custom_font = font.Font(p,p.cget("font"))
custom_font.configure(underline=True,size=40)
p.configure(font=custom_font)
p.place(x=60,y=5)
s=Label(WIND,text="ADD ITEMS",font=("Arial",25,"italic"))
s.place(x=2,y=80)

def subm():
    task = entry.get()
    if task:
        box.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("WARNING!", "ENTER A TASK")
box =Listbox(WIND, width=65)
box.place(x=2,y=150)
entry = Entry(WIND,width=30,font=("Helvetica", 12),fg="blue")
entry.place(x=2,y=120)
SUBM= Button(WIND,width=15, text="SUBMIT", command=subm,bg="blue",fg="white")
SUBM.place(x=280,y=120)

WIND.mainloop()