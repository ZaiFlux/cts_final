import tkinter as tk
from tkinter import ttk, messagebox

# ===== Sample Data (ALL ZERO) =====
contributors_data = [
    {"name": "Ana", "current": 0.00, "target": 0.00, "last_added": 0.00},
    {"name": "John", "current": 0.00, "target": 0.00, "last_added": 0.00},
    {"name": "Maria", "current": 0.00, "target": 0.00, "last_added": 0.00},
]

col_widths = [200, 100, 100, 120]
edit_refresh_callback = None

# ===== Functions =====
def main_menu():
    print("Main Menu clicked")

def add_contributor():
    print("Add Contributor clicked")

def generate_receipt():
    print("Generate Receipt clicked")

# ===== Main Table Refresh =====
def refresh_table():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    for row_index, data in enumerate(contributors_data):
        remaining = data["target"] - data["current"]

        ttk.Label(scrollable_frame, text=data["name"]).grid(row=row_index, column=0, sticky="w", padx=5, pady=2)
        ttk.Label(scrollable_frame, text=f"{data['current']:.2f}").grid(row=row_index, column=1, sticky="e", padx=5)
        ttk.Label(scrollable_frame, text=f"{data['target']:.2f}").grid(row=row_index, column=2, sticky="e", padx=5)
        ttk.Label(scrollable_frame, text=f"{remaining:.2f}").grid(row=row_index, column=3, sticky="e", padx=5)

# ===== Add Amount Window =====
def open_add_amount(index):
    data = contributors_data[index]

    form_window = tk.Toplevel(root)
    form_window.title(f"Add Amount - {data['name']}")
    form_window.geometry("300x200")

    ttk.Label(form_window, text=data["name"], font=("Arial", 11, "bold")).pack(pady=10)

    ttk.Label(form_window, text="Enter Amount").pack()
    amount_entry = ttk.Entry(form_window)
    amount_entry.pack(pady=5)

    def update_amount():
        try:
            amount = float(amount_entry.get())
            data["current"] += amount
            data["last_added"] = amount

            refresh_table()

            if edit_refresh_callback:
                edit_refresh_callback()

            form_window.destroy()
        except:
            print("Invalid input")

    ttk.Button(form_window, text="Update", command=update_amount).pack(pady=10)

# ===== EDIT / MANAGE RECORDS =====
def edit_contributor():
    global edit_refresh_callback

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Records")
    edit_window.geometry("550x350")

    ttk.Label(edit_window, text="Manage records", font=("Arial", 12)).pack(pady=10)

    frame = ttk.Frame(edit_window)
    frame.pack(fill="both", expand=True, padx=10, pady=5)

    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    list_frame = ttk.Frame(canvas)

    list_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=list_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # ===== Refresh List =====
    def refresh_edit_list():
        for widget in list_frame.winfo_children():
            widget.destroy()

        for i, data in enumerate(contributors_data):
            row = ttk.Frame(list_frame)
            row.pack(fill="x", pady=5)

            # Name
            ttk.Label(row, text=data["name"], width=15).pack(side="left")

            # Add Amount Button
            ttk.Button(
                row,
                text="Add Current Amount",
                command=lambda idx=i: open_add_amount(idx)
            ).pack(side="left", padx=10)

            # Right side container
            right_frame = ttk.Frame(row)
            right_frame.pack(side="right")

            # Last added
            ttk.Label(
                right_frame,
                text=f"{data['last_added']:.2f}",
                width=10,
                anchor="e"
            ).pack(side="left", padx=5)

            # ❌ DELETE BUTTON
            def delete_record(idx=i):
                confirm = messagebox.askyesno(
                    "Delete Record",
                    f"Delete '{contributors_data[idx]['name']}'?\nThis cannot be undone."
                )
                if confirm:
                    contributors_data.pop(idx)
                    refresh_edit_list()
                    refresh_table()

            ttk.Button(
                right_frame,
                text="❌",
                width=3,
                command=delete_record
            ).pack(side="left")

    edit_refresh_callback = refresh_edit_list
    refresh_edit_list()

# ===== MAIN WINDOW =====
root = tk.Tk()
root.title("Contribution Program")
root.geometry("600x400")

# ===== TOP HEADER =====
top_frame = ttk.Frame(root, padding=5, relief="solid", borderwidth=1)
top_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(top_frame, text="Program Name", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10)
ttk.Label(top_frame, text="Due Date", font=("Arial", 12)).grid(row=0, column=1, sticky="nsew")

dots_button = ttk.Button(top_frame, text="⋯")
dots_button.grid(row=0, column=2, sticky="e", padx=10)

menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Main Menu", command=main_menu)
menu.add_command(label="Add Contributor", command=add_contributor)
menu.add_command(label="Edit Records", command=edit_contributor)
menu.add_separator()
menu.add_command(label="Generate Receipt", command=generate_receipt)

dots_button.bind("<Button-1>", lambda e: menu.post(e.x_root, e.y_root))
top_frame.columnconfigure(1, weight=1)

# ===== TABLE HEADER =====
header_frame = ttk.Frame(root, padding=5, relief="solid", borderwidth=1)
header_frame.pack(fill="x", padx=10)

columns = ["Contributor", "Current", "Target", "Remaining"]

for i, col in enumerate(columns):
    anchor = "e" if col != "Contributor" else "w"

    ttk.Label(header_frame, text=col, font=("Arial", 11, "bold")).grid(row=0, column=i, sticky=anchor, padx=5)
    header_frame.columnconfigure(i, minsize=col_widths[i])

# ===== SCROLLABLE TABLE =====
scroll_frame = ttk.Frame(root)
scroll_frame.pack(fill="both", expand=True, padx=10, pady=5)

canvas = tk.Canvas(scroll_frame)
scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

for i in range(4):
    scrollable_frame.columnconfigure(i, minsize=col_widths[i])

# ===== INIT =====
refresh_table()

# ===== RUN =====
root.mainloop()