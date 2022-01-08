import tkinter
from tkinter import *
from tkinter import ttk

import login
import workerApp
from queries import Query
import tkinter.messagebox as mb

label_font = ('Times New Roman', 10)

def log_out(window):
    window.destroy()
    login.logInForm()


def exit_click(window, user):
    q = Query()
    window.destroy()
    #director_app(q.getUserLoginByID(user.idUser))

def directorApp(login):
    window = tkinter.Tk()
    window.title("Добро пожаловать, босс!")
    window.geometry('1100x450')
    window['background'] = 'white'
    q = Query()
    idUser = q.getUserIdByLogin(login)
    user = q.getUserInfo(idUser)

    reg_dir_Label = Label(window, text='Директор, Темковый Альберт Аристархович', fg="black", bg="white")
    reg_dir_Label.grid(sticky="W", column=0, row=0)

#ПРОБЕЛЫ
    for i in range(1, 6, 2):
        for j in range(1, 10):
            if i == 1:
                space_i = Label(window, text='  ', fg='white', bg='white')
                space_i.grid(sticky='W', column=i, row=j)
            else:
                space_i = Label(window, text='          ..', fg='white', bg='white')
                space_i.grid(sticky='W', column=i, row=j)
#ВЫВОДЫ

    category_print_Label = Label(window, text='Просмотр', fg="black", bg="white")
    category_print_Label.grid(sticky="W", column=0, row=1)
    #кнопки
    print_client_button = Button(window, text='Вывод выбранного клиента',  width=30,
                            command=lambda: change_worker())
    print_client_button.grid(sticky="W", column=0, row=2)

    print_worker_button = Button(window, text='Вывод выбранного кладовщика',  width=30,
                            command=lambda: change_worker())
    print_worker_button.grid(sticky="W", column=0, row=3)

    print_order_button = Button(window, text='Вывод выбранного заказа',  width=30,
                            command=lambda: change_worker())
    print_order_button.grid(sticky="W", column=0, row=4)

    print_income_button = Button(window, text='Просмотр прибыли за период',  width=30,
                            command=lambda: change_worker())
    print_income_button.grid(sticky="W", column=0, row=5)
    print_top_button = Button(window, text='Вывод ключевых клиентов',  width=30,
                            command=lambda: change_worker())
    print_top_button.grid(sticky="W", column=0, row=6)
    print_prod_button = Button(window, text='Вывод всех товаров', width=30,
                              command=lambda: change_worker())
    print_prod_button.grid(sticky="W", column=0, row=7)


#ADD
    category_add_Label = Label(window, text='Добавление', fg="black", bg="white")
    category_add_Label.grid(sticky="W", column=2, row=1)
    #кнопки
    reg_work_button = Button(window, text='Регистрация кладовщика',  width=30,
                             command=lambda: reg_work())
    reg_work_button.grid(sticky="W", column=2, row=2)

    add_product_button = Button(window, text='Добавление нового товара',  width=30,
                            command=lambda: change_worker())
    add_product_button.grid(sticky="W", column=2, row=3)
    add_statusp_button = Button(window, text='Добавление нового cтатуса товара',  width=30,
                            command=lambda: change_worker())
    add_statusp_button.grid(sticky="W", column=2, row=4)
    add_statuso_button = Button(window, text='Добавление нового товара', width=30,
                                command=lambda: change_worker())
    add_statuso_button.grid(sticky="W", column=2, row=5)

#CHANGE
    category_change_Label = Label(window, text='Изменение', fg="black", bg="white")
    category_change_Label.grid(sticky="W", column=4, row=1)

    # кнопки

    change_work_button = Button(window, text='Изменение данных кладовщика',  width=30,
                            command=lambda: change_worker())
    change_work_button.grid(sticky="W", column=4, row=2)

    change_product_button = Button(window, text='Изменить товар',  width=30,
                            command=lambda: change_worker())
    change_product_button.grid(sticky="W", column=4, row=3)

    change_client_button = Button(window, text='Изменение данных клиента',  width=30,
                            command=lambda: change_worker())
    change_client_button.grid(sticky="W", column=4, row=4)

    change_statuso_button = Button(window, text='Изменение статуса заказа',  width=30,
                            command=lambda: change_worker())
    change_statuso_button.grid(sticky="W", column=4, row=5)

    change_statusp_button = Button(window, text='Изменение статуса товара',  width=30,
                            command=lambda: change_worker())
    change_statusp_button.grid(sticky="W", column=4, row=6)

#DELETE
    category_print_Label = Label(window, text='Удаление', fg="black", bg="white")
    category_print_Label.grid(sticky="W", column=6, row=1)
    # кнопки
    del_statusp_button = Button(window, text='Удаление статуса для продуктов',  width=30,
                            command=lambda: change_worker())
    del_statusp_button.grid(sticky="W", column=6, row=2)
    del_statuso_button = Button(window, text='Удаление статуса для заказов',  width=30,
                            command=lambda: change_worker())
    del_statuso_button.grid(sticky="W", column=6, row=3)
    del_order_button = Button(window, text='Удаление заказа',  width=30,
                            command=lambda: change_worker())
    del_order_button.grid(sticky="W", column=6, row=4)


    log_out_button = Button(window, text='Выход',
                             command=lambda: log_out(window))
    log_out_button.grid(sticky="W", column=0, row=19)

def change_worker():
    return 0

def reg_new_worker(window, login, password, full_name, phone_number, email):
    q=Query()
    conf = mb.askokcancel('Вы уверены, что запомнили введёные данные и регистрируетесь?') #переделать

    if conf and login != '' and password != '' and full_name != '' and phone_number != '' and email != '':
        try:
            q.register_worker(login, password, full_name, phone_number, email)
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg='black', bg='white')
            label.config(text='Регистрация прошла успешно')
            label.grid(column=1, row=100)
        except:
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg='black', bg='white')
            label.config(text='Что-то пошло не так при регистрации')
            label.grid(column=1, row=100)



def reg_work():
    window = Tk()
    window.title("Регистрация нового клиента")
    window.geometry('490x250')
    window['background'] = 'white'

    name_label = Label(window, text='Регистрация    ', font=label_font, fg="black",
                       bg="white")
    name_label.grid(column=0, row=0)
    name_label = Label(window, text='Имя', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=1, sticky='w')
    name_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    name_text.grid(column=1, row=1, sticky='w')

    phone_label = Label(window, text='Номер телефона', font=label_font, fg="black", bg="white")
    phone_label.grid(column=0, row=2, sticky='w')
    phone_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    phone_text.grid(column=1, row=2, sticky='w')

    q = Query()

    mail_label = Label(window, text='Эл.почта', font=label_font, fg="black", bg="white")
    mail_label.grid(column=0, row=3, sticky='w')
    mail_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    mail_text.grid(column=1, row=3, sticky='w')

    login_label = Label(window, text='Логин', font=label_font, fg="black", bg="white")
    login_label.grid(column=0, row=4, sticky='w')
    login_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    login_text.grid(column=1, row=4, sticky='w')

    pass_label = Label(window, text='Пароль', font=label_font, fg="black", bg="white")
    pass_label.grid(column=0, row=5, sticky='w')
    pass_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    pass_text.grid(column=1, row=5, sticky='w')

    confirm_button = Button(window, text='Подтвердить', fg="black", bg="white",
                            command=lambda: reg_new_worker(window, login_text.get(), pass_text.get(), name_text.get(),
                                                         phone_text.get(), mail_text.get()))
    confirm_button.grid(column=0, row=10, sticky='w')

    exit_button = Button(window, text='Выйти из меню регистрации', fg="black", bg="white",
                         command=lambda: exit_click(window))
    exit_button.grid(column=1, row=10, sticky='w')
    window.mainloop()

