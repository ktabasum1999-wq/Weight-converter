import tkinter as tk
from tkinter import messagebox

# Function for conversion
def convert_weight():
    try:
        weight = float(weight_entry.get())
        unit = unit_var.get()

        if unit == "K":
            converted = weight * 2.205
            result_label.config(text=f"{round(converted, 2)} lbs", fg="#198754")
        elif unit == "L":
            converted = weight / 2.205
            result_label.config(text=f"{round(converted, 2)} kg", fg="#198754")
        else:
            messagebox.showerror("Error", "Please select a valid unit!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric weight.")

# Hover effect for button
def on_enter(e):
    convert_btn.config(bg="#0D6EFD")

def on_leave(e):
    convert_btn.config(bg="#007BFF")

# Main window
root = tk.Tk()
root.title("Weight Converter")
root.geometry("400x350")
root.configure(bg="#F1F3F6")

# Outer frame (for drop shadow illusion)
outer = tk.Frame(root, bg="#C9CCD0", bd=0)
outer.place(relx=0.5, rely=0.5, anchor="center", width=330, height=280)

# Inner card (main white box)
card = tk.Frame(root, bg="white", bd=0, highlightthickness=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=320, height=270)

# Title
title_label = tk.Label(
    card,
    text="⚖️ Weight Converter",
    font=("Segoe UI Semibold", 15),
    bg="white",
    fg="#212529"
)
title_label.pack(pady=(20, 10))

# Input Section
tk.Label(
    card,
    text="Enter your weight:",
    font=("Segoe UI", 11),
    bg="white",
    fg="#333333"
).pack(pady=(10, 5))

weight_entry = tk.Entry(
    card,
    font=("Segoe UI", 12),
    width=12,
    justify="center",
    relief="solid",
    bd=1
)
weight_entry.pack(pady=5)

# Unit selection
unit_var = tk.StringVar(value="K")

unit_frame = tk.Frame(card, bg="white")
unit_frame.pack(pady=10)

tk.Radiobutton(
    unit_frame, text="Kilograms", variable=unit_var, value="K",
    font=("Segoe UI", 10), bg="white", activebackground="white"
).pack(side="left", padx=15)

tk.Radiobutton(
    unit_frame, text="Pounds", variable=unit_var, value="L",
    font=("Segoe UI", 10), bg="white", activebackground="white"
).pack(side="left", padx=15)

# Convert Button
convert_btn = tk.Button(
    card,
    text="Convert",
    font=("Segoe UI", 11, "bold"),
    bg="#007BFF",
    fg="white",
    activebackground="#0056b3",
    activeforeground="white",
    relief="flat",
    width=14,
    height=1,
    command=convert_weight
)
convert_btn.pack(pady=15)

# Add hover effects
convert_btn.bind("<Enter>", on_enter)
convert_btn.bind("<Leave>", on_leave)

# Result Label
result_label = tk.Label(
    card,
    text="",
    font=("Segoe UI", 12, "bold"),
    bg="white",
    fg="#198754"
)
result_label.pack(pady=5)

# Footer
footer = tk.Label(
    root,
    text="Made with ❤️ by tabasum khan using Python Tkinter",
    font=("Segoe UI", 9),
    bg="#F1F3F6"
    fg="#6C757D"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
