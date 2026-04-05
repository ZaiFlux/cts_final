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
        name = entry_name.get()
        if not name.strip():
            messagebox.showwarning("Input Error", "Program Name cannot be empty!")
            return
        add_program_to_list(name)  # Add only Program Name to scrollable area
        contrib_window.destroy()

    tk.Button(contrib_window, text="Add", command=submit_info).pack(pady=15)

# --- Function to add clickable program name to scrollable area ---
def add_program_to_list(program_name):
    def on_click(event, name=program_name):
        messagebox.showinfo("Program Clicked", f"You clicked on '{name}'")
        # Later, you can open a new window with full program details or receipt

    lbl = tk.Label(
        scrollable_frame,
        text=program_name,
        anchor="w",
        font=("Arial", 12, "bold"),
        fg="orange",       # clickable color
        cursor="hand2"
    )
    lbl.pack(fill="x", padx=5, pady=2)
    lbl.bind("<Button-1>", on_click)  # Make it clickable

# --- Main window ---
root = tk.Tk()
root.title("Main Page") 
root.geometry("600x500")   

# --- Button to open Contribution Program ---
tk.Button(root, text="Create Contribution Program", command=open_contribution_window, width=30, height=2).pack(pady=10)

# --- Clean straight horizontal line ---
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=10, pady=5)

# --- Scrollable area for created programs ---
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