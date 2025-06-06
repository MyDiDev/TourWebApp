import mysql.connector

class Connection:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password=")A{IjWm1}h,H+u-^"
        )
        self.cur = self.cnx.cursor()

class User(Connection):
    def __init__(self, name:str, email:str, password:str, type:str):
        self.name = name
        self.email = email
        self.password = password
        self.type = type
        self.cur = super().cur
    
    def add_user(self):
        try:
            self.cur.callproc("SP_INSERTAR_USUARIOS", [self.name, self.password, self.type])
        except Exception:
            raise mysql.connector.errors

    def del_user(self, id:int):
        try:
            self.cur.callproc("SP_ELIMINAR_USUARIOS", [id])
        except Exception:
            raise mysql.connector.errors

    def upt_user(self, id:int):
        try:
            self.cur.callproc("SP_ACTUALIZAR_USUARIOS", [id, self.name, self.password, self.type])
        except Exception:
            raise mysql.connector.errors

    def read_user(self):
        try:
            self.cur.callproc("SP_LEER_USUARIOS")
        except Exception:
            raise mysql.connector.errors
    

class Offer:
    def __init__(self, title:str, description:str, img_ulr:str, details:str, itinerary:str, price:float):
        self.title = title
        self.description= description
        self.img_url = img_ulr
        self.details = details
        self.itinerary = itinerary
        self.price = price

class Contact:
    def __init__(self, name:str, email:str, message:str):
        self.name = name
        self.email = email
        self.message = message

class Schedule:
    def __init__(self, name:str, email:str, phone:str, id_tour:int, id_user:int, id_payment:int, date:str, people_amount:int):
        self.name = name
        self.email = email
        self.phone = phone
        self.id_tour = id_tour
        self.id_user = id_user
        self.id_payment = id_payment
        self.date = date
        self.people_amount = people_amount

    