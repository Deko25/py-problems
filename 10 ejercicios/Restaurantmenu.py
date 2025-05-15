import tkinter as tk
from tkinter import messagebox

dishes = {}

def add_dish():
    dish_name = entry_dish.get().strip()
    try:
        price = float(entry_price.get().strip())
        availability = int(entry_availability.get().strip())
        
        if dish_name in dishes:
            dishes[dish_name]['price'] = price
            dishes[dish_name]['availability'] = availability
            messagebox.showinfo("SUCCESS", f"The dish '{dish_name}' was updated. Now costs {price} and has {availability} available.")
        else:
            dishes[dish_name] = {"price": price, "availability": availability}
            messagebox.showinfo("SUCCESS", f"The dish '{dish_name}' was added with price {price} and {availability} available.")  
    except ValueError:         
        messagebox.showerror("Error", "The price and availability must be valid numbers.")
def change_availability():
    dish_name = entry_dish.get().strip()
    try:
        availability = int(entry_availability.get().strip())
        
        if dish_name in dishes:
            dishes[dish_name]['availability'] = availability
            messagebox.showinfo("SUCCESS", f"The availability of '{dish_name}' was updated to {availability}.")
        else:
            messagebox.showerror("Error", f"The dish '{dish_name}' is not found in the menu.")
    except ValueError:         
        messagebox.showerror("Error", "The availability must be a valid number.")

def total_available():
    total = sum(dish['availability'] for dish in dishes.values())
    messagebox.showinfo("Total Availability", f"The total number of available dishes is {total}.")
                 
root = tk.Tk()
root.title("Restaurant Menu Manager")

tk.Label(root, text="Dish Name:").grid(row=0, column=0)
entry_dish = tk.Entry(root)
entry_dish.grid(row=0, column=1)
tk.Label(root, text="Price:").grid(row=1, column=0)
entry_price = tk.Entry(root) 
entry_price.grid(row=1, column=1)
tk.Label(root, text="Availability:").grid(row=2, column=0)
entry_availability = tk.Entry(root) 
entry_availability.grid(row=2, column=1)

tk.Button(root, text="Add Dish", command=add_dish).grid(row=4, column=0)
tk.Button(root, text="modificar", command=change_availability).grid(row=4, column=1)
tk.Button(root, text="Total Available", command=total_available).grid(row=4, column=2)    
root.mainloop()
    