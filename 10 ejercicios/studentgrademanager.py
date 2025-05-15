import tkinter as tk
from tkinter import messagebox 

studen = {}

def add_student():
    student = entry_student.get().strip()
    try:
        grade = float(entry_grade.get().strip())  # Convertir a número
        if student in studen:
            studen[student]['grades'].append(grade)
            messagebox.showinfo("SUCCESS", f"The student '{student}' was updated with a new grade: {grade}.")
        else:
            studen[student] = {'grades': [grade]}
            messagebox.showinfo("SUCCESS", f"The student '{student}' was added with grade: {grade}.")  
    except ValueError:         
        messagebox.showerror("Error", "The grade must be a valid number.")
                
def add_grades():
    student = entry_student.get().strip()
    try:
        grade = float(entry_grade.get().strip()) 
        
        if student in studen:
            if 'grades' in studen[student]:
                studen[student]['grades'].append(grade)
            else:
                studen[student]['grades'] = [grade]
            messagebox.showinfo("SUCCESS", f"The student '{student}' received a new grade: {grade}.")
        else:
           
            studen[student] = {"grades": [grade]}
            messagebox.showinfo("SUCCESS", f"The student '{student}' was added with grade: {grade}.")  
    except ValueError:
        messagebox.showerror("Error", "The grade must be a valid number.")
def get_average():
    student = entry_student.get().strip()
    if student in studen:
        grades = studen[student]['grades']
        if grades:
            average = sum(grades) / len(grades)
            messagebox.showinfo("Average", f"The average grade for {student} is {average:.2f}")
        else:
            messagebox.showinfo("No Grades", f"No grades available for {student}.")
    else:
        messagebox.showinfo("Not Found", "This student is not in the list.")                
root = tk.Tk ()
root.title("student grade manager")   

tk.Label(root, text="student:").grid(row=0, column=0)
entry_student= tk.Entry(root)
entry_student.grid(row=0,column=1)
tk.Label(root, text="grade:").grid(row=1,column=0)
entry_grade=tk.Entry(root)
entry_grade.grid(row=1,column=1)

tk.Button(root,text="add students", command=add_student).grid(row=4,column=0)
tk.Button(root,text="add grades",command=add_grades).grid(row=4,column=1)
tk.Button(root,text="Average",command=get_average).grid(row=4,column=2)
root.mainloop()     