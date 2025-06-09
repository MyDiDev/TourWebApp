import reflex as rx
from .homepage import render_page
from ..DB.connection import Offer
from ..DB.connection import Schedule
from ..DB.connection import Transactions
from .loginpage import LoginState
from datetime import datetime, timedelta

class PaymentState(rx.State):
    offer_title: str= ""
    offer_details:str = ""
    offer_price:float = 0
    image_url:str = ""
    offer_id:int = 0
    uid: int | str = 0

    @rx.event
    def get_offer_data(self) -> None:
        offer_conn = Offer("","","","","",0)
        offer_id = self.router.page.params.get("id")
        self.offer_id = int(offer_id)
        offer_data = offer_conn.read_offer_by_id(self.offer_id)

        for offer_row in offer_data:
            self.offer_title = str(offer_row[1])
            self.image_url = str(offer_row[3])
            self.offer_details = str(offer_row[4])
            self.offer_price = float(offer_row[6])

    @rx.event
    def add_schedule_and_payment(self, data):
        payment_method = data.get("method")
        name = data.get("username")
        email = data.get("email")
        phone = data.get("phone")
        people_amount = data.get("people_amount")

        if not payment_method or not name or not email or not phone or not people_amount:
            yield rx.toast.error("Llene las entradas", close_button=True)
            return
        
        payment_conn = Transactions(payment_method, "Realizado", self.offer_price)
        payment_conn.add_payment()
        payment_id = payment_conn.payments_get_id(self.offer_price)

        yield rx.toast.info("Pago Registrado", close_button=True)

        uid = self.router.page.params.get("uid")
        uid = int(uid)

        time = datetime.now() + timedelta(days=24, hours=2, minutes=30)
        people_amount = int(people_amount)

        schedule_conn = Schedule(name, email, phone, self.offer_id, uid, payment_id[0][0], time.strftime("%Y-%m-%d %H:%M:%S"), people_amount)
        schedule_conn.add_schedule()

        yield rx.toast.info("Reserva Realizada, Gracias por reservas y confiar en TourGO!", close_button=True)
        yield rx.redirect("/home")

def payment_page() -> rx.Component:
    return render_page(
        rx.box(
            rx.desktop_only(
                rx.vstack(
                    rx.vstack(
                        rx.image(src=PaymentState.image_url, height="700px", width="700px", style={"object-fit":"cover"}),

                        rx.heading(PaymentState.offer_title, size="9"),
                        rx.separator(),
                        
                        rx.box(
                            rx.heading("Detalles de esta actividad", size="7"),
                            rx.text(PaymentState.offer_details, margin_y=".5em"),
                        ),

                        rx.hstack(
                            rx.text("Precio:", size="4"),
                            rx.heading(f"{PaymentState.offer_price:,} RD$", size="4"),
                            spacing="2",
                            align="center",
                        ),

                        rx.dialog.root(
                            rx.dialog.trigger(
                                rx.button(f"Pagar", size="3", width="100%", font_size="1.2em", style={"cursor":"pointer"}),
                            ),
                            rx.dialog.content(
                                rx.heading("Realiza el Pago!", size="8"),

                                rx.hstack(
                                    rx.text("Precio:", size="4"),
                                    rx.heading(f"{PaymentState.offer_price:,} RD$", size="4"),
                                    spacing="2",
                                    align="center",
                                    margin_top="1em"
                                ),

                                rx.form(
                                    rx.vstack(
                                        rx.text("Nombre:", size="4"),
                                        rx.input(placeholder="Ingrese su nombre o nombre de usuario", name="username", type="text", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    rx.vstack(
                                        rx.text("Email:", size="4"),
                                        rx.input(placeholder="Ingrese su correo electronico", name="email", type="email", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),

                                    rx.vstack(
                                        rx.text("Telefono:", size="4"),
                                        rx.input(placeholder="Ingrese su numero de telefono", name="phone", type="text", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    
                                    rx.vstack(
                                        rx.text("Cuantas personas Van?:", size="4"),
                                        rx.input(placeholder="Ingrese la cantidad de gente", name="people_amount", type="number", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),

                                    rx.vstack(
                                        rx.text("Metodo:", size="4"),
                                        rx.select(
                                            ["Tarjeta de Credito", "Transaccion", "Fisico"],
                                            default_value="Tarjeta de Credito",
                                            name="method",
                                            required=True,
                                            margin_y="1.5em",
                                            width="100%",
                                            size="3"
                                        ),
                                        spacing="3",
                                    ),

                                    rx.vstack(
                                        rx.button("Realizar Pago", type="submit",  size="3", width="100%", style={"cursor":"pointer"}, margin_y="1em"),
                                    ),
                                    
                                    rx.vstack(
                                        rx.text("Una vez decida realizar este pago, acepta nuestros terminos y condiciones para esta tarea", size="1", text_align="center"),
                                        margin_y=".5em",
                                        align="center",
                                    ),
                                    on_submit=PaymentState.add_schedule_and_payment,
                                    padding=".5em",
                                ),
                                style={
                                    "background": "rgba( 0, 0, 0, 0.3 )",
                                    "backdrop-filter": "blur(20px)",
                                    "-webkit-backdrop-filter": "blur(20px)",
                                    "border-radius": "10px",
                                    "border": "1px solid rgba( 255, 255, 255, 0.18 )",
                                },
                            ),

                        ),

                        style={
                            "background": "rgba( 0, 0, 0, 0.3 )",
                            "backdrop-filter": "blur(20px)",
                            "-webkit-backdrop-filter": "blur(20px)",
                            "border-radius": "10px",
                            "border": "1px solid rgba( 255, 255, 255, 0.18 )",
                        },
                        padding="1em",
                        width="700px",
                        spacing="4",
                        margin_y="5dvh",
                    ),
                    justify="center",
                    align="center",
                    on_mount=PaymentState.get_offer_data,
                ),
            ),
        )
    )