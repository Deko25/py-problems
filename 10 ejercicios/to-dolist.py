import tkinter as tk
from tkinter import messagebox

tasks = {}

def add_taks():
    task_name = entry_task.get()
    try:
        priority = str(entry_priority.get())
        if task_name in tasks:
            tasks[task_name]['priority'] = priority
            messagebox.showinfo("SUCCESS", f"The task '{task_name}' was updated. Now has a priority of {priority}.")
        else:
            tasks[task_name] = {"priority": priority}
            messagebox.showinfo("SUCCESS", f"The task '{task_name}' was added with a priority of {priority}.")
    except ValueError:
        messagebox.showerror("Error", "The priority must be a valid number.")

def complete_task():
    task_name = entry_task.get().strip()
    if task_name in tasks:
        del tasks[task_name]
        messagebox.showinfo("SUCCESS", f"The task '{task_name}' was completed and removed from the list.")
    else:
        messagebox.showerror("Error", f"The task '{task_name}' is not found in the list.")

def filter_tasks():
    try:
        priority = str(entry_priority.get().strip())
        filtered_tasks = {task: info for task, info in tasks.items() if info['priority'] >= priority}
        if filtered_tasks:
            task_list = "\n".join([f"{task}: {info['priority']}" for task, info in filtered_tasks.items()])
            messagebox.showinfo("Filtered Tasks", task_list)
        else:
            messagebox.showinfo("Filtered Tasks", "No tasks found with the specified priority.")
    except ValueError:
        messagebox.showerror("Error", "The priority .")

root = tk.Tk()
root.title("Task Manager")
tk.Label(root, text="Task:").grid(row=0, column=0)
entry_task = tk.Entry(root)
entry_task.grid(row=0, column=1)
tk.Label(root, text="Priority:").grid(row=1, column=0)
entry_priority = tk.Entry(root)
entry_priority.grid(row=1, column=1)

tk.Button(root, text="Add Task", command=add_taks).grid(row=4, column=0)
tk.Button(root, text="Complete Task", command=complete_task).grid(row=4, column=1)
tk.Button(root, text="Filter Tasks", command=filter_tasks).grid(row=4, column=2)
root.mainloop()
                        