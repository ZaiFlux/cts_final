import tkinter as tk
from tkinter import ttk

# ===== Functions for menu actions =====
def main_menu():
    print("Main Menu clicked")

def add_contributor():
    print("Add Contributor clicked")

def edit_contributor():
    print("Edit Contributor clicked")

def generate_receipt():
    print("Generate Receipt clicked")

# ===== Create main window =====
root = tk.Tk()
root.title("Contribution Program")
root.geometry("600x400")

# ===== Top Row Header =====
top_frame = ttk.Frame(root, padding=5, relief="solid", borderwidth=1)
top_frame.pack(fill="x", padx=10, pady=5)

program_name = ttk.Label(top_frame, text="Program Name", font=("Arial", 12))
program_name.grid(row=0, column=0, sticky="w", padx=10)

due_date = ttk.Label(top_frame, text="Due Date", font=("Arial", 12))
due_date.grid(row=0, column=1, sticky="nsew")

# ===== Three-dot button =====
dots_button = ttk.Button(top_frame, text="⋯")
dots_button.grid(row=0, column=2, sticky="e", padx=10)

# ===== Menu =====
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Main Menu", command=main_menu)
menu.add_command(label="Add Contributor", command=add_contributor)
menu.add_command(label="Edit Contributor", command=edit_contributor)
menu.add_separator()
menu.add_command(label="Generate Receipt", command=generate_receipt)

def show_menu(event):
    menu.post(event.x_root, event.y_root)

dots_button.bind("<Button-1>", show_menu)

# Make middle column expand
top_frame.columnconfigure(1, weight=1)

# ===== Second Row: Contributor Header =====
header_frame = ttk.Frame(root, padding=5, relief="solid", borderwidth=1)
header_frame.pack(fill="x", padx=10)

columns = ["Contributor", "Current", "Target", "Remaining"]

for i, col in enumerate(columns):
    if col == "Remaining":
        ttk.Label(header_frame, text=col, font=("Arial", 11, "bold")).grid(row=0, column=i, sticky="e", padx=5)
    else:
        ttk.Label(header_frame, text=col, font=("Arial", 11, "bold")).grid(row=0, column=i, sticky="w", padx=5)
    header_frame.columnconfigure(i, weight=1)

# ===== Scrollable Area =====
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

# ===== Run App =====
root.mainloop()