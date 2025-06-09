import mysql.connector
import datetime

class Connection:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            database="TourBD",
            password=")A{IjWm1}h,H+u-^",
        )
        self.cur = self.cnx.cursor()

class User:
    def __init__(self, name:str, email:str, password:str, type:str):
        self.name = name
        self.email = email
        self.password = password
        self.type = type
        self.conn = Connection()
        self.cur = self.conn.cur
        self.cnx = self.conn.cnx
    
    def add_user(self):
        try:
            self.cur.callproc("SP_INSERTAR_USUARIOS", [self.name, self.email, self.password, self.type])
            self.cnx.commit()
        except Exception as e:
            raise e

    def del_user(self, id:int):
        try:
            self.cur.callproc("SP_ELIMINAR_USUARIOS", [id])
            self.cnx.commit()
        except Exception as e:
            raise e

    def upt_user(self, id:int):
        try:
            self.cur.callproc("SP_ACTUALIZAR_USUARIOS", [self.name, self.email, self.password, self.type, id])
            self.cnx.commit()
        except Exception as e:
            raise e

    def read_user(self):
        try:
            self.cur.callproc("SP_LEER_USUARIOS")
            for result in self.cur.stored_results():
                users = result.fetchall()
            return users
        except Exception as e:
            raise e
        
    def read_user_login(self):
        try:
            self.cur.callproc("SP_LEER_USUARIOS_U", [self.name, self.password])
            for result in self.cur.stored_results():
                users = result.fetchall()
            return users
        except Exception as e:
            raise e
    

class Offer:
    def __init__(self, title:str, description:str, img_ulr:str, details:str, itinerary:str, price:float):
        self.title = title
        self.description= description
        self.img_url = img_ulr
        self.details = details
        self.itinerary = itinerary
        self.price = price
        self.conn = Connection()
        self.cur = self.conn.cur
        self.cnx = self.conn.cnx

    def add_offer(self):
        try:
            self.cur.callproc("SP_INSERTAR_OFERTAS", [self.title, self.description, self.img_url, self.details, self.itinerary, self.price])
            self.cnx.commit()
        except Exception as e:
            raise e

    def del_offer(self, id:int):
        try:
            self.cur.callproc("SP_ELIMINAR_OFERTAS", [id])
            self.cnx.commit()
        except Exception as e:
            raise e

    def upt_offer(self, id:int):
        try:
            self.cur.callproc("SP_ACTUALIZAR_OFERTAS", [self.title, self.description, self.img_url, self.details, self.itinerary, self.price, id])
            self.cnx.commit()
        except Exception as e:
            raise e

    def read_offer(self):
        try:
            self.cur.callproc("SP_LEER_OFERTAS")
            for result in self.cur.stored_results():
                offers = result.fetchall()
            return offers
        except Exception as e:
            raise e
        
    def read_offer_by_id(self, id:int):
        try:
            self.cur.callproc("SP_LEER_OFERTAS_ID", [id])
            for result in self.cur.stored_results():
                offers = result.fetchall()
            return offers
        except Exception as e:
            raise e

class Contact:
    def __init__(self, name:str, email:str, message:str):
        self.name = name
        self.email = email
        self.message = message
        self.conn = Connection()
        self.cur = self.conn.cur
        self.cnx = self.conn.cnx

    def add_contact(self) -> None:
        try:
            self.cur.callproc("SP_INSERTAR_CONTACTOS", [self.name, self.email, self.message])
            self.cnx.commit()
        except Exception as e:
            raise e

    def del_contact(self, id:int) -> None:
        try:
            self.cur.callproc("SP_ELIMINAR_CONTACTOS", [id])
            self.cnx.commit()
            print(f"Successfully deleted contact with ID: {id}")
        except Exception as e:
            raise e

    def upt_contact(self, id:int) -> None:
        try:
            self.cur.callproc("SP_ACTUALIZAR_CONTACTOS", [self.name, self.email, self.message, id])
            self.cnx.commit()
        except Exception as e:
            raise e

    def read_contact(self) -> None | list[tuple]:
        try:
            self.cur.callproc("SP_LEER_CONTACTOS")
            for result in self.cur.stored_results():
                contacts:list[tuple] = result.fetchall()
            return contacts
        except Exception as e:
            raise e
    

class Schedule:
    def __init__(self, name:str, email:str, phone:str, id_tour:int, id_user:int, id_payment:int, date, people_amount:int):
        self.name = name
        self.email = email
        self.phone = phone
        self.id_tour = id_tour
        self.id_user = id_user
        self.id_payment = id_payment
        self.date = date
        self.people_amount = people_amount
        self.conn = Connection()
        self.cur = self.conn.cur
        self.cnx = self.conn.cnx

    def add_schedule(self):
        try:
            formatted_date = self.date
            if isinstance(self.date, datetime.datetime):
                formatted_date = self.date.strftime("%Y-%m-%d %H:%M:%S")
            
            data = [self.name, self.email, self.phone, self.id_tour, self.id_user, self.id_payment, formatted_date, self.people_amount]
            for value in data:
                print(value)

            self.cur.callproc("SP_INSERTAR_RESERVAS", [self.name, self.email, self.phone, self.id_tour, self.id_user, self.id_payment, formatted_date, self.people_amount])
            self.cnx.commit()
        except Exception as e:
            raise e

    def del_schedule(self, id:int):
        try:
            self.cur.callproc("SP_ELIMINAR_RESERVAS", [id])
            self.cnx.commit()
        except Exception as e:
            raise e

    def upt_schedule(self, id:int):
        try:
            self.cur.callproc("SP_ACTUALIZAR_RESERVAS", [self.name, self.email, self.phone, self.id_tour, self.id_user, self.id_payment, self.date, self.people_amount, id])
            self.cnx.commit()
        except Exception as e:
            raise e

    def read_schedule(self):
        try:
            self.cur.callproc("SP_LEER_RESERVAS")
            for result in self.cur.stored_results():
                schedules = result.fetchall()
            return schedules
        except Exception as e:
            raise e

class Transactions:
    def __init__(self, metodo_pago: str, estado_pago: str, monto: float):
        self.metodo_pago = metodo_pago
        self.estado_pago = estado_pago
        self.monto = monto
        self.conn = Connection()
        self.cur = self.conn.cur
        self.cnx = self.conn.cnx

    def add_payment(self):
        try:
            self.cur.callproc("SP_INSERTAR_PAGOS", [self.metodo_pago, self.estado_pago, self.monto])
            self.cnx.commit()
        except Exception as e:
            raise e

    def del_payment(self, id_pago: int):
        try:
            self.cur.callproc("SP_ELIMINAR_PAGOS", [id_pago])
            self.cnx.commit()
        except Exception as e:
            raise e

    def upt_payment(self, id_pago: int):
        try:
            self.cur.callproc("SP_ACTUALIZAR_PAGOS", [self.metodo_pago, self.estado_pago, self.monto, id_pago])
            self.cnx.commit()
        except Exception as e:
            raise e

    def read_payments(self):
        try:
            self.cur.callproc("SP_LEER_PAGOS")
            for result in self.cur.stored_results():
                payments = result.fetchall()
            return payments
        except Exception as e:
            raise e
        
    def payments_get_id(self, amount:float):
        try:
            self.cur.callproc("SP_LEER_PAGOS_ID", [amount])
            for result in self.cur.stored_results():
                payments = result.fetchall()
            return payments
        except Exception as e:
            raise e
