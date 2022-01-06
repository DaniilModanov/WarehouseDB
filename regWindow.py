from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
from queries import Query
label_font = ('Times New Roman', 10)

def exit_click(window):
    window.destroy()

def reg_customer(window, login, password, full_name, phone_number, email):
    q=Query()
    conf = mb.askokcancel('Вы уверены, что запомнили введёные данные и регистрируетесь?') #переделать

    if conf and login != '' and password != '' and full_name != '' and phone_number != '' and email != '':
        try:
            q.register_customer(login, password, full_name, phone_number, email)
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg='black', bg='white')
            label.config(text='Регистрация прошла успешно')
            label.grid(column=1, row=100)
        except:
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg='black', bg='white')
            label.config(text='Что-то пошло не так при регистрации')
            label.grid(column=1, row=100)


def reg_cus():
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
                            command=lambda: reg_customer(window, login_text.get(), pass_text.get(), name_text.get(), phone_text.get(), mail_text.get()))
    confirm_button.grid(column=0, row=10, sticky='w')

    exit_button = Button(window, text='Выйти из меню регистрации', fg="black", bg="white",
                         command=lambda: exit_click(window))
    exit_button.grid(column=1, row=10, sticky='w')
    window.mainloop()
