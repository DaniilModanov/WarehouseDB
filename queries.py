import pyodbc
import bcrypt
from tools import *
from datetime import datetime

key = b'$2b$12$QOVGUfNiqGURvVHgFtuwc.'

class Query:
    def __init__(self):
        self.connection_to_db = pyodbc.\
            connect(r'Driver={SQL Server};Server=DESKTOP-CU27HEJ;Database=Warehouse_Coursework;Trusted_Connection=yes;')
        self.cursor = self.connection_to_db.cursor()

    def __del__(self):
        self.connection_to_db.close()

    def getLogin(self, login):
        self.cursor.execute(f"SELECT login from Users where login ='{login}'")
        return self.cursor.fetchone().login



    def getPassword(self, login, password):
        self.cursor.execute(f"SELECT password from Users where login ='{login}'")
        ifPass = str.encode(self.cursor.fetchone().password)
        password = bcrypt.hashpw(str.encode(password), key)
        if password == ifPass:
            return True
        return None

    def getWorkersName(self):
        self.cursor.execute('Select full_name from WarehouseWorker')
        workersNames = []
        while True:
            t = self.cursor.fetchone()
            if t == None:
                break
            workersNames.append(t.full_name)
        return workersNames
    def getCustomerName(self):
        self.cursor.execute('Select full_name from Customer')
        return self.cursor.fetchall()
    #window, login, password, full_name, phone_number, email

    def register_customer(self, login, password, full_name, phone_number, email):
        password = bcrypt.hashpw(str.encode(password), key)
        self.cursor.execute(f"EXEC ADD_CUSTOMER '{login}', '{password.decode()}','{full_name}', '{phone_number}', '{email}'")
        self.connection_to_db.commit()

    def register_worker(self, login, password, full_name, phone_number, email):
        password = bcrypt.hashpw(str.encode(password), key)
        self.cursor.execute(f"EXEC ADD_WORKER '{login}', '{password.decode()}','{full_name}', '{phone_number}', '{email}'")
        self.connection_to_db.commit()

    def regDirector(self, login, password):
        password = bcrypt.hashpw(str.encode(password), key)

        self.cursor.execute(
            f"EXEC ADD_DIR '{login}', '{password.decode()}'")
        self.connection_to_db.commit()

    def getUserIdByLogin(self, login):
        self.cursor.execute(f"Select id_user from Users where login='{login}'")
        return self.cursor.fetchone().id_user

    def getUserInfo(self, idUser):
        self.cursor.execute(
            f"SELECT id_customer FROM Customer JOIN Users ON Users.id_user = Customer.id_user AND Users.id_user='{idUser}'")
        id_customer = self.cursor.fetchone()
        if id_customer:
            customer_info = self.cursor.execute(f"SELECT id_customer, full_name, email, phone_number FROM Customer JOIN Users ON Users.id_user = Customer.id_user AND Users.id_user='{idUser}'")
            return Customer(idUser, "Покупатель", customer_info.full_name, customer_info.phone_number, customer_info.email, customer_info.id_customer)
        else:
            self.cursor.execute(
                f"SELECT id_worker, full_name, email, phone_number FROM WarehouseWorker JOIN Users ON Users.id_user = WarehouseWorker.id_user AND Users.id_user='{idUser}'")
            worker_info = self.cursor.fetchone()
            if worker_info:
                return Worker(idUser, "Кладовщик", worker_info.full_name, worker_info.phone_number, worker_info.email, worker_info.id_worker)
            else:
                return User(idUser, "Директор")


    def getUserProfile(self, userId):
        self.cursor.execute(f"SELECT id_customer FROM Customer JOIN Users ON Users.id_user = Customer.id_user AND Users.id_user='{userId}'")
        id_customer = self.cursor.fetchone()
        if id_customer:
            return "Покупатель"
        else:
            self.cursor.execute(
                f"SELECT id_worker FROM WarehouseWorker JOIN Users ON Users.id_user = WarehouseWorker.id_user AND Users.id_user='{userId}'")
            id_worker = self.cursor.fetchone()
            if id_worker != None:
                return "Кладовщик"
            else:
                return "Директор"

    def getCustomerInfo(self, idUser):
        self.cursor.execute(f"Select id_customer, full_name, phone_number, email from Customer where id_user='{idUser}'")
        customerInfo = self.cursor.fetchone()
        return Customer(idUser, customerInfo.full_name, customerInfo.phone_number,
                        customerInfo.email, customerInfo.id_customer)
    def getCatalog(self):
        self.cursor.execute(f"SELECT * FROM Products")
        products = self.cursor.fetchall()
        arr_products = []
        for value in products:
            temp = Product(value[0], value[1], value[2], value[3], value[4], value[5])
            arr_products.append(temp)
        return arr_products
    def getTopProducts(self):
        self.cursor.execute(f"SELECT * FROM POPULAR_PRODUCTS")
    def getProductStatuses(self):
        self.cursor.execute(f"SELECT * FROM ProductStatus")
        statuses = self.cursor.fetchall()
        return statuses

    def create_and_pay_order(self, customer, cart, address):
        date = datetime.today().strftime('%Y-%m-%d')
        user_id = customer.idCustomer
        total = 0
        self.cursor.execute(f"MAKE_AND_PAY_ORDER {user_id}, '{date}', '{address}', {cart[0].id}, {cart[0].quantity}")
        self.connection_to_db.commit()
        total += cart[0].price * cart[0].quantity
        self.cursor.execute(f"SELECT COUNT(id_order) FROM Orders")
        last_index = self.cursor.fetchone()[0]
        for i in range(1, len(cart)):
            self.cursor.execute(f"ADD_GOOD_TO_ORDER {cart[i].id}, {last_index}, {cart[i].quantity}")
            self.connection_to_db.commit()
            total += cart[i].price * cart[i].quantity

        self.cursor.execute(f"UPDATE Orders SET total_price={total} WHERE Orders.id_order={last_index}")

    def createOrder(self, customer, cart, address):
        date = datetime.today().strftime('%Y-%m-%d')
        user_id = customer.idCustomer
        total = 0
        self.cursor.execute(f"MAKE_ORDER {user_id}, '{date}', '{address}', {cart[0].id}, {cart[0].quantity}")
        self.connection_to_db.commit()
        total += cart[0].price * cart[0].quantity
        self.cursor.execute(f"SELECT COUNT(id_order) FROM Orders")
        last_index = self.cursor.fetchone()[0]
        for i in range(1, len(cart)):
            self.cursor.execute(f"ADD_GOOD_TO_ORDER {cart[i].id}, {last_index}, {cart[i].quantity}")
            self.connection_to_db.commit()
            total += cart[i].price * cart[i].quantity

        self.cursor.execute(f"UPDATE Orders SET total_price={total} WHERE Orders.id_order={last_index}")

    def getCustomerOrders(self, customer):
        self.cursor.execute(f"""SELECT Customer.full_name AS Customer, WarehouseWorker.full_name AS Worker, OrderStatus.status, created_at, total_price FROM Orders
	                            JOIN Customer ON Customer.id_customer=Orders.customer_id
	                            JOIN WarehouseWorker ON WarehouseWorker.id_worker=Orders.worker_id
	                            JOIN OrderStatus ON OrderStatus.status_id=Orders.id_status
	                            WHERE Customer.id_customer={customer.idCustomer}""")
        return self.cursor.fetchall()

    def getOrderStatuses(self):
        self.cursor.execute(f"SELECT * FROM OrderStatus")
        statuses = self.cursor.fetchall()
        return statuses