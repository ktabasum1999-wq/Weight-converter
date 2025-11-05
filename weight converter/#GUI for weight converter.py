#GUI for weight converter

import tkinter as tk
from tkinter import messagebox


# Convert Function

def convert_weight():
    try:
        weight = float(weight_entry.get())
        unit = unit_var.get()

        if unit == "K":
            converted = weight * 2.205
            result_label.config(
                text=f"{round(converted, 2)} lbs",
                fg="#2E8B57"
            )
        elif unit == "L":
            converted = weight / 2.205
            result_label.config(
                text=f"{round(converted, 2)} kg",
                fg="#2E8B57"
            )
        else:
            messagebox.showerror("Error", "Please select a valid unit!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric weight.")

# GUI Window Setup

root = tk.Tk()
root.title("Weight Converter")
root.geometry("350x280")
root.config(bg="#F8F9FA")  # light background

# Title Label

title_label = tk.Label(
    root,
    text="⚖️ Weight Converter",
    font=("Segoe UI", 16, "bold"),
    bg="#F8F9FA",
    fg="#333333"
)
title_label.pack(pady=15)

 
# Weight Input Section
 
frame = tk.Frame(root, bg="#F8F9FA")
frame.pack(pady=5)

tk.Label(
    frame,
    text="Enter your weight:",
    font=("Segoe UI", 12),
    bg="#F8F9FA"
).grid(row=0, column=0, padx=5, pady=5)

weight_entry = tk.Entry(frame, font=("Segoe UI", 12), width=10, justify="center")
weight_entry.grid(row=0, column=1, padx=5, pady=5)

# Radio Buttons for Units

unit_var = tk.StringVar(value="K")

unit_frame = tk.Frame(root, bg="#F8F9FA")
unit_frame.pack(pady=10)

tk.Radiobutton(
    unit_frame, text="Kilograms", variable=unit_var, value="K",
    font=("Segoe UI", 11), bg="#F8F9FA"
).pack(side="left", padx=10)

tk.Radiobutton(
    unit_frame, text="Pounds", variable=unit_var, value="L",
    font=("Segoe UI", 11), bg="#F8F9FA"
).pack(side="left", padx=10)


# Convert Button

convert_btn = tk.Button(
    root,
    text="Convert",
    font=("Segoe UI", 12, "bold"),
    bg="#007BFF",
    fg="white",
    activebackground="#0056b3",
    activeforeground="white",
    relief="flat",
    width=12,
    command=convert_weight
)
convert_btn.pack(pady=10)

# Result Label

result_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 13, "bold"),
    bg="#F8F9FA",
    fg="#333333"
)
result_label.pack(pady=10)

# Footer Note

footer = tk.Label(
    root,
    text="Made with ❤️ using Python Tkinter",
    font=("Segoe UI", 9),
    bg="#F8F9FA",
    fg="#777777"
)
footer.pack(side="bottom", pady=5)

root.mainloop()
