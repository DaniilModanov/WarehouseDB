from tkinter import *
import tkinter.messagebox as mb

import login
from queries import *

label_font = ('Times New Roman', 10)

def show_catalog():
    q=Query()
    q.getCatalog()
    catWindow = Tk()
    catWindow.title("Каталог")
    catWindow.geometry('500x300')
    catWindow['background'] ='white'
    listbox = Listbox(catWindow)

    # Adding Listbox to the left
    # side of root window
    listbox.pack(side=LEFT, fill=BOTH)

    # Creating a Scrollbar and
    # attaching it to root window
    scrollbar = Scrollbar(catWindow)

    # Adding Scrollbar to the right
    # side of root window
    scrollbar.pack(side=RIGHT, fill=BOTH)

    products = q.getCatalog()

    for values in products:
        listbox.insert(END, values)

    listbox.config(yscrollcommand=scrollbar.set)

    scrollbar.config(command=listbox.yview)

    catWindow.mainloop()

def log_out(window):
    window.destroy()
    login.logInForm()

def confirm_change(window, user, name_text, date_text, phone_text, mail_text):
    q = Query()
    q.changeInfoOfUser(user.idLocal, name_text.get(), date_text.get(), phone_text.get(), mail_text.get() )
    conf = mb.askokcancel("Изменение данных", 'Вы уверены, что хотите изменить данные?')
    if conf:
        window.destroy()
        customerApp(q.getUserLoginByID(user.idUser))


def exit_click(window, user):
    q = Query()
    window.destroy()
    customerApp(q.getUserLoginByID(user.idUser))


def confirm_pass_change(pass_wind, user, old_pass, new_pass, confirm_pass):
    conf = mb.askokcancel("Изменение пароля", 'Вы уверены, что хотите изменить пароль?')
    if conf:
        q = Query()
        login = q.getUserLoginByID(user.idUser)
        ifPass = q.getPassword(login, old_pass.get())
        wrong_pass_label = Label(pass_wind, font=('Times New Roman', 10, 'bold'),
                                 fg="red", bg="white")
        if ifPass:
            if confirm_pass.get() != '' and new_pass.get() == confirm_pass.get():
                q.changePassword(user.idUser, new_pass.get())
                mb.showinfo('Изменение пароля', 'Пароль успешно изменен!')
                pass_wind.destroy()
            else:
                wrong_pass_label.config(text='Пароли не совпадают')
                wrong_pass_label.grid(column=0, row=10, sticky='w')
        else:
            wrong_pass_label.config(text='Неверный пароль      ')
            wrong_pass_label.grid(column=0, row=10, sticky='w')

def password_change(window, user):
    pass_wind = Toplevel()
    pass_wind.title('Изменение информации')
    pass_wind.geometry('450x350')
    pass_wind['background'] = 'white'
    pass_wind.grab_set()

    old_pass_label = Label(pass_wind, text='Старый пароль    ', font=label_font, fg="black", bg="white")
    old_pass_label.grid(column=0, row=0, sticky='w')
    old_pass = Entry(pass_wind, font=label_font, show='*', fg="black", bg="white", width=30)
    old_pass.grid(column=1, row=0, sticky='e')

    new_pass_label = Label(pass_wind, text='Новый пароль    ', font=label_font, fg="black", bg="white")
    new_pass_label.grid(column=0, row=1, sticky='w')
    new_pass = Entry(pass_wind, font=label_font, show='*', fg="black", bg="white", width=30)
    new_pass.grid(column=1, row=1, sticky='e')

    confirm_pass_label = Label(pass_wind, text='Подтвердите пароль    ', font=label_font, fg="black", bg="white")
    confirm_pass_label.grid(column=0, row=2, sticky='w')
    confirm_pass = Entry(pass_wind, font=label_font, show='*', fg="black", bg="white", width=30)
    confirm_pass.grid(column=1, row=2, sticky='e')

    exit_button = Button(pass_wind, text='Назад', fg="black", bg="white",
                         command=lambda: pass_wind.destroy())
    exit_button.grid(column=1, row=10, sticky='w')

    confirm_button = Button(pass_wind, text='Изменить пароль', fg="black", bg="white",
                            command=lambda: confirm_pass_change(pass_wind, user, old_pass, new_pass, confirm_pass))
    confirm_button.grid(column=1, row=10, sticky='e')

def change_info(window, user):
    window.destroy()
    window = Tk()
    window.title('Изменение информации')
    window.geometry('400x250')
    window['background'] = 'white'

    name_label = Label(window, text='Введите информацию, которую хотите изменить    ', font=label_font, fg="black",
                       bg="white")
    name_label.grid(column=0, row=0)
    name_label = Label(window, text='Имя', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=1, sticky='w')
    name_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    name_text.insert(1, user.name)
    name_text.grid(column=0, row=1, sticky='e')

    date_label = Label(window, text='Дата рождения', font=label_font, fg="black", bg="white")
    date_label.grid(column=0, row=2, sticky='w')
    date_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    date_text.insert(1, user.dateOfBrith)
    date_text.grid(column=0, row=2, sticky='e')

    phone_label = Label(window, text='Номер телефона', font=label_font, fg="black", bg="white")
    phone_label.grid(column=0, row=3, sticky='w')
    phone_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    phone_text.insert(1, user.phoneNumber)
    phone_text.grid(column=0, row=3, sticky='e')

    mail_label = Label(window, text='Эл.почта', font=label_font, fg="black", bg="white")
    mail_label.grid(column=0, row=4, sticky='w')
    mail_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    mail_text.insert(1, user.mail)
    mail_text.grid(column=0, row=4, sticky='e')

    confirm_button = Button(window, text='Подтвердить изменения', fg="black", bg="white",
                            command=lambda: confirm_change(window, user, name_text, date_text, phone_text, mail_text))
    confirm_button.grid(column=0, row=10, sticky='e')

    password_button = Button(window, text='Изменить пароль', fg="black", bg="white",
                             command=lambda: password_change(window, user))
    password_button.grid(column=0, row=10, sticky='w')

    exit_button = Button(window, text='Отмена', fg="black", bg="white",
                         command=lambda: exit_click(window, user))
    exit_button.grid(column=0, row=11, sticky='w')
    window.mainloop()



def customerApp(username):
    window = Tk()
    window.title("Добро пожаловать в ОАО Закупочки")
    window.geometry('745x500')
    window['background'] = 'white'
    q = Query()
    id_user = q.getUserIdByLogin(username)
    customer_info = q.getCustomerInfo(id_user)

    text = customer_info.full_name + '\n' + customer_info.phoneNumber + '\n' + customer_info.email
    info = Label(window, text=text, fg='black', bg='white') #, height=3, width=30

    info.configure(state='disable', anchor="w")
    info.grid(sticky="E", column=0, row=0)

#SPACE
    for i in range(1, 6, 2):
        for j in range(1, 10):
            if i == 1:
                space_i = Label(window, text='          ..', fg='white', bg='white')
                space_i.grid(sticky='W', column=i, row=j)
            else:
                space_i = Label(window, text='          ..', fg='white', bg='white')
                space_i.grid(sticky='W', column=i, row=j)
#ПРОСМОТР
    catalog_btn = Button(window, text='Посмотреть товары', fg="black", bg="white", width=30, command=lambda: show_catalog())
    catalog_btn.grid(sticky="W", column=0, row=1)
    class_book_button = Button(window, text='Посмотреть свои заказы', fg="black", bg="white", width=30)
    class_book_button.grid(sticky="W", column=0, row=2)
#ADD
    timetable_button = Button(window, text='Создать заказ', fg="black", bg="white", width=30,)
    timetable_button.grid(sticky="W", column=2, row=1)
#CHANGE
    grades_button = Button(window, text='Отменить заказ', fg="black", bg="white", width=30,)
    grades_button.grid(sticky="W", column=4, row=1)
    change_info_button = Button(window, text='Изменить данные', fg="black", bg="white", width=30,
                                command=lambda: change_info(window, username))
    change_info_button.grid(sticky="E", column=2, row=2)
#DELETE


    log_out_button = Button(window, text='Выйти', fg="black", bg="white", command=lambda: log_out(window))
    log_out_button.grid(sticky="W", column=0, row=4)


    window.mainloop()
