import tkinter as tk

root = tk.Tk()
root.title("Receipt")
root.geometry("400x500")
root.configure(bg="black")

# Blank Receipt Template
receipt_text = """
==============================
           RECEIPT
==============================

Date Issued: 

Personal Info:

------------------------------
Current Amount : 
Target Amount  : 
Remaining Bal. : 

------------------------------
Due Date       : 
Mode of Payment: 

==============================
        THANK YOU!
==============================
"""

# Display receipt
label = tk.Label(root, text=receipt_text,
                 bg="black", fg="white",
                 font=("Courier", 11),
                 justify="left")
label.pack(padx=20, pady=20)

root.mainloop()