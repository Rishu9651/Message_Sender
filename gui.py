import tkinter
import tkinter as tk
from tkinter.messagebox import showinfo, showerror
from main import *

def btn_click():
    num=number.get()
    msg=textMsg.get(1.0,"end-1c")
    r=send_sms(num,msg)
    if r:
        showinfo("Successfully sent!")
    else:
        showerror("Something went wrong!")


root = tk.Tk()
root.title("Message")
root.geometry("400x500")
l1 =tk.Label(root,text="To:")
l1.config(font= "16 " )
l1.grid(row=0,column=0,sticky=tkinter.E)
number = tk.Entry(root,)
number.grid(row=0,column=1,padx=10,pady=20)
textMsg = tk.Text(root,height=20,width=40)
textMsg.grid(row=1,column=1,padx=10,pady=30)
sendBtn = tk.Button(root, text="SEND SMS",command=btn_click)
sendBtn.grid(row=3,column=1)


root.mainloop()

