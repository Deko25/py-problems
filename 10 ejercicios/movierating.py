import tkinter as tk
from tkinter import messagebox

movie= {}

def add_movie():
    name_movie = entry_movie.get().strip()
    try:
        rating = float(entry_rating.get().strip())
        if name_movie in movie:
            movie[name_movie]['rating'] = rating
            messagebox.showinfo("SUCCESS", f"The movie '{name_movie}' was updated. Now has a rating of {rating}.")
        else:
            movie[name_movie] = {"rating": rating}
            messagebox.showinfo("SUCCESS", f"The movie '{name_movie}' was added with a rating of {rating}.")
    except ValueError:
        messagebox.showerror("Error", "The rating must be a valid number.")
        
def rate_movie():
    name_movie = entry_movie.get().strip()
    try:
        rating = float(entry_rating.get().strip())
        if 0 <= rating <= 5:
            movie[name_movie]['rating'] = rating
            messagebox.showinfo("SUCCESS", f"The movie '{name_movie}' was updated. Now has a rating of {rating}.")
        else:
            messagebox.showerror("Error", f"The rate'{name_movie}' not within the range of 0 to 5.")
    except ValueError:
        messagebox.showerror("Error", "The rating must be a valid number.")

def average_rating():
    if movie:
        total_rating = sum(movie[movie_name]['rating'] for movie_name in movie)
        average = total_rating / len(movie)
        messagebox.showinfo("Average Rating", f"The average rating of all movies is {average:.2f}")
    else:
        messagebox.showinfo("No Movies", "No movies available to calculate the average rating.")

root = tk.Tk()
root.title("Movie Rating Manager")
tk.Label(root, text="Movie Name:").grid(row=0, column=0)
entry_movie = tk.Entry(root)
entry_movie.grid(row=0, column=1)
tk.Label(root, text="Rating:").grid(row=1, column=0)
entry_rating = tk.Entry(root)
entry_rating.grid(row=1, column=1)
tk.Button(root, text="Add Movie", command=add_movie).grid(row=4, column=0)
tk.Button(root, text="Rate Movie", command=rate_movie).grid(row=4, column=1)
tk.Button(root, text="Average Rating", command=average_rating).grid(row=4, column=2)
root.mainloop()                        
