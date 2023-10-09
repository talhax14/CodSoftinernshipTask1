"""Muhammad Talha"""

import tkinter as tk

#function to add task
def addTask():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

#function to remove task
def removeTask():
    selectedTask = task_listbox.curselection()
    if selectedTask:
        task_listbox.delete(selectedTask)

#function to edit selected task
def editTask():
    selectedTask = task_listbox.curselection()
    if selectedTask:
        editedTask = task_entry.get()
        if editedTask:
            task_listbox.delete(selectedTask)
            task_listbox.insert(selectedTask[0], editedTask)
            task_entry.delete(0, tk.END)

#creating the main window
root = tk.Tk()
root.title("To Do List")

#creating buttons
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add New Task", command=addTask)
remove_button = tk.Button(root, text="Remove Task", command=removeTask)
edit_button = tk.Button(root, text="Edit Task", command=editTask)

task_entry.pack(pady=20)
add_button.pack()
remove_button.pack()
edit_button.pack()

#configuring the list box
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack()

root.mainloop()
