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
