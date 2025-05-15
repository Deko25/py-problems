import tkinter as tk
from tkinter import messagebox

pet = {}
def add_pet():
    pet_name = entry_pet.get().strip()
    species = entry_species.get().strip()
    try:
        age = int(entry_age.get().strip())
        if pet_name in pet:
            pet[pet_name]['quantity'] = age
            messagebox.showinfo("SUCCESS", f"The pet '{pet_name}' was updated. Now has {pet[pet_name]['quantity']} years.")
        else:
            pet[pet_name] = {"species": species, "quantity": age}
            messagebox.showinfo("SUCCESS", f"The pet '{pet_name}'species' {species} ' with {age} years.")
    except ValueError:
        messagebox.showerror("Error", "The age must be a valid integer.")       
        
def fin_by_species():
    pet_name = entry_pet.get().strip()
    if pet_name in pet:
        pet_info = pet[pet_name]
        messagebox.showinfo("Pet Found",f"Name: {pet_name}\nSpecies: {pet_info['species']}\nAge: {pet_info['quantity']} years")
    else:
        messagebox.showerror("Not Found", f"The pet '{pet_name}' is not found in the inventory.")
        
def older_than():
    try:
        age = int(entry_age.get().strip())
        filtered_pets = {name: info for name, info in pet.items() if info['quantity'] >= age}
        if filtered_pets:
            pet_list = "\n".join([f"{name}: {info['quantity']}" for name, info in filtered_pets.items()])
            messagebox.showinfo("Filtered Pets", pet_list)
        else:
            messagebox.showinfo("Filtered Pets", "No pets found with the specified quantity.")
    except ValueError:
        messagebox.showerror("Error", "The quantity must be a valid integer.")

root = tk.Tk()
root.title("Pet Adoption Tracker")
tk.Label(root, text="Pet Name:").grid(row=0, column=0)
entry_pet = tk.Entry(root) 
entry_pet.grid(row=0, column=1)
tk.Label(root, text="Species:").grid(row=1, column=0)
entry_species = tk.Entry(root)
entry_species.grid(row=1, column=1)
tk.Label(root, text="age:").grid(row=2, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)
tk.Button(root, text="Add Pet", command=add_pet).grid(row=4, column=0)
tk.Button(root, text="Find Pet", command=fin_by_species).grid(row=4, column=1)  
tk.Button(root, text="Older Than", command=older_than).grid(row=4, column=2)
root.mainloop()                        