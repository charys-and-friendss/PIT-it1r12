import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Student Management System")
window.geometry("950x600")
window.config(bg="#16161d")

bg_color = "#16161d"
card_color = "#232333"
button_color = "#7c5cff"
text_color = "white"

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




def clear_fields():


    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_year.delete(0, tk.END)




def delete_student():


    selected = table.selection()


    if not selected:
        messagebox.showwarning("Error", "Please select a student")
        return


    table.delete(selected)


    messagebox.showinfo("Deleted", "Student Deleted")




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




def select_student(event):


    selected = table.selection()


    if selected:


        values = table.item(selected, "values")


        clear_fields()


        entry_id.insert(0, values[0])
        entry_name.insert(0, values[1])
        entry_course.insert(0, values[2])
        entry_year.insert(0, values[3])



title = tk.Label(
    window,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Poppins", 24, "bold"),
    bg=bg_color,
    fg="white"
)


title.pack(pady=20)


main_frame = tk.Frame(
    window,
    bg=card_color,
    bd=0
)


main_frame.pack(pady=10, padx=20, fill="both")


form_frame = tk.Frame(
    main_frame,
    bg=card_color
)


form_frame.pack(side="left", padx=30, pady=30)

label_font = ("Poppins", 11, "bold")
entry_font = ("Poppins", 11)


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