from tkinter import *

import directorApp
import workerApp
import customerApp
import regWindow
import workerApp
from queries import *

def logInForm():
    window = Tk()
    window.title('Авторизация')
    window.geometry('450x450')
    window.resizable(False, False)
    window['background'] = 'white'
    q = Query()
    font_header = ('Times New Roman', 15, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    def logInUser():

        username = username_entry.get()
        password = password_entry.get()

        if username != '' or password != '':
            if q.getLogin(username) and q.getPassword(username, password):
                window.destroy()
                idUser = q.getUserIdByLogin(username)
                user = q.getUserProfile(idUser)
                if user == 'Кладовщик':
                    workerApp.workerApp(username)
                elif user == 'Покупатель':
                    customerApp.customerApp(username)
                elif user == 'Директор':
                    directorApp.directorApp(username)

            else:
                wrong_password_label = Label(window, text='Неправильный логин или пароль', font=label_font, **base_padding, foreground='red')
                wrong_password_label['background'] = 'white'
                wrong_password_label.pack()

    def signUpCustomer():
        regWindow.reg_cus()



    main_label = Label(window, text='Вход в приложение ОАО Закупочки', font=font_header, justify=CENTER, **header_padding)
    main_label['background'] = 'white'
    main_label.pack()
    username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
    username_label['background'] = 'white'
    username_label.pack()

    # поле ввода имени
    username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    # метка для поля ввода пароля
    password_label = Label(window, text='Пароль', font=label_font , **base_padding)
    password_label['background'] = 'white'
    password_label.pack()

    # поле ввода пароля
    password_entry = Entry(window, bg='#fff', fg='#444',show='*', font=font_entry)
    password_entry.pack()

    # кнопка отправки формы
    send_btn = Button(window, text='Войти', command=logInUser, font=button_font, foreground='black')
    send_btn.pack(**base_padding)

    reg_label = Label(window, text='Ещё не зарегистрированы в нашем приложении?', font=label_font, **base_padding)
    reg_label['background'] = 'white'
    reg_label.pack()

    reg_btn = Button(window, text='Зарегистрироваться', command=signUpCustomer)
    reg_btn.pack(**base_padding)

    window.mainloop()

