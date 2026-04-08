import tkinter as tk
from tkinter import ttk, messagebox

# --- Function to open Contribution Program window ---
def open_contribution_window():
    contrib_window = tk.Toplevel(root)
    contrib_window.title("Create Contribution Program")
    contrib_window.geometry("400x300")

    # Labels and Entries
    tk.Label(contrib_window, text="Program Name:").pack(anchor="w", padx=10, pady=5)
    entry_name = tk.Entry(contrib_window, width=40)
    entry_name.pack(padx=10)

    tk.Label(contrib_window, text="Purpose:").pack(anchor="w", padx=10, pady=5)
    entry_purpose = tk.Entry(contrib_window, width=40)
    entry_purpose.pack(padx=10)

    tk.Label(contrib_window, text="Target Amount:").pack(anchor="w", padx=10, pady=5)
    entry_target = tk.Entry(contrib_window, width=40)
    entry_target.pack(padx=10)

    tk.Label(contrib_window, text="Due Date:").pack(anchor="w", padx=10, pady=5)
    entry_due = tk.Entry(contrib_window, width=40)
    entry_due.pack(padx=10)

    # --- Add button ---
    def submit_info():
        name = entry_name.get().strip()
        purpose = entry_purpose.get().strip()
        target = entry_target.get().strip()
        due = entry_due.get().strip()

        if not name:
            messagebox.showwarning("Input Error", "Program Name cannot be empty!")
            return

        add_program_to_list(name, purpose, target, due)
        contrib_window.destroy()

    tk.Button(contrib_window, text="Add", command=submit_info).pack(pady=15)

# --- Function to add program row ---
def add_program_to_list(program_name, purpose, target, due):

    def on_click(event, name=program_name):
        messagebox.showinfo("Program Clicked", f"You clicked on '{name}'")

    def delete_program():
        lbl_frame.destroy()

    # Row frame
    lbl_frame = tk.Frame(scrollable_frame)
    lbl_frame.pack(fill="x", padx=5, pady=2)

    # Column 0: Program Name
    lbl_name = tk.Label(lbl_frame, text=program_name, font=("Arial", 12, "bold"),
                        fg="orange", cursor="hand2")
    lbl_name.grid(row=0, column=0, sticky="w")
    lbl_name.bind("<Button-1>", on_click)

    # Column 1: Purpose
    tk.Label(lbl_frame, text=f"Purpose: {purpose}")\
        .grid(row=0, column=1, padx=10, sticky="w")

    # Column 2: Target
    tk.Label(lbl_frame, text=f"Target: {target}")\
        .grid(row=0, column=2, padx=10, sticky="w")

    # Column 3: Due Date (this expands)
    tk.Label(lbl_frame, text=f"Due: {due}")\
        .grid(row=0, column=3, padx=10, sticky="w")

    # Column 4: 3 dots (far right)
    dots_btn = tk.Button(lbl_frame, text="⋮", font=("Arial", 12), bd=0, cursor="hand2")
    dots_btn.grid(row=0, column=4, sticky="e")

    # Make column 3 expand to push dots to the right
    lbl_frame.grid_columnconfigure(3, weight=1)

    # Menu
    menu = tk.Menu(lbl_frame, tearoff=0)
    menu.add_command(label="Delete", command=delete_program)

    def show_menu(event):
        menu.tk_popup(event.x_root, event.y_root)

    dots_btn.bind("<Button-1>", show_menu)

# --- Main window ---
root = tk.Tk()
root.title("Main Page")
root.geometry("700x500")

# Button
tk.Button(root, text="Create Contribution Program",
          command=open_contribution_window,
          width=30, height=2).pack(pady=10)

# Separator
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=10, pady=5)

# Scrollable area
scroll_frame = tk.Frame(root)
scroll_frame.pack(fill="both", expand=True, padx=10, pady=5)

canvas = tk.Canvas(scroll_frame)
scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()