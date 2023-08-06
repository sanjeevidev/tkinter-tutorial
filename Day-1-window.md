## Creating Window UI
```python
from tkinter import *
from tkinter.ttk import *

# main window object named root
root = Tk()

# giving title to the main window
root.title("First_Program")

# Label is what output will be
label = Label(root, text ="Hello World !").pack()
root.mainloop()
```
