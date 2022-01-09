status = ['Директор', 'Работник', 'Покупатель']

def has_number(inputString):
    return any(char.isdigit() for char in inputString)

def has_letter(inputString):
    return any(char.isalpha() for char in inputString)
def has_point(inputString):
    return any(char == '.' for char in inputString)

class User:
    def __init__(self, idUser, status,idLocal = None):
        self.idUser = idUser
        self.idLocal = idLocal


class Worker(User):
    def __init__(self, idUser, idLocal, name, phoneNumber, email, idWorker):
        super().__init__(idUser, status)
        self.full_name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.idWorker = idWorker

class Customer(User):
    def __init__(self, idUser, name, phoneNumber, email, idCustomer):
        super().__init__(idUser, status)
        self.full_name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.idCustomer = idCustomer
    def to_string(self):
        return self.full_name + ' ' + self.email + ' ' + self.phoneNumber


class Cart:
    def __init__(self):
        self.product_list = []

    def addToCart(self, product):
        self.product_list.append(product)


class Product:
    def __init__(self, id_product, name, price, status_product, description, available):
        self.id = id_product
        self.name = name
        self.price = price
        self.status = status_product
        self.description = description
        self.available = available
        self.quantity = 0
    def to_string(self):
        temp_money = str(self.price)
        temp_money = temp_money[:-2]
        return str(self.name) + ' ' + temp_money

    def to_string_wl(self):
        temp_money = str(self.price)
        temp_money = temp_money[:-2]
        return str(self.name) + ' ' + temp_money + ' ' + str(self.quantity)

    def add_one(self):
        self.quantity += 1

    def remove_one(self):
        if self.quantity > 0:
            self.quantity -= 1
            return False
        else:
            return True

class Order:
    def __init__(self, id_order, customer_id, worker_id, status, created_at, client_address, total_price):
        self.id = id_order
        self.customer_id = customer_id
        self.worker_id = worker_id
        self.status = status
        self.created_at = created_at
        self.client_address = client_address
        self.total_price = total_price

    def to_string(self):
        return "Заказ номер №" + str(self.id) + " Cоздан: " + self.created_at + \
               " Адрес: " + self.client_address + " Итого: " + self.total_price
