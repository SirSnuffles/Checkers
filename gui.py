# from tkinter import *
# "G:/Programs/PersonalPrograms/PythonScripts/checkers-board.jpg"
# from tkinter import ttk

# path = "G:\\Programs\\PersonalPrograms\\PythonScripts\\checkers-board.jpg"

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
img = ImageTk.PhotoImage(Image.open("checkers-board.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()