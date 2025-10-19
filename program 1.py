from tkinter import*
root=Tk()
root.title("To-Do List")
root.geometry("400x600")
root.config(bg="light blue")
def add_task():
    task=entry.get()
    if add_task!="":
        listbox.insert(END, task) 
        entry.delete(0, End)
def delete_task():
    selected=listbox.curselection()
    if selected:
        listbox.delete(selected)
Label(root, text="My To-Do List",bg="#B88E23", font=("Arial",14,"bold")).pack(pady=10)  
entry = Entry(root, width=25)
entry.pack()
user_input=entry.get()
btn=Button(root, text="add task",bg="green", fg="white",command=add_task).pack(padx=5)
btn=Button(root,text="Delete task", bg="tomato",fg="white",command=delete_task).pack(pady=5
)
listbox = Listbox(root, width=30, height=15)
listbox.pack(pady=10)   
root.mainloop()


