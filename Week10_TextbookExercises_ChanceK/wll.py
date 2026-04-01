from tkinter import *

root = Tk()
root.title("Locked Layout ")

root.resizable(False, False)

Label(root, text="Top Left").grid(row=0, column=0)
Label(root, text="Top Right").grid(row=0, column=1)
Label(root, text="Bottom Left").grid(row=1, column=0)
Label(root, text="Bottom Right").grid(row=1, column=1)

root.mainloop()