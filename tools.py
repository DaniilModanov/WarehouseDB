status = ['Директор', 'Работник', 'Покупатель']

class User:
    def __init__(self, idUser, status,idLocal = None):
        self.idUser = idUser
        self.idLocal = idLocal


class Worker(User):
    def __init__(self, idUser, idLocal, name, phoneNumber, email):
        super().__init__(idUser, status)
        self.full_name = name
        self.email = email
        self.phoneNumber = phoneNumber

class Customer(User):
    def __init__(self, idUser, name, phoneNumber, email):
        super().__init__(idUser, status)
        self.full_name = name
        self.email = email
        self.phoneNumber = phoneNumber


class Cart:
    def __init__(self):
        self.product_list = []

    def addToCart(self, product):
        self.product_list.append(product)


class Product:
    def __init__(self, id_product, name, price, status_product, description, quantity_product):
        self.id = id_product
        self.name = name
        self.price = price
        self.status = status_product
        self.description = description
        self.quantity = quantity_product
    def to_string(self):
        return str(self.name) + ' ' + str(self.price) + ' ' + str(self.quantity)