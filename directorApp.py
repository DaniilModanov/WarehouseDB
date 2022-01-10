import tkinter
from tkinter import *
from tkinter import ttk
from tools import *
import login
import workerApp
from queries import Query
import tkinter.messagebox as mb

label_font = ('Times New Roman', 10)


def log_out(window):
    window.destroy()
    login.logInForm()


def exit_click(window):
    q = Query()
    window.destroy()

def search_worker(entry):
    if entry.get() != '':
        s = entry.get()
        q = Query()
        searchWindow = Tk()
        searchWindow.title("Наёденный работник")
        searchWindow['background'] = 'white'
        searchWindow.resizable(False, False)
        if has_dog(s) and has_letter(s) and has_point(s):
            worker_info, username = q.getWorkerByEmail(s)
            text = "Имя и Фамилия: " + worker_info.full_name + '\n' + 'телефон: ' + worker_info.phoneNumber + '\n' + \
                   'почта: ' + worker_info.email + '\n' + 'логин: ' + username + '\n' + 'userID: '+ str(worker_info.idUser) + \
                   '\n' + 'workerID: ' + str(worker_info.idWorker)
            search_lbl = Label(searchWindow, text=text, fg='black', bg='white')
            search_lbl.grid(column=0, row=0)
        if has_plus(s) and has_number(s) and has_letter(s) is not True:
            worker_info, username = q.getWorkerByPhone(s)
            text = "Имя и Фамилия: " + worker_info.full_name + '\n' + 'телефон: ' + worker_info.phoneNumber + '\n' +\
                   'почта: ' + worker_info.email + '\n' + 'логин: ' + username + '\n' + 'userID: '+ str(worker_info.idUser) + \
                   '\n' + 'workerID: ' + str(worker_info.idWorker)
            search_lbl = Label(searchWindow, text=text, fg='black', bg='white')
            search_lbl.grid(column=0, row=0)
    else:
        entry.insert(0, "Сперва введите данные")

def search_client(entry):
    if entry.get() != '':
        s = entry.get()
        q = Query()
        searchWindow = Tk()
        searchWindow.title("Наёденный клиент")
        searchWindow['background'] = 'white'
        searchWindow.resizable(False, False)
        if has_dog(s) and has_letter(s) and has_point(s):
            customer_info, username = q.getCustomerByEmail(s)
            text = "Имя и Фамилия: " + customer_info.full_name + '\n' + 'телефон: ' + customer_info.phoneNumber + '\n' + \
                   'почта: ' + customer_info.email + '\n' + 'логин: ' + username + '\n' + 'userID: '+ str(customer_info.idUser) + \
                   '\n' + 'customerID: ' + str(customer_info.idCustomer)
            search_lbl = Label(searchWindow, text=text, fg='black', bg='white')
            search_lbl.grid(column=0, row=0)
        if has_plus(s) and has_number(s) and has_letter(s) is not True:
            customer_info, username = q.getCustomerByPhone(s)
            text = "Имя и Фамилия: " + customer_info.full_name + '\n' + 'телефон: ' + customer_info.phoneNumber + '\n' +\
                   'почта: ' + customer_info.email + '\n' + 'логин: ' + username + '\n' + 'userID: '+ str(customer_info.idUser) + \
                   '\n' + 'customerID: ' + str(customer_info.idCustomer)
            search_lbl = Label(searchWindow, text=text, fg='black', bg='white')
            search_lbl.grid(column=0, row=0)
    else:
        entry.insert(0, "Сперва введите данные")


def out_client():
    outWindow = tkinter.Tk()
    outWindow.title("Поиск клиента")
    outWindow.geometry('400x200')
    outWindow['background'] = 'white'
    lbl_phone_email = Label(outWindow, text='Введите почту или номер телефона', fg='black', bg='white')
    lbl_phone_email.grid(column=0, row=0)
    ent_phone_email = Entry(outWindow)
    ent_phone_email.grid(column=0, row=1)
    search_btn = Button(outWindow, text='Поиск', fg='black', bg='white', command=lambda: search_client(ent_phone_email))
    search_btn.grid(column=0, row=2)


def out_worker():
    outWindow = tkinter.Tk()
    outWindow.title("Поиск работника")
    outWindow.geometry('400x200')
    outWindow['background'] = 'white'
    lbl_phone_email = Label(outWindow, text='Введите почту или номер телефона', fg='black', bg='white')
    lbl_phone_email.grid(column=0, row=0)
    ent_phone_email = Entry(outWindow)
    ent_phone_email.grid(column=0, row=1)
    search_btn = Button(outWindow, text='Поиск', fg='black', bg='white', command=lambda: search_worker(ent_phone_email))
    search_btn.grid(column=0, row=2)

def add_new_good(window, price, amount, name, description, status):
    q = Query()
    conf = mb.askokcancel('Вы уверены, что запомнили введёные данные и регистрируетесь?')  # переделать

    if conf and status.get() != '' and price.get() != '' and amount.get() != '' and name.get() != '' and description.get() != '' \
            and has_number(status.get()):
        try:
            q.addGood(name.get(), price.get(), status.get(), description.get(), amount.get())
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg='black', bg='white')
            label.config(text='Добавление товара прошло успешно')
            label.grid(column=1, row=100)
            name.delete(0, END)
            price.delete(0, END)
            description.delete(0, END)
            status.delete(0, END)
            amount.delete(0, END)

        except:
            label = Label(window, font=('Times New Roman', 10, 'bold'), fg='black', bg='white')
            label.config(text='Что-то пошло не так при добавлении товара')
            label.grid(column=0, row=100)

def new_good():
    window = Tk()
    window.title("Добавление нового товара")
    window.geometry('600x450')
    window['background'] = 'white'

    name_label = Label(window, text='Добавление товара в БД    ', font=label_font, fg="black",
                       bg="white")
    name_label.grid(column=0, row=0)
    name_label = Label(window, text='Название', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=1, sticky='w')
    name_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    name_text.grid(column=1, row=1, sticky='w')

    price_label = Label(window, text='Цена', font=label_font, fg="black", bg="white")
    price_label.grid(column=0, row=2, sticky='w')
    price_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    price_text.grid(column=1, row=2, sticky='w')

    status_label = Label(window, text='Статус (ID)', font=label_font, fg="black", bg="white")
    status_label.grid(column=0, row=3, sticky='w')
    status_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    status_text.grid(column=1, row=3, sticky='w')

    description_label = Label(window, text='Описание', font=label_font, fg="black", bg="white")
    description_label.grid(column=0, row=4, sticky='w')
    description_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    description_text.grid(column=1, row=4, sticky='w')

    amount_label = Label(window, text='Количество', font=label_font, fg="black", bg="white")
    amount_label.grid(column=0, row=5, sticky='w')
    amount_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    amount_text.grid(column=1, row=5, sticky='w')

    confirm_button = Button(window, text='Подтвердить', fg="black", bg="white",
                            command=lambda: add_new_good(window, price_text, amount_text, name_text,
                                                           description_text, status_text))
    confirm_button.grid(column=0, row=10, sticky='w')

    exit_button = Button(window, text='Выйти из меню добавления товара', fg="black", bg="white",
                         command=lambda: exit_click(window))
    exit_button.grid(column=0, row=11, sticky='w')

    query = Query()
    statuses = query.getProductStatuses()
    set = ttk.Treeview(window)
    set.grid(column=2, row=12)

    set['columns'] = ('ID Статуса', 'Название')
    set.column("#0", width=0, stretch=NO)
    set.column('ID Статуса', anchor=CENTER, width=80)
    set.column('Название', anchor=CENTER, width=80)

    set.heading("#0", text="", anchor=CENTER)
    set.heading('ID Статуса', text="ID Статуса", anchor=CENTER)
    set.heading("Название", text='Название', anchor=CENTER)

    for i in statuses:
        set.insert(parent='', index='end', iid=i, text='',
                   values=(i[0], i[1]))

    window.mainloop()


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

    # ПРОБЕЛЫ
    for i in range(1, 6, 2):
        for j in range(1, 10):
            if i == 1:
                space_i = Label(window, text='  ', fg='white', bg='white')
                space_i.grid(sticky='W', column=i, row=j)
            else:
                space_i = Label(window, text='          ..', fg='white', bg='white')
                space_i.grid(sticky='W', column=i, row=j)
    # ВЫВОДЫ

    category_print_Label = Label(window, text='Просмотр', fg="black", bg="white")
    category_print_Label.grid(sticky="W", column=0, row=1)
    # кнопки
    print_client_button = Button(window, text='Вывод выбранного клиента', width=30, fg="black", bg="white",
                                 command=lambda: out_client())
    print_client_button.grid(sticky="W", column=0, row=2)

    print_worker_button = Button(window, text='Вывод выбранного кладовщика', width=30, fg="black", bg="white",
                                 command=lambda: out_worker())
    print_worker_button.grid(sticky="W", column=0, row=3)

    print_order_button = Button(window, text='Вывод выбранного заказа', width=30, fg="black", bg="white",
                                command=lambda: change_worker())
    print_order_button.grid(sticky="W", column=0, row=4)

    print_income_button = Button(window, text='Просмотр прибыли за период', width=30, fg="black", bg="white",
                                 command=lambda: change_worker())
    print_income_button.grid(sticky="W", column=0, row=5)
    print_top_button = Button(window, text='Вывод ключевых клиентов', width=30, fg="black", bg="white",
                              command=lambda: change_worker())
    print_top_button.grid(sticky="W", column=0, row=6)
    print_prod_button = Button(window, text='Вывод всех товаров', width=30, fg="black", bg="white",
                               command=lambda: change_worker())
    print_prod_button.grid(sticky="W", column=0, row=7)

    # ADD
    category_add_Label = Label(window, text='Добавление', fg="black", bg="white")
    category_add_Label.grid(sticky="W", column=2, row=1)
    # кнопки
    reg_work_button = Button(window, text='Регистрация кладовщика', width=30, fg="black", bg="white",
                             command=lambda: reg_work())
    reg_work_button.grid(sticky="W", column=2, row=2)

    add_product_button = Button(window, text='Добавление нового товара', width=30, fg="black", bg="white",
                                command=lambda: new_good())
    add_product_button.grid(sticky="W", column=2, row=3)
    add_statusp_button = Button(window, text='Добавление нового cтатуса товара', width=30, fg="black", bg="white",
                                command=lambda: change_worker())
    add_statusp_button.grid(sticky="W", column=2, row=4)
    add_statuso_button = Button(window, text='Добавление нового статуса заказа', width=30, fg="black", bg="white",
                                command=lambda: change_worker())
    add_statuso_button.grid(sticky="W", column=2, row=5)

    # CHANGE
    category_change_Label = Label(window, text='Изменение', fg="black", bg="white")
    category_change_Label.grid(sticky="W", column=4, row=1)

    # кнопки

    change_work_button = Button(window, text='Изменение данных кладовщика', width=30, fg="black", bg="white",
                                command=lambda: change_worker())
    change_work_button.grid(sticky="W", column=4, row=2)

    change_product_button = Button(window, text='Изменить товар', width=30, fg="black", bg="white",
                                   command=lambda: change_good())
    change_product_button.grid(sticky="W", column=4, row=3)

    change_client_button = Button(window, text='Изменение данных клиента', width=30, fg="black", bg="white",
                                  command=lambda: change_worker())
    change_client_button.grid(sticky="W", column=4, row=4)

    change_statuso_button = Button(window, text='Изменение статуса заказа', width=30, fg="black", bg="white",
                                   command=lambda: change_worker())
    change_statuso_button.grid(sticky="W", column=4, row=5)

    change_statusp_button = Button(window, text='Изменение статуса товара', width=30, fg="black", bg="white",
                                   command=lambda: change_worker())
    change_statusp_button.grid(sticky="W", column=4, row=6)

    # DELETE
    category_print_Label = Label(window, text='Удаление', fg="black", bg="white")
    category_print_Label.grid(sticky="W", column=6, row=1)
    # кнопки
    del_statusp_button = Button(window, text='Удаление статуса для продуктов', width=30, fg="black", bg="white",
                                command=lambda: change_worker())
    del_statusp_button.grid(sticky="W", column=6, row=2)
    del_statuso_button = Button(window, text='Удаление статуса для заказов', width=30, fg="black", bg="white",
                                command=lambda: change_worker())
    del_statuso_button.grid(sticky="W", column=6, row=3)
    del_order_button = Button(window, text='Удаление заказа', width=30, fg="black", bg="white",
                              command=lambda: change_worker())
    del_order_button.grid(sticky="W", column=6, row=4)

    log_out_button = Button(window, text='Выход',
                            command=lambda: log_out(window))
    log_out_button.grid(sticky="W", column=0, row=19)

def change_good():
    window = Tk()
    window.title("Изменение товара")
    window.geometry('600x450')
    window['background'] = 'white'

    name_label = Label(window, text='Добавление товара в БД    ', font=label_font, fg="black",
                       bg="white")
    name_label.grid(column=0, row=0)
    name_label = Label(window, text='Название', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=1, sticky='w')
    name_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    name_text.grid(column=1, row=1, sticky='w')

    id_label = Label(window, text='ID Товара', font=label_font, fg="black", bg="white")
    id_label.grid(column=0, row=2, sticky='w')
    id_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    id_text.grid(column=1, row=2, sticky='w')

    price_label = Label(window, text='Цена', font=label_font, fg="black", bg="white")
    price_label.grid(column=0, row=3, sticky='w')
    price_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    price_text.grid(column=1, row=3, sticky='w')

    status_label = Label(window, text='Статус (ID)', font=label_font, fg="black", bg="white")
    status_label.grid(column=0, row=4, sticky='w')
    status_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    status_text.grid(column=1, row=4, sticky='w')

    description_label = Label(window, text='Описание', font=label_font, fg="black", bg="white")
    description_label.grid(column=0, row=5, sticky='w')
    description_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    description_text.grid(column=1, row=5, sticky='w')

    amount_label = Label(window, text='Количество', font=label_font, fg="black", bg="white")
    amount_label.grid(column=0, row=6, sticky='w')
    amount_text = Entry(window, font=label_font, fg="black", bg="white", width=30)
    amount_text.grid(column=1, row=6, sticky='w')

    confirm_button = Button(window, text='Подтвердить', fg="black", bg="white",
                            command=lambda: edit_good(window,id_text, price_text, amount_text, name_text,
                                                         description_text, status_text))
    confirm_button.grid(column=0, row=10, sticky='w')

    exit_button = Button(window, text='Выйти из меню изменения товара', fg="black", bg="white",
                         command=lambda: exit_click(window))
    exit_button.grid(column=0, row=11, sticky='w')

    query = Query()
    statuses = query.getProductStatuses()
    set = ttk.Treeview(window)
    set.grid(column=2, row=12)

    set['columns'] = ('ID Статуса', 'Название')
    set.column("#0", width=0, stretch=NO)
    set.column('ID Статуса', anchor=CENTER, width=80)
    set.column('Название', anchor=CENTER, width=80)

    set.heading("#0", text="", anchor=CENTER)
    set.heading('ID Статуса', text="ID Статуса", anchor=CENTER)
    set.heading("Название", text='Название', anchor=CENTER)

    for i in statuses:
        set.insert(parent='', index='end', iid=i, text='',
                   values=(i[0], i[1]))

    window.mainloop()

def edit_good(window,id, price, amount, name, description, status):
    q = Query()
    conf = mb.askokcancel('Вы уверены, что запомнили введёные данные и регистрируетесь?')  # переделать

    if conf and id.get() != '' and has_number(id.get()):
        q.editGood(id.get(), name.get(), price.get(), status.get(), description.get(), amount.get())
        label = Label(window, font=('Times New Roman', 10, 'bold'), fg='black', bg='white')
        label.config(text='Изменение товара прошло успешно')
        label.grid(column=1, row=100)
        name.delete(0, END)
        price.delete(0, END)
        description.delete(0, END)
        status.delete(0, END)
        amount.delete(0, END)

        # except:
        #     label = Label(window, font=('Times New Roman', 10, 'bold'), fg='black', bg='white')
        #     label.config(text='Что-то пошло не так при изменении товара')
        #     label.grid(column=0, row=100)

def change_worker():
    return 0


def reg_new_worker(window, login, password, full_name, phone_number, email):
    q = Query()
    conf = mb.askokcancel('Вы уверены, что запомнили введёные данные и регистрируетесь?')  # переделать

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
