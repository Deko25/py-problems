import tkinter as tk
from tkinter import messagebox

box = {}

def add_box():
    box_name = entry_box.get().strip()
    try:
        quantity = int(entry_quantity.get().strip())
        if box_name in box:
            box[box_name]['quantity'] += quantity
            messagebox.showinfo("SUCCESS", f"The box '{box_name}' was updated. Now has {box[box_name]['quantity']} items.")
        else:
            box[box_name] = {"quantity": quantity}
            messagebox.showinfo("SUCCESS", f"The box '{box_name}' was added with {quantity} items.")
    except ValueError:
        messagebox.showerror("Error", "The quantity must be a valid integer.")    

def update_quantity():
    box_name = entry_box.get().strip()
    try:
        quantity = int(entry_quantity.get().strip())
        if box_name in box:
            box[box_name]['quantity'] = quantity
            messagebox.showinfo("SUCCESS", f"The quantity of '{box_name}' was updated to {quantity}.")
        else:
            messagebox.showerror("Error", f"The box '{box_name}' is not found in the inventory.")
    except ValueError:
        messagebox.showerror("Error", "The quantity must be a valid integer.")    

def has_enough():
    box_name = entry_box.get().strip()
    try:
        quantity = int(entry_quantity.get().strip())
        if box_name in box:
            if box[box_name]['quantity'] >= quantity:
                messagebox.showinfo("SUCCESS", f"The box '{box_name}' has enough items: {quantity} .")
            else:
                messagebox.showinfo("Not Enough", f"The box '{box_name}' does not have enough items.")
        else:
            messagebox.showerror("Error", f"The box '{box_name}' is not found in the inventory.")
    except ValueError:
        messagebox.showerror("Error", "The quantity must be a valid integer.")

root = tk.Tk()
root.title("Warehouse Box Manager") 

tk.Label(root, text="Box Name:").grid(row=0, column=0)
entry_box = tk.Entry(root)
entry_box.grid(row=0, column=1)
tk.Label(root, text="Quantity:").grid(row=1, column=0)
entry_quantity = tk.Entry(root) 
entry_quantity.grid(row=1, column=1)
tk.Button(root, text="Add Box", command=add_box).grid(row=4, column=0)
tk.Button(root, text="Update Quantity", command=update_quantity).grid(row=4, column=1)
tk.Button(root, text="Check Availability", command=has_enough).grid(row=4, column=2)

root.mainloop()            
    
# update_quantity():
# has_enough():