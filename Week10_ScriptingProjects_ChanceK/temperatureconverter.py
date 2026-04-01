import tkinter as tk
from tkinter import messagebox

def f_to_c():
    try:
        f = float(entry_f.get())
        c = (f - 32) * 5 / 9
        entry_c.delete(0, tk.END)
        entry_c.insert(0, f"{c:.2f}")
    except ValueError:
        messagebox.showerror("Input error", "Invalid input")

def c_to_f():
    try:
        c = float(entry_c.get())
        f = (c * 9 / 5) + 32
        entry_f.delete(0, tk.END)
        entry_f.insert(0, f"{f:.2f}")
    except ValueError:
        messagebox.showerror("Input error", "Invalid input")

root = tk.Tk()
root.title("Temperature Converter")
root.resizable(False, False)

tk.Label(root, text="Fahrenheit").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Celsius").grid(row=0, column=1, padx=10, pady=5)

entry_f = tk.Entry(root)
entry_f.grid(row=1, column=0, padx=10, pady=5)
entry_f.insert(0, "32.0")

entry_c = tk.Entry(root)
entry_c.grid(row=1, column=1, padx=10, pady=5)
entry_c.insert(0, "0.0")

tk.Button(root, text=">>>>", command=f_to_c).grid(row=2, column=0, pady=10)
tk.Button(root, text="<<<<", command=c_to_f).grid(row=2, column=1, pady=10)

root.mainloop()