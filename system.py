import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# MAIN WINDOW
window = tk.Tk()
window.title("Student Management System")
window.geometry("950x600")
window.config(bg="#16161d")

# COLORS
bg_color = "#16161d"
card_color = "#232333"
button_color = "#7c5cff"
text_color = "white"

# TITLE
title = tk.Label(
    window,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Poppins", 24, "bold"),
    bg=bg_color,
    fg="white"
)

title.pack(pady=20)

# MAIN FRAME
main_frame = tk.Frame(
    window,
    bg=card_color,
    bd=0
)

main_frame.pack(pady=10, padx=20, fill="both")

# FORM FRAME
form_frame = tk.Frame(
    main_frame,
    bg=card_color
)

form_frame.pack(side="left", padx=30, pady=30)

# TABLE FRAME
table_frame = tk.Frame(
    main_frame,
    bg=card_color
)

table_frame.pack(side="right", padx=20, pady=20)
