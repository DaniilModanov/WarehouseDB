from tkinter import *
import login
from queries import *
import tkinter.messagebox as mb

def log_out(window):
    window.destroy()
    login.logInForm()

def workerApp(login):
    window = Tk()
    window.title("Добро пожаловать в ОАО Закупочки, работая у нас вы строите общее будущее!")
    window.geometry('545x350')
    window['background'] = 'white'
    q = Query()
    id_user = q.getUserIdByLogin(login)
    customer_info = q.getUserInfo(id_user)

    text = customer_info.full_name + '\n' + customer_info.phoneNumber + '\n' + customer_info.email
    info = Label(window, text=text, fg='black', bg='white')

    info.configure(state='disable', anchor="w")
    info.grid(sticky="E", column=0, row=0)
#SPACES
    for i in range(1, 10):
        space_i = Label(window, text='    ', fg='white', bg='white')
        space_i.grid(sticky='W', column=2, row=i)
#ВЫВОД
    catalog_btn = Button(window, text='Посмотреть товары', fg="black", bg="white", width=30, command=lambda: show_catalog())
    catalog_btn.grid(sticky="W", column=0, row=1)
    class_book_button = Button(window, text='Посмотреть свои заказы', fg="black", bg="white", width=30)
    class_book_button.grid(sticky="W", column=0, row=2)
    class_book_button = Button(window, text='Посмотр информации заказа', fg="black", bg="white", width=30)
    class_book_button.grid(sticky="W", column=0, row=3)

#CHANGE
    catalog_btn = Button(window, text='Изменить количество товаров', fg="black", bg="white", width=30, command=lambda: show_catalog())
    catalog_btn.grid(sticky="W", column=3, row=1)
    catalog_btn = Button(window, text='Обработка заказа', fg="black", bg="white", width=30, command=lambda: show_catalog())
    catalog_btn.grid(sticky="W", column=3, row=2)
    catalog_btn = Button(window, text='Изменить статус товара', fg="black", bg="white", width=30, command=lambda: show_catalog())
    catalog_btn.grid(sticky="W", column=3, row=3)


    space_i = Label(window, text='  ', fg='white', bg='white')
    space_i.grid(sticky='W', column=1, row=0)
    log_out_button = Button(window, text='Выйти', fg="black", bg="white", command=lambda: log_out(window))
    log_out_button.grid(sticky="W", column=2, row=0)

    window.mainloop()

def show_catalog():
    return 0