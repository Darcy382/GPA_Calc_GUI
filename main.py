from tkinter import *
from Course import Course

root = Tk()
root.title("GPA Calculator")

rows = []
current_row = 1


def add_row():
    this_row = len(rows)
    global current_row
    rows.append(list())
    rows[this_row].append(Entry(root, width=15))
    rows[this_row].append(Entry(root, width=7))
    rows[this_row].append(Entry(root, width=7))
    rows[this_row][0].grid(row=current_row, column=0)
    rows[this_row][1].grid(row=current_row, column=1)
    rows[this_row][2].grid(row=current_row, column=2)
    current_row += 1
    add.grid(row=current_row, column=0)
    calc_button.grid(row=current_row, column=1, columnspan=2)


def calculate():
    courses = []
    for row in rows:
        if row[0].get() and row[1].get() and row[2].get():
            courses.append(Course(row[0].get(), row[1].get(), row[2].get()))
    total_gpa = 0
    total_credits = 0
    for course in courses:
        total_gpa += course.gpa_value()
        total_credits += course.credits

    gpa = total_gpa / total_credits

    gpa_label = Label(root, text="You have a {}!".format(gpa))
    gpa_label.grid(row=1, column=3)


# Creating Objects
label1 = Label(root, text="Course Name")
label2 = Label(root, text="Grade")
label3 = Label(root, text="Credits")
add = Button(root, text="Add Course", fg="blue", command=add_row)
calc_button = Button(root, text="Calculate GPA", fg="green", command=calculate)

# Griding objects
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)


if __name__ == "__main__":
    add_row()
    root.mainloop()