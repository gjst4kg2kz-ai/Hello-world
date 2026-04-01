from tkinter import *

root = Tk()
root.title("Unlocked Layout ")

root.resizable(True, True)

for i in range(2):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

Label(root, text="Top Left", bg="lightblue").grid(row=0, column=0, sticky="nsew")
Label(root, text="Top Right", bg="lightgreen").grid(row=0, column=1, sticky="nsew")
Label(root, text="Bottom Left", bg="lightyellow").grid(row=1, column=0, sticky="nsew")
Label(root, text="Bottom Right", bg="lightpink").grid(row=1, column=1, sticky="nsew")

root.mainloop()