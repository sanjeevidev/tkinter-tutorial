#Start and Stop Buttons
import tkinter as tk
from tkinter import messagebox

r = tk.Tk()
r.title('Counting Seconds')
def show():
    tk.messagebox.showinfo("Hello","Displayed")

button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button1 = tk.Button(r, text='Start', width=20, command=show)

button.pack()
button1.pack()

r.mainloop()