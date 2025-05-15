import tkinter as tk
from tkinter import messagebox

gym = {}

def register_member():
    member_name = entry_member.get().strip()
    try:
        membership_fee = float(entry_membership_fee.get().strip())
        if member_name in gym:
            gym[member_name]['membership_fee'] = membership_fee
            messagebox.showinfo("SUCCESS", f"The member '{member_name}' was updated. Now has a membership fee of {membership_fee}.")
        else:
            gym[member_name] = {"membership_fee": membership_fee}
            messagebox.showinfo("SUCCESS", f"The member '{member_name}' was added with a membership fee of {membership_fee}.")
    except ValueError:
        messagebox.showerror("Error", "The membership fee must be a valid number.")

def change_plan():
    member_name = entry_member.get().strip()
    try:
        membership_fee = float(entry_membership_fee.get().strip())
        if member_name in gym:
            gym[member_name]['membership_fee'] = membership_fee
            messagebox.showinfo("SUCCESS", f"The membership fee of '{member_name}' was updated to {membership_fee}.")
        else:
            messagebox.showerror("Error", f"The member '{member_name}' is not found in the gym.")
    except ValueError:
        messagebox.showerror("Error", "The membership fee must be a valid number.")

def unpaid_members():
    unpaid = [member for member in gym if gym[member]['membership_fee'] > 0]
    if unpaid:
        messagebox.showinfo("Unpaid Members", f"The following members have unpaid membership fees: {', '.join(unpaid)}")
    else:
        messagebox.showinfo("No Unpaid Members", "All members have paid their membership fees.")

root = tk.Tk()
root.title("Gym Membership Manager")
tk.Label(root, text="Member Name:").grid(row=0, column=0)
entry_member = tk.Entry(root)
entry_member.grid(row=0, column=1)
tk.Label(root, text="Membership Fee:").grid(row=1, column=0)
entry_membership_fee = tk.Entry(root)
entry_membership_fee.grid(row=1, column=1)
tk.Button(root, text="Register Member", command=register_member).grid(row=4, column=0)
tk.Button(root, text="Change Plan", command=change_plan).grid(row=4, column=1)
tk.Button(root, text="Unpaid Members", command=unpaid_members).grid(row=4, column=2)
root.mainloop()        