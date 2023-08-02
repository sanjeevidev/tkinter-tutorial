#Example-1 - Start and Stop Buttons
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

#Example-2 - Button with Different Colors
import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Colored Button Example")
button = tk.Button(root, text="Click Me!", command=on_button_click, bg="black", fg="white")
button.pack()

root.mainloop()

#Example-3 - Button with Image
import tkinter as tk
from PIL import Image, ImageTk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Button with Image Example")

# Load the image
image = Image.open("path/to/image.png")
photo = ImageTk.PhotoImage(image)

button = tk.Button(root, image=photo, command=on_button_click)
button.pack()

root.mainloop()