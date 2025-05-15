import tkinter as tk
from tkinter import messagebox 

library = {}

def add_book():
    title = entry_title.get().strip()
    try:
        author = entry_author.get().strip()
        pages = int(entry_pages.get())
        
        if title in library:
            library[title]['author'] = author
            library[title]['pages'] = pages
            messagebox.showinfo("SUCCESS", f"The title '{title}' was updated. Now has {pages} pages.")
        else:
            library[title] = {"author": author, "pages": pages}
            messagebox.showinfo("SUCCESS", f"The title '{title}' was added with author '{author}' and {pages} pages.")  
    except ValueError:         
        messagebox.showerror("Error", "The number of pages must be a valid integer.")

def find_book():
    title = entry_title.get().strip()
    if title in library:
        book = library[title]
        messagebox.showinfo("Book Found", f"Title: {title}\nAuthor: {book['author']}\nPages: {book['pages']}")
    else:
        messagebox.showerror("Not Found", f"The book '{title}' is not found in the inventory.")
 
def show_books():
    if library:
        books = "\n".join([f"{title}: {info['author']} ({info['pages']} pages)" for title, info in library.items()])
        messagebox.showinfo("Library Books", books)
    else:
        messagebox.showinfo("Library Books", "No books in the library.")

        
root = tk.Tk ()
root.title("Library Book Tracker")   

tk.Label(root, text="title book:").grid(row=0, column=0)
entry_title= tk.Entry(root)
entry_title.grid(row=0,column=1)
tk.Label(root, text="author:").grid(row=1,column=0)
entry_author=tk.Entry(root)
entry_author.grid(row=1,column=1)
tk.Label(root,text="pages:").grid(row=2,column=0)
entry_pages=tk.Entry(root)
entry_pages.grid(row=2,column=1)

tk.Button(root,text="add book", command=add_book).grid(row=4,column=0)
tk.Button(root,text="search book",command=find_book).grid(row=4,column=1)
tk.Button(root,text="show books",command=show_books).grid(row=4,column=2)
root.mainloop()     