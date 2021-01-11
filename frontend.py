from tkinter import *
import backend
from datetime import datetime as dt


def get_selected_row(event):
    global selected_row
    index = listbox.curselection()[0]
    selected_row = listbox.get(index)

    regEntry.delete(0, END)
    regEntry.insert(END, selected_row[0])
    dateEntry.delete(0, END)
    dateEntry.insert(END, selected_row[1])
    # catEntry.delete(0, END)
    # catEntry.insert(END, selected_row[2])
    studentCat.set(" ")
    studentCat.set(selected_row[2])

    nameEntry.delete(0, END)
    nameEntry.insert(END, selected_row[3])

    DegreeEntry.delete(0, END)
    DegreeEntry.insert(END, selected_row[4])

    depEntry.delete(0, END)
    depEntry.insert(END, selected_row[5])
    # statusEntry.delete(0, END)
    # statusEntry.insert(END, selected_row[6])
    studentStatus.set(" ")
    studentStatus.set(selected_row[6])

    durEntry.delete(0, END)
    durEntry.insert(END, selected_row[7])


def refresh_command():
    regEntry.delete(0, END)

    dateEntry.delete(0, END)

    # catEntry.delete(0, END)
    studentCat.set(" ")

    nameEntry.delete(0, END)

    DegreeEntry.delete(0, END)

    depEntry.delete(0, END)

    # statusEntry.delete(0, END)
    studentStatus.set(" ")

    durEntry.delete(0, END)

    view_command()


def delete_command():
    backend.delete(selected_row[0])
    refresh_command()
    view_command()


def view_command():
    listbox.delete(0, END)
    for rows in backend.view():
        listbox.insert(END, rows)


def search_command():
    listbox.delete(0, END)
    for row in backend.search(studentReg.get(), studentDate.get(), studentCat.get(), studentName.get(), studentDegree.get(), studentDepartment.get(), studentStatus.get(), studentDuration.get()):
        listbox.insert(END, row)


def add_command():
    backend.insert_table(studentReg.get(), studentDate.get(), studentCat.get(), studentName.get(),
                              studentDegree.get(), studentDepartment.get(), studentStatus.get(), studentDuration.get())

    listbox.delete(0, END)
    listbox.insert(END, (studentReg.get(), studentDate.get(), studentCat.get(), studentName.get(),
                              studentDegree.get(), studentDepartment.get(), studentStatus.get(), studentDuration.get()))

    refresh_command()


root = Tk()
root.title('University Database')
root.config(bg='light grey')

# LABELS

name_label = Label(root, text='Name:', fg='black', bg='light grey')
name_label.grid(row=0, column=0)

reg_label = Label(root, text='RegNumber:', fg='black', bg='light grey')
reg_label.grid(row=0, column=2)

degree_label = Label(root, text='Degree:', fg='black', bg='light grey')
degree_label.grid(row=1, column=0)

dep_label = Label(root, text='Department:', font=('Courier', 10), fg='black', bg='light grey')
dep_label.grid(row=1, column=2)

status_label = Label(root, text='Status:', font=('Courier', 10), fg='black', bg='light grey')
status_label.grid(row=2, column=0)

cat_label = Label(root, text='Category:', font=('Courier', 10), fg='black', bg='light grey')
cat_label.grid(row=2, column=2)

date_label = Label(root, text='RegDate:', font=('Courier', 10), fg='black', bg='light grey')
date_label.grid(row=3, column=0)

period_label = Label(root, text='Duration :', font=('Courier', 10), fg='black', bg='light grey')
period_label.grid(row=3, column=2)


# ENTRIES

studentName = StringVar()
nameEntry = Entry(root, textvariable=studentName)
nameEntry.grid(row=0, column=1)

studentReg = StringVar()
regEntry = Entry(root, textvariable=studentReg)
regEntry.grid(row=0, column=3)

studentDegree = StringVar()
DegreeEntry = Entry(root, textvariable=studentDegree)
DegreeEntry.grid(row=1, column=1)

studentDepartment = StringVar()
depEntry = Entry(root, textvariable=studentDepartment)
depEntry.grid(row=1, column=3)

studentStatus = StringVar()
statusEntry = OptionMenu(root, studentStatus, "Graduated", "Studying")
statusEntry.grid(row=2, column=1)

# statusEntry = Entry(root, textvariable=studentStatus)
# statusEntry.grid(row=2, column=1)

studentCat = StringVar()
catEntry = OptionMenu(root, studentCat, "NS", "PC", "GC")
catEntry.grid(row=2, column=3)

# catEntry = Entry(root, textvariable=studentCat)
# catEntry.grid(row=2, column=3)

studentDate = StringVar()
dateEntry = Entry(root, textvariable=studentDate)
dateEntry.grid(row=3, column=1)

studentDuration = StringVar()
durEntry = Entry(root, textvariable=studentDuration)
durEntry.grid(row=3, column=3)


# button

add_button = Button(root, text='Add', width=10, pady=5, command=add_command)
add_button.grid(row=4, column=3)
search_button = Button(root, text='Search', width=10, pady=5, command=search_command)
search_button.grid(row=5, column=3)
delete_button = Button(root, text='Delete Data', width=10, pady=5, command=delete_command)
delete_button.grid(row=6, column=3)
view_button = Button(root, text='View All', width=10, pady=5, command=view_command)
view_button.grid(row=7, column=3)
refresh_button = Button(root, text='Refresh', width=10, pady=5, command=refresh_command)
refresh_button.grid(row=8, column=3)
close_button = Button(root, text='Close', width=10, pady=5, command=quit)
close_button.grid(row=9, column=3)

# Listbox

listbox = Listbox(root, height=8, width=35)
listbox.grid(row=4, column=0, rowspan=9, columnspan=2)

# Scroll button
scrollbar = Scrollbar(root)
scrollbar.grid(row=4, column=2, rowspan=9)

listbox.bind('<<ListboxSelect>>', get_selected_row)


root.mainloop()
