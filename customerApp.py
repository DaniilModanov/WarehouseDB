import tkinter
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from datetime import datetime

import login
from queries import *

label_font = ('Times New Roman', 10)

def make_order():
    q = Query()
    orderWindow = Tk()
    orderWindow.title("Создание заказа")
    orderWindow.geometry('550x400')
    orderWindow['background'] = 'white'
    name_label = Label(orderWindow, text='Введите информацию, которую хотите изменить    ', font=label_font, fg="black",
                       bg="white")
    name_label.grid(column=0, row=0)
    name_label = Label(orderWindow, text='Название товара', font=label_font, fg="black", bg="white")
    name_label.grid(column=0, row=1, sticky='w')
    name_text = Entry(orderWindow, font=label_font, fg="black", bg="white", width=30)
    name_text.grid(column=0, row=1, sticky='e')

    date_label = Label(orderWindow, text='', font=label_font, fg="black", bg="white")
    date_label.grid(column=0, row=2, sticky='w')
    date_text = Entry(orderWindow, font=label_font, fg="black", bg="white", width=30)
    date_text.grid(column=0, row=2, sticky='e')

    phone_label = Label(orderWindow, text='Номер телефона', font=label_font, fg="black", bg="white")
    phone_label.grid(column=0, row=3, sticky='w')
    phone_text = Entry(orderWindow, font=label_font, fg="black", bg="white", width=30)
    phone_text.grid(column=0, row=3, sticky='e')

    mail_label = Label(orderWindow, text='Эл.почта', font=label_font, fg="black", bg="white")
    mail_label.grid(column=0, row=4, sticky='w')
    mail_text = Entry(orderWindow, font=label_font, fg="black", bg="white", width=30)
    mail_text.grid(column=0, row=4, sticky='e')

    confirm_button = Button(orderWindow, text='Подтвердить и отправить в корзину', fg="black", bg="white")
    confirm_button.grid(column=0, row=10, sticky='e')

    exit_button = Button(orderWindow, text='Отмена', fg="black", bg="white")
    exit_button.grid(column=0, row=11, sticky='w')
    orderWindow.mainloop()

def show_cart(cart, username, window):
    window.destroy()
    cartWindow = Tk()
    cartWindow.title("Корзина")
    cartWindow.geometry('600x400')
    cartWindow['background'] = 'white'
    s_cart = ''
    for value in cart:
        s_cart += value.to_string_wl() + '\n'
    order_lbl = Label(cartWindow, text=s_cart, fg='black', bg='white')
    order_lbl.grid(column=0, row=0)

    address_ent = Entry(cartWindow, font=label_font, fg="black", bg="white", width=30)
    address_ent.grid(column=0, row=1)

    buy_btn = Button(cartWindow, text="Оформить заказ", fg='black', bg='white')
    buy_btn.grid(column=0, row=2)

    deny_btn = Button(cartWindow, text="Отменить и оставить заказ в корзине", fg='black', bg='white')
    deny_btn.grid(column=0, row=3)


def show_top_of_catalog():
    q = Query()

    catWindow = Tk()
    catWindow.title("Каталог")
    catWindow.geometry('550x400')
    catWindow['background'] = 'white'

    set = ttk.Treeview(catWindow)
    set.pack()

    set['columns'] = ('Name', 'Description', 'Availability', 'Price')
    set.column("#0", width=0, stretch=NO)
    set.column("Name", anchor=CENTER, width=80)
    set.column("Description", anchor=CENTER, width=300)
    set.column("Availability", anchor=CENTER, width=80)
    set.column("Price", anchor=CENTER, width=80)

    set.heading("#0", text="", anchor=CENTER)
    set.heading("Name", text="Name", anchor=CENTER)
    set.heading("Description", text="Description", anchor=CENTER)
    set.heading("Availability", text="Availability", anchor=CENTER)
    set.heading("Price", text="Price", anchor=CENTER)

    statuses = q.getProductStatuses()
    products = q.getTopProducts()

    for i in range(len(products)):
        status_i = ""
        for j in range(len(statuses)):
            if products[i][3] == statuses[j][0]:
                status_i = statuses[j][1]
        price_i = products[i][2]

        if status_i != "":
            set.insert(parent='', index='end', iid=i, text='',
                       values=(products[i][1], products[i][4], status_i, price_i))

def add_item(box, catalog, wishlist, wishlist_box):
    if box.curselection() != ():
        select = box.curselection()[0]
        if catalog[select].quantity < catalog[select].available:

            if catalog[select].quantity > 0:
                catalog[select].add_one()
                # wishlist[catalog[select].index] = catalog[select]
                # ind_wl = wishlist.index(catalog[select])
                # wishlist.append(catalog[select])
                s_temp = wishlist[len(wishlist) - 1].to_string()
                wishlist_box.insert(END, s_temp)
            else:
                catalog[select].add_one()
                wishlist.append(catalog[select])
                s_temp = wishlist[len(wishlist) - 1].to_string()
                wishlist_box.insert(END, s_temp)

        else:
            print("больше этого товара нет") #cделать вывод в label



def show_descr(box, description_text, catalog):
    if box.curselection() != ():
        select = box.curselection()[0]

        tempText = "Описание: " + str(catalog[select].description)
        description_text['text'] = tempText



def add_to_cart(box, wishlist, username, window):
    cart = wishlist
    show_cart(cart, username, window)
    # query.cursor.execute(f"MAKE_ORDER") # через queries.py делай
    print(box)
    for val in wishlist:
        print(val.name)



def show_catalog_lb(username):
    wishlist = []
    cart = Cart()
    q=Query()
    catWindow = Tk()
    catWindow.title("Каталог")
    catWindow.geometry('550x400')
    catWindow['background'] ='white'
    box = Listbox(catWindow, width=40, height=10)

    box.grid(row=0, column=0)
    scroll = Scrollbar(catWindow, command=box.yview)
    scroll.grid(row=0, column=2)
    box.config(yscrollcommand=scroll.set)

    wishbox = Listbox(catWindow, width=40, height=10)
    wishbox.grid(row=0, column=5)
    wishscroll = Scrollbar(catWindow, command=box.yview)
    wishscroll.grid(row=0, column=6)
    wishbox.config(yscrollcommand=wishscroll.set)



    catalog = q.getCatalog()
    for value in catalog:
        temp = value.to_string()
        box.insert(END, temp)

    # description_text = tkinter.StringVar(catWindow)
    # description_text.set('Описание: Выберите товар')
    # description = Label(catWindow, text=description_text, font=label_font, fg='black', bg='white')
    # description.grid(row=0, column=4)
    description = Label(catWindow, text="Описание:")
    description.grid(row=2, column=0)

    add_btn = Button(catWindow, text="Add to wishlist", command=lambda: add_item(box, catalog, wishlist, wishbox))
    add_btn.grid(row=0, column=3)
    description_btn = Button(catWindow, text="Show description", command=lambda: show_descr(box, description, catalog))
    description_btn.grid(row=1, column=3)
    cart_btn = Button(catWindow, text="Add to cart", command=lambda: add_to_cart(box, wishlist, username, catWindow))
    cart_btn.grid(row=2, column=3)
    catWindow.mainloop()


def show_catalog():
    q=Query()

    catWindow = Tk()
    catWindow.title("Каталог")
    catWindow.geometry('550x400')
    catWindow['background'] ='white'

    set = ttk.Treeview(catWindow)
    set.pack()

    set['columns'] = ('Name', 'Description', 'Availability', 'Price')
    set.column("#0", width=0, stretch=NO)
    set.column("Name", anchor=CENTER, width=80)
    set.column("Description", anchor=CENTER, width=300)
    set.column("Availability", anchor=CENTER, width=80)
    set.column("Price", anchor=CENTER, width=80)

    set.heading("#0", text="", anchor=CENTER)
    set.heading("Name", text="Name", anchor=CENTER)
    set.heading("Description", text="Description", anchor=CENTER)
    set.heading("Availability", text="Availability", anchor=CENTER)
    set.heading("Price", text="Price", anchor=CENTER)




    statuses = q.getProductStatuses()
    products = q.getCatalog()

    for i in range(len(products)):
        status_i = ""
        for j in range(len(statuses)):
            if products[i][3] == statuses[j][0]:
                status_i = statuses[j][1]
        price_i = products[i][2]

        if status_i != "":
            set.insert(parent='', index='end', iid=i, text='',
                   values=(products[i][1], products[i][4], status_i, price_i))


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
    catalog_btn = Button(window, text='Посмотреть товары', fg="black", bg="white", width=30, command=lambda: show_catalog_lb(username))
    catalog_btn.grid(sticky="W", column=0, row=1)
    class_book_button = Button(window, text='Посмотреть свои заказы', fg="black", bg="white", width=30)
    class_book_button.grid(sticky="W", column=0, row=2)
    catalog_btn = Button(window, text='Посмотреть популярные товары', fg="black", bg="white", width=30,
                         command=lambda: show_catalog())
    catalog_btn.grid(sticky="W", column=0, row=3)
#ADD
    timetable_button = Button(window, text='Создать заказ', fg="black", bg="white", width=30,)
    timetable_button.grid(sticky="W", column=2, row=1)
#CHANGE
    grades_button = Button(window, text='Отменить заказ', fg="black", bg="white", width=30,)
    grades_button.grid(sticky="W", column=4, row=1)
    change_info_button = Button(window, text='Изменить данные', fg="black", bg="white", width=30,
                                command=lambda: change_info(window, username))
    change_info_button.grid(sticky="E", column=4, row=2)

    log_out_button = Button(window, text='Выйти', fg="black", bg="white", command=lambda: log_out(window))
    log_out_button.grid(sticky="W", column=0, row=4)

    cart_button = Button(window, text='Корзина', fg="black", bg="white", command=lambda: cart(username))
    log_out_button.grid(sticky="W", column=0, row=4)

    window.mainloop()

def cart(username):
    cartWindow = Tk()

