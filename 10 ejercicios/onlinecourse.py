import  tkinter as tk
from tkinter import messagebox

curses = {}

def add_course():
    title = entry_course.get().strip()
    try:
        time = int(entry_time.get().strip())
        registered = int(entry_registered.get().strip())
        if title in curses:
            curses[title]['time'] = time
            curses[title]['registered'] = registered
            messagebox.showinfo("SUCCESS", f"The course '{title}' was updated. Now has {time} hours and {registered} students.")
        else:
            curses[title] = {"time": time, "registered": registered}
            messagebox.showinfo("SUCCESS", f"The course '{title}' was added with {time} hours and {registered} students.")
    except ValueError:
        messagebox.showerror("Error", "The time and registered must be valid numbers.")

def update_registered():
    title = entry_course.get().strip()
    try:
        registered = int(entry_registered.get().strip())
        if title in curses:
            curses[title]['registered'] = registered
            messagebox.showinfo("SUCCESS", f"The number of students in '{title}' was updated to {registered}.")
        else:
            messagebox.showerror("Error", f"The course '{title}' is not found in the list.")
    except ValueError:
        messagebox.showerror("Error", "The number of students must be a valid integer.")

def filter_by_hours():
    try:
        hours = int(entry_time.get().strip())
        filtered_courses = {title: info for title, info in curses.items() if info['time'] >= hours}
        if filtered_courses:
            courses_list = "\n".join([f"{title}: {info['time']} hours, {info['registered']} students" for title, info in filtered_courses.items()])
            messagebox.showinfo("Filtered Courses", courses_list)
        else:
            messagebox.showinfo("Filtered Courses", "No courses found with the specified hours.")
    except ValueError:
        messagebox.showerror("Error", "The number of hours must be a valid integer.")

root = tk.Tk()
root.title("Course Manager")
tk.Label(root, text="Course Title:").grid(row=0, column=0)
entry_course = tk.Entry(root)
entry_course.grid(row=0, column=1)
tk.Label(root, text="Time (hours):").grid(row=1, column=0)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1)
tk.Label(root, text="Registered Students:").grid(row=2, column=0)
entry_registered = tk.Entry(root)
entry_registered.grid(row=2, column=1)

tk.Button(root, text="Add Course", command=add_course).grid(row=4, column=0)
tk.Button(root, text="Update Registered", command=update_registered).grid(row=4, column=1)
tk.Button(root, text="Filter by Hours", command=filter_by_hours).grid(row=4, column=2)
root.mainloop()                        
        