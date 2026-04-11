import tkinter as tk
from tkinter import ttk, messagebox

def update_dynamic_field(*args):
    category = category_var.get()

    if category in ["Student", "Teacher"]:
        dynamic_label.config(text="School")
    elif category == "Alumni":
        dynamic_label.config(text="Year Graduated")
    elif category == "Parent Sponsor":
        dynamic_label.config(text="Child Name")
    else:
        dynamic_label.config(text="Additional Info")

def submit_form():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    location = location_entry.get()
    category = category_var.get()
    dynamic = dynamic_entry.get()

    # Validation
    if category == "Select Category":
        messagebox.showerror("Error", "Please select a category.")
        return

    if not name or not phone or not email:
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    if not phone.isdigit():
        messagebox.showerror("Error", "Phone must be digits only.")
        return

    if "@" not in email:
        messagebox.showerror("Error", "Invalid email.")
        return

    messagebox.showinfo("Success", "Contributor added successfully!")

# MAIN WINDOW
root = tk.Tk()
root.title("Contributor Form")
root.geometry("450x500")

# FORM FRAME (expands to push button down)
form_frame = tk.Frame(root)
form_frame.pack(expand=True)

# CATEGORY
tk.Label(form_frame, text="Category", font=("Arial", 10, "bold")).pack(pady=2)

category_var = tk.StringVar()

category_dropdown = ttk.Combobox(
    form_frame,
    textvariable=category_var,
    state="readonly",
    width=32
)

category_dropdown['values'] = (
    "Select Category",
    "Student",
    "Teacher",
    "Alumni",
    "Parent",
    "Sponsor",
    "Friend",
    "Others"
)

category_dropdown.current(0)
category_dropdown.pack(pady=5)

category_var.trace("w", update_dynamic_field)

# NAME
tk.Label(form_frame, text="Full Name").pack(pady=2)
name_entry = tk.Entry(form_frame, width=35)
name_entry.pack(pady=5)

# PHONE
tk.Label(form_frame, text="Phone Number").pack(pady=2)
phone_entry = tk.Entry(form_frame, width=35)
phone_entry.pack(pady=5)

# EMAIL
tk.Label(form_frame, text="Email Address").pack(pady=2)
email_entry = tk.Entry(form_frame, width=35)
email_entry.pack(pady=5)

# LOCATION
tk.Label(form_frame, text="Location").pack(pady=2)
location_entry = tk.Entry(form_frame, width=35)
location_entry.pack(pady=5)

# DYNAMIC FIELD
dynamic_label = tk.Label(form_frame, text="Additional Info")
dynamic_label.pack(pady=2)
dynamic_entry = tk.Entry(form_frame, width=35)
dynamic_entry.pack(pady=5)

# BOTTOM BUTTON
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", pady=25)

tk.Button(
    bottom_frame,
    text="Add Contributor",
    command=submit_form,
    bg="#4CAF50",
    fg="white",
    width=25
).pack()

root.mainloop()