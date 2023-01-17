import tkinter, pickle
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-Do List by Jonathan")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task...")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task...")

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="No data files found for the tasks...")

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

scrollbar_tasks.config(command = listbox_tasks.yview)
listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)

entry_task = tkinter.Entry(root, width=52)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add Task", width=10, command=add_task)
button_add_task.pack(side=tkinter.LEFT)

button_delete_task = tkinter.Button(root, text="Delete Task", width=10, command=delete_task)
button_delete_task.pack(side=tkinter.LEFT)

button_load_tasks = tkinter.Button(root, text="Load Task(s)", width=10, command=load_task)
button_load_tasks.pack(side=tkinter.LEFT)

button_save_tasks = tkinter.Button(root, text="Save Task(s)", width=10, command=save_task)
button_save_tasks.pack(side=tkinter.LEFT)

root.mainloop()
