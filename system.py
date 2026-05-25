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

# LABEL FONT
label_font = ("Poppins", 11, "bold")
entry_font = ("Poppins", 11)

# STUDENT ID
tk.Label(
    form_frame,
    text="Student ID",
    bg=card_color,
    fg="white",
    font=label_font
).grid(row=0, column=0, sticky="w", pady=10)

entry_id = tk.Entry(
    form_frame,
    font=entry_font,
    bg="#2f2f45",
    fg="white",
    insertbackground="white",
    bd=0,
    width=25
)

entry_id.grid(row=1, column=0, pady=5, ipady=8)

# FULL NAME
tk.Label(
    form_frame,
    text="Full Name",
    bg=card_color,
    fg="white",
    font=label_font
).grid(row=2, column=0, sticky="w", pady=10)

entry_name = tk.Entry(
    form_frame,
    font=entry_font,
    bg="#2f2f45",
    fg="white",
    insertbackground="white",
    bd=0,
    width=25
)

entry_name.grid(row=3, column=0, pady=5, ipady=8)

# COURSE
tk.Label(
    form_frame,
    text="Course",
    bg=card_color,
    fg="white",
    font=label_font
).grid(row=4, column=0, sticky="w", pady=10)

entry_course = tk.Entry(
    form_frame,
    font=entry_font,
    bg="#2f2f45",
    fg="white",
    insertbackground="white",
    bd=0,
    width=25
)

entry_course.grid(row=5, column=0, pady=5, ipady=8)

# YEAR
tk.Label(
    form_frame,
    text="Year Level",
    bg=card_color,
    fg="white",
    font=label_font
).grid(row=6, column=0, sticky="w", pady=10)

entry_year = tk.Entry(
    form_frame,
    font=entry_font,
    bg="#2f2f45",
    fg="white",
    insertbackground="white",
    bd=0,
    width=25
)

entry_year.grid(row=7, column=0, pady=5, ipady=8)

# BUTTON FRAME
button_frame = tk.Frame(
    form_frame,
    bg=card_color
)

button_frame.grid(row=8, column=0, pady=25)

# BUTTON STYLE
btn_font = ("Poppins", 10, "bold")

# ADD BUTTON
add_btn = tk.Button(
    button_frame,
    text="ADD",
    bg="#7c5cff",
    fg="white",
    font=btn_font,
    width=12,
    bd=0,
    pady=8,
    cursor="hand2",
    command=add_student
)

add_btn.grid(row=0, column=0, padx=5)

# UPDATE BUTTON
update_btn = tk.Button(
    button_frame,
    text="UPDATE",
    bg="#00b894",
    fg="white",
    font=btn_font,
    width=12,
    bd=0,
    pady=8,
    cursor="hand2",
    command=update_student
)

update_btn.grid(row=0, column=1, padx=5)

# DELETE BUTTON
delete_btn = tk.Button(
    button_frame,
    text="DELETE",
    bg="#d63031",
    fg="white",
    font=btn_font,
    width=12,
    bd=0,
    pady=8,
    cursor="hand2",
    command=delete_student
)

delete_btn.grid(row=0, column=2, padx=5)

# ADD STUDENT
def add_student():

    student_id = entry_id.get()
    name = entry_name.get()
    course = entry_course.get()
    year = entry_year.get()

    if student_id == "" or name == "" or course == "" or year == "":
        messagebox.showwarning("Error", "Please fill all fields")
        return

    table.insert("", tk.END, values=(
        student_id,
        name,
        course,
        year
    ))

    clear_fields()

    messagebox.showinfo("Success", "Student Added Successfully")


# CLEAR FIELDS
def clear_fields():

    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_year.delete(0, tk.END)


# DELETE STUDENT
def delete_student():

    selected = table.selection()

    if not selected:
        messagebox.showwarning("Error", "Please select a student")
        return

    table.delete(selected)

    messagebox.showinfo("Deleted", "Student Deleted")


# UPDATE STUDENT
def update_student():

    selected = table.selection()

    if not selected:
        messagebox.showwarning("Error", "Select a student first")
        return

    table.item(selected, values=(
        entry_id.get(),
        entry_name.get(),
        entry_course.get(),
        entry_year.get()
    ))

    clear_fields()

    messagebox.showinfo("Updated", "Student Updated")


# SELECT STUDENT
def select_student(event):

    selected = table.selection()

    if selected:

        values = table.item(selected, "values")

        clear_fields()

        entry_id.insert(0, values[0])
        entry_name.insert(0, values[1])
        entry_course.insert(0, values[2])
        entry_year.insert(0, values[3])




