from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
file_name= NONE

def new_file():
    global file_name
    file_name="Не названый."
    text.delete('1.0', END)

def save_file():
    out=asksaveasfile(mode='w', defaultextension='.txt')
    data=text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception: 
        messagebox.showerror("ОШИБКА!", "Сохранение файла невозможно")
def file_open():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return 
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

root = Tk()
root.title("Программа заметок")
root.geometry("300x400")
text = Text(root, width=300, height=400)
text.pack()


menu_bar = Menu(root)
file_menu = Menu(menu_bar)

file_menu.add_command(label="Новый файл", command=new_file)
file_menu.add_command(label="Открыть", command=file_open)
file_menu.add_command(label="Сохранить файл", command=save_file)
menu_bar.add_cascade(label="Файлик", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()