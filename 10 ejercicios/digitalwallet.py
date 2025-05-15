import tkinter as tk 
from tkinter import messagebox

expense = {}

def add_expense():
    name_expense = entry_expense.get().strip()
    try:
        amount = float(entry_amount.get().strip())
        if name_expense in expense:
            expense[name_expense]['amount'] = amount
            messagebox.showinfo("SUCCESS", f"The expense '{name_expense}' was updated. Now has an amount of {expense[name_expense]['amount']}.")
        else:
            expense[name_expense] = {"amount": amount}
            messagebox.showinfo("SUCCESS", f"The expense '{name_expense}' was added with an amount of {amount}.")
    except ValueError:
        messagebox.showerror("Error", "The amount must be a valid number.")

def total_spent():
    total = sum(expense[expense_name]['amount'] for expense_name in expense)
    messagebox.showinfo("Total Spent", f"The total amount spent is {total:.2f}")
    
def expense_percentage():
    if expense:
        total = sum(expense[expense_name]['amount'] for expense_name in expense)
        for expense_name in expense:
            percentage = (expense[expense_name]['amount'] / total) * 100
            messagebox.showinfo("Percentage", f"The percentage of '{expense_name}' is {percentage:.2f}%")
    else:
        messagebox.showinfo("No Expenses", "No expenses available to calculate the percentage.")
        
root = tk.Tk()
root.title("Expense Tracker")
tk.Label(root, text="Expense Name:").grid(row=0, column=0)
entry_expense = tk.Entry(root)
entry_expense.grid(row=0, column=1)
tk.Label(root, text="Amount:").grid(row=1, column=0)
entry_amount= tk.Entry(root)
entry_amount.grid(row=1, column=1)
tk.Button(root, text="Add Expense", command=add_expense).grid(row=4, column=0)
tk.Button(root, text="Total Spent", command=total_spent).grid(row=4, column=1) 
tk.Button(root, text="Expense Percentage", command=expense_percentage).grid(row=4, column=2)
root.mainloop()            