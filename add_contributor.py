import tkinter as tk

def open_category_window():
    cat_window = tk.Toplevel(root)
    cat_window.title("Select Category")
    cat_window.geometry("300x300")

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

    for c in categories:
        tk.Radiobutton(cat_window, text=c, variable=category_var, value=c).pack(anchor="w")

    def confirm():
        selected = category_var.get()
        set_placeholder(f"Enter {selected} name")
        cat_window.destroy()

    tk.Button(cat_window, text="OK", command=confirm).pack(pady=10)


def set_placeholder(text):
    entry.delete(0, tk.END)
    entry.insert(0, text)
    entry.config(fg="grey")
    entry.placeholder = text


def on_focus_in(event):
    if entry.get() == entry.placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")


def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, entry.placeholder)
        entry.config(fg="grey")


# MAIN WINDOW
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

tk.Button(root, text="Category", command=open_category_window).pack(pady=20)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# default placeholder
entry.placeholder = "Enter name"
entry.insert(0, entry.placeholder)
entry.config(fg="grey")

# events for placeholder behavior
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)

root.mainloop()