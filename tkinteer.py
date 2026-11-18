from tkinter import *

def add_task():
    global count
    count += 1
    task_name = entry_name.get()
    task_days = entry_days.get()
    label_result["text"] = f"Задач добавлено: {count}\nПоследняя: {task_name} ({task_days} дн.)"

def clear_fields():
    entry_name.delete(0, END)
    entry_days.delete(0, END)

root = Tk()
root.title("Планировщик задач")
root.geometry("460x520")

count = 0

img = PhotoImage(file="task-planner-banner.png")
label_img = Label(root, image=img)
label_img.pack()


label_name = Label(root, text="Название задачи")
label_name.pack()
entry_name = Entry(root, width=40)
entry_name.pack()

label_days = Label(root, text="Длительность (дней)")
label_days.pack()
entry_days = Entry(root, width=40)
entry_days.pack()

btn_add = Button(root, text="Добавить задачу", command=add_task)
btn_add.pack()

btn_clear = Button(root, text="Очистить поля", command=clear_fields)
btn_clear.pack()

label_result = Label(root, text="Задач добавлено: 0")
label_result.pack()

root.mainloop()