## Creating a Button with ttk module 
## Example 
```python
from tkinter import *

root = Tk()
root.geometry('100x100')
btn = Button(root, text = 'Click me !', bd = '7', command = root.destroy)
btn.pack(side = 'top')

root.mainloop()

# <<< EXAMPLE-2 >>>
# Following will import tkinter.ttk module and automatically override all the widgets which are present in tkinter module.
from tkinter import *
from tkinter.ttk import *

root = Tk()		
root.geometry('100x100')	
btn = Button(root, text = 'Click me !', command = root.destroy)
btn.pack(side = 'top')	

root.mainloop()
```
