import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.config(bg="#f5f5f5")

# Task List
tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def mark_task_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        tasks[index] = f"✔ {tasks[index]}"
        update_task_list()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# GUI Elements
title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Helvetica", 14), width=25)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), bg="#4caf50", fg="white", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Helvetica", 14), width=30, height=15, bg="#ffffff", fg="#333", selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

mark_button = tk.Button(root, text="Mark Completed", font=("Helvetica", 12), bg="#2196f3", fg="white", command=mark_task_completed)
mark_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", font=("Helvetica", 12), bg="#f44336", fg="white", command=remove_task)
remove_button.pack(pady=5)

# Run the application
root.mainloop()
