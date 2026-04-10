import tkinter as tk

def open_category_window():
    # create popup window
    cat_window = tk.Toplevel(root)
    cat_window.title("Select Category")
    cat_window.geometry("300x250")

    # variable to store selection
    category_var = tk.StringVar(value="Student")

    categories = [
        "Student",
        "Teacher",
        "Alumni",
        "Parent Sponsor",
        "Friend",
        "Others"
    ]

    tk.Label(cat_window, text="Choose a category:", font=("Arial", 12)).pack(pady=10)

    # create radio buttons
    for c in categories:
        tk.Radiobutton(cat_window, text=c, variable=category_var, value=c).pack(anchor="w")

    # show selected value
    def confirm():
        print("Selected:", category_var.get())
        cat_window.destroy()

    tk.Button(cat_window, text="OK", command=confirm).pack(pady=10)


# main window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

# category button
btn = tk.Button(root, text="Category", command=open_category_window)
btn.pack(pady=50)

root.mainloop()