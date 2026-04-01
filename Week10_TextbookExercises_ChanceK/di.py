from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()
root.title("Kitty")

img = Image.open("kitty.jpg")
photo = ImageTk.PhotoImage(img)

label = Label(root, image=photo)
label.pack()

root.mainloop()
