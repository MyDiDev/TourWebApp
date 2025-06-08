import reflex as rx
from ..Components.navbar import navbar
from ..Components.footer import footer
from ..DB.connection import Offer
from ..DB.connection import Contact
from .loginpage import LoginState

class HomePageState(rx.State):
    offers: list[dict] = []

    @rx.event
    def get_offers(self):
        offer_connection = Offer("","","","","",0)
        offers_data = offer_connection.read_offer()
        
        self.offers = [
            {
                "id":int(offer[0]),
                "title":str(offer[1]),
                "description":str(offer[2]),
                "image_url":str(offer[3]),
                "details":str(offer[4]),
                "itinerary":str(offer[5]),
                "price":float(offer[6]),
            }
            for offer in offers_data
        ]

    @rx.event
    def add_contact(self, data):
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")
        
        if not name or not email or not message:
            yield rx.toast.error("Llene las entradas", close_button=True)
            return

        contact_conn = Contact(name, email, message)
        contact_conn.add_contact()
        yield rx.toast.success("Mensaje enviado exitosamente!", close_button=True)

def render_offer_card(offer) -> rx.Component:
    return rx.box(
        rx.image(src=offer["image_url"], width="450px", height="450px", border_radius="5px",  style={"object-fit":"cover", "border-bottom-right-radius":"0px", "border-bottom-left-radius":"0px"}),
        rx.box(
            rx.heading(offer["title"], margin_top=".5em", size="5"),
            rx.text(offer["description"], size="2"),
            rx.link(
                rx.button("Ver Mas", margin_top="1em", size="2", width="100%", style={"cursor":"pointer"}),
                href=f"/description?offer_id={offer['id']}"
            ),
            padding_x=".5em",
            padding_bottom="1em",
        ),
        width="450px",
        style={
            "background": "rgba( 0, 0, 0, 0.3 )",
            "backdrop-filter": "blur(20px)",
            "-webkit-backdrop-filter": "blur(20px)",
            "border-radius": "10px",
            "border": "1px solid rgba( 255, 255, 255, 0.18 )",
        },
    )

def render_page(child:rx.Component) -> rx.Component:
    return rx.fragment(
        rx.box(
            child,
            height="100%",
        ),
    )

def home_page() -> rx.Component:
    return render_page(
        rx.box(
            rx.desktop_only(
                rx.cond(
                    LoginState.is_logged,
                    rx.box(
                        rx.box(
                            navbar(),
                            rx.vstack(
                                rx.heading("Vive experiencias únicas", font_size="100px", line_height="1.5", style={"cursor":"Default"}),
                                rx.text("Descubre y reserva tu próxima aventura con confianza.", size="7", style={"cursor":"Default"}),
                                rx.button("¿Que Esperas?", background_color="white", color="black", size="4", width="50%", style={"cursor":"pointer"}),
                                spacing="5",
                                justify="center",
                                align="center",
                                
                                width="100%",
                                height="100dvh",
                                color="white",
                            ),
                            style={
                                "background-image":"url('https://images.pexels.com/photos/5273055/pexels-photo-5273055.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')",
                                "background-color":"rgba(0,0,0,0.5)",
                                "background-blend-mode":"color-burn",
                                "background-position":"center",
                                "background-size":"cover",
                                "background-repeat":"no-repeat",
                            },
                        ),
                        rx.hstack(
                            rx.image(src="https://images.pexels.com/photos/810775/pexels-photo-810775.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width="50%", border_radius="5px"),
                            rx.vstack(
                                rx.heading("¡Busca tu viaje!", size="9"),
                                rx.text("Elige destino, fecha y número de personas para encontrar el tour ideal!.", size="6"),
                                rx.button("Agenda el tuyo!", size="3", width="100%"),  
                                spacing="6",   
                                justify="center",
                            ),
                            spacing="7",
                            justify="center",
                            align="center",

                            width="100%",
                            padding="1em",
                            margin_y="1em",
                        ),
                        rx.heading("¡Esta es tu oportunidad!", size="9", margin_y="2em", text_align="center"),
                        rx.hstack(
                            rx.form(
                                rx.vstack(
                                    rx.box(
                                        rx.heading("Destino", size="7", margin_bottom=".5em"),
                                        rx.text("Ingresa el destino para tu tour", size="4"),
                                    ),
                                    rx.input(placeholder="Ingrese el destino del tour", size="3", width="100%"),
                                    spacing="4",
                                    margin_y="1.2em",
                                ),
                                rx.vstack(
                                    rx.box(
                                        rx.heading("Fecha", size="7", margin_y=".5em"),
                                        rx.text("Ingresa la fecha para el tour", size="4"),
                                    ),
                                    rx.input(placeholder="Ingrese la fecha para el tour", size="3", width="100%"),
                                    spacing="4",
                                    margin_y="1.2em",
                                ),
                                rx.vstack(
                                    rx.box(
                                        rx.heading("Personas", size="7", margin_y=".5em"),
                                        rx.text("ingresa la cantidad de personas", size="4"),
                                    ),
                                    rx.input(placeholder="Ingrese cuantas personas van", size="3", width="100%"),
                                    spacing="4",
                                    margin_y="1.2em",
                                ),
                                rx.vstack(
                                    rx.button("Agendar", size="4", width="100%", style={"cursor":"pointer"}),
                                    margin_top=".5em",
                                ),
                                width="50%",
                                max_width="500px",
                                padding="1em",
                                border_radius="10px",
                                style={
                                    "background": "rgba( 0, 0, 0, 0.3 )",
                                    "backdrop-filter": "blur(20px)",
                                    "-webkit-backdrop-filter": "blur(20px)",
                                    "border-radius": "10px",
                                    "border": "1px solid rgba( 255, 255, 255, 0.18 )",
                                },
                            ),
                            rx.image(src="https://images.pexels.com/photos/2646066/pexels-photo-2646066.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width="60%", style={"border-radius":"5px"}),
                            
                            style={
                                "justify-content":"space-evenly",
                            },
                            align="center",
                            spacing="6",

                            padding="1em",
                            margin_y="1em",
                        ),
                        rx.heading("Ofertas Destacadas", size="9", margin_y="2em", text_align="center"),

                        rx.hstack(
                            rx.foreach(HomePageState.offers, render_offer_card),
                            on_mount=HomePageState.get_offers,
                            justify="center",
                            align="center",
                            spacing="8",
                            style={
                                "flex-wrap":"wrap",
                            },
                        ),
                
                        rx.heading("Sobre Nosotros", size="9", margin_y="2em", text_align="center"),
                        rx.vstack(
                            rx.hstack(
                                rx.vstack(
                                    rx.heading("01", font_size="100px"),
                                    rx.box(
                                        rx.heading("Turismo con Propósito", size="9", margin_y=".5em"),
                                        rx.text("En TurisGo creemos que viajar es más que visitar lugares. Trabajamos con comunidades locales para ofrecer experiencias auténticas que respetan la cultura, la historia y el entorno.", size="5"),
                                        width="500px",
                                    ),
                                    justify="center",
                                    spacing="4",
                                ),
                                rx.image(src="https://images.pexels.com/photos/10842217/pexels-photo-10842217.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width="40%", max_height="500px", border_radius="5px", style={"object-fit":"cover"}),
                                
                                align="center",
                                width="100%",
                                style={"justify-content":"space-evenly"},
                            ),

                            rx.hstack(
                                rx.image(src="https://images.pexels.com/photos/5232896/pexels-photo-5232896.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width="40%", max_height="500px", border_radius="5px", style={"object-fit":"cover"}),

                                rx.vstack(
                                    rx.heading("02", font_size="100px"),
                                    rx.box(
                                        rx.heading("Comprometidos con la Sostenibilidad", size="9", margin_y=".5em"),
                                        rx.text("Priorizamos actividades que minimizan el impacto ambiental, promovemos prácticas responsables y apoyamos proveedores que comparten nuestra visión ecológica.", size="5"),
                                        width="500px",
                                    ),
                                    justify="center",
                                    spacing="4",
                                ),
                                align="center",
                                width="100%",
                                style={"justify-content":"space-evenly"},
                            ),

                            spacing="9",
                            style={"gap":"20dvh"},
                            height="100%",
                            justify="center",
                            margin_y="1em",
                            id="about",
                        ),
                        
                        rx.heading("¿Tienes preguntas? ¡Contáctanos!", size="9", text_align="center", margin_y=".5em", margin_top="3em"),
                        rx.text("Estamos aquí para ayudarte a planificar tu próxima aventura. Escríbenos y te responderemos en menos de 24 horas.", text_align="center", margin_bottom="2.5em"),
                        
                        rx.vstack(
                            rx.hstack(
                                rx.box(
                                    rx.heading("Correo Electronico"),
                                    rx.link("contacto@turisgo.com"),
                                ),
                                rx.box(
                                    rx.heading("Numero de Telefono"),
                                    rx.link("+34 123-456-789"),
                                ),
                                width="100%",
                                justify="center",
                                align="start",
                                spacing="8"
                            ),
                            rx.vstack(
                                rx.box(
                                    rx.heading("Ubicacion"),
                                    rx.html('''
                                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3784.193164027807!2d-69.8890732888208!3d18.474907570494103!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8eaf88162ae70441%3A0xd6e5500879fecb4d!2sColonial%20Zone%20Dominican%20Republic!5e0!3m2!1sen!2sdo!4v1749081120146!5m2!1sen!2sdo" width="700" height="550" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" style="border-radius:15px;"></iframe>
                                    ''',  margin_y="1.2em"),
                                ),
                                width="100%",
                                justify="center",
                                align="center",
                            ),

                            justify="center",
                            spacing="7",
                            width="100%",
                            margin_y="2em",
                            id="contact",
                        ),

                        rx.heading("¡Llena el Formulario!", size="9", margin_top="3em", margin_bottom="1.5em", text_align="center"),

                        rx.vstack(
                            rx.form(
                                rx.vstack(
                                    rx.box(
                                        rx.heading("Nombre", size="7", margin_bottom=".5em"),
                                        rx.text("Ingresa su nombre", size="4"),
                                    ),
                                    rx.input(placeholder="Ingrese su nombre de usuario", size="3", name="name", type="text", width="100%"),
                                    spacing="4",
                                    margin_y="1.2em",
                                ),
                                rx.vstack(
                                    rx.box(
                                        rx.heading("Email", size="7", margin_y=".5em"),
                                        rx.text("Ingresa el correo electronico", size="4"),
                                    ),
                                    rx.input(placeholder="Ingrese el email o correo de tu cuenta", size="3", width="100%", type="email", name="email"),
                                    spacing="4",
                                    margin_y="1.2em",
                                ),
                                rx.vstack(
                                    rx.box(
                                        rx.heading("Mensaje", size="7", margin_y=".5em"),
                                        rx.text("Describe lo que quieres?", size="4"),
                                    ),
                                    rx.text_area(placeholder="Escribe aqui", size="3", width="100%", name="message"),
                                    spacing="4",
                                    margin_y="1.2em",
                                ),
                                rx.vstack(
                                    rx.button("Enviar", size="4", width="100%", type="submit", style={"cursor":"pointer"}),
                                    margin_top=".5em",
                                ),
                                width="50%",
                                max_width="700px",
                                padding="1em",
                                border_radius="10px",
                                on_submit=HomePageState.add_contact,
                                reset_on_submit=True,
                                style={
                                    "background": "rgba( 0, 0, 0, 0.3 )",
                                    "backdrop-filter": "blur(20px)",
                                    "-webkit-backdrop-filter": "blur(20px)",
                                    "border-radius": "10px",
                                    "border": "1px solid rgba( 255, 255, 255, 0.18 )",
                                },
                            ),
                            justify="center",
                            align="center",
                            margin_bottom="3em",
                            width="100%",
                        ),
                        footer(),
                        height="100%",
                        color="white",
                    ),
                    rx.vstack(
                        rx.heading("Intenta Iniciar Sesion", size="8"),
                        rx.text("Tu Sesion no esta registrada", size="5"),
                        rx.link(
                            rx.button("Inicia Sesion", size="4", style={"cursor":"pointer"}),
                            href="/login",
                        ),
                        width="100%",
                        margin_top="20dvh",
                        justify="center",
                        align="center"
                    ), 
                )
            ),
            rx.tablet_only(),
            rx.mobile_only(),
        ),
    )