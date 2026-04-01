import tkinter as tk
from tkinter import messagebox

def compute_tax():
    try:
        income = float(entry_income.get())
        dependents = int(entry_dependents.get())
        total_tax = income * 0.1 - dependents * 100
        if total_tax < 0:
            total_tax = 0
        entry_total_tax.config(state="normal")
        entry_total_tax.delete(0, tk.END)
        entry_total_tax.insert(0, f"{total_tax:.2f}")
        entry_total_tax.config(state="readonly")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Tax Calculator")
root.geometry("300x150")
root.resizable(False, False)

tk.Label(root, text="Gross income").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_income = tk.Entry(root)
entry_income.grid(row=0, column=1, padx=10, pady=5)
entry_income.insert(0, "0.0")

tk.Label(root, text="Dependents").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_dependents = tk.Entry(root)
entry_dependents.grid(row=1, column=1, padx=10, pady=5)
entry_dependents.insert(0, "0")

compute_button = tk.Button(root, text="Compute", command=compute_tax)
compute_button.grid(row=2, column=0, columnspan=2, pady=5)

tk.Label(root, text="Total tax").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_total_tax = tk.Entry(root)
entry_total_tax.grid(row=3, column=1, padx=10, pady=5)
entry_total_tax.insert(0, "0.0")
entry_total_tax.config(state="readonly")

root.mainloop()