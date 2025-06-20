import reflex as rx
from ..DB.connection import User

class RegisterState(rx.State):
    
    @rx.event
    def add_new_user(self, data):
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if not username or not password or not email:
            yield rx.toast.error("Llene las entradas", close_button=True)
            return
        
        user_conn = User(username, email, password, 'user')
        user_conn.add_user()
        yield rx.redirect("/login")

def register_page() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.box(
                rx.desktop_only(
                    rx.hstack(
                        rx.vstack(
                            rx.vstack(
                                rx.heading("¡Bienvenido a TourGo!", size="9"),
                                rx.text("Descubre y reserva tu próxima aventura con confianza.", size="6"),
                                justify="center",
                                align="center",
                                spacing="5",
                                text_align="center",
                            ),
                            
                            width="100%",
                            height="100dvh",

                            style={
                                "background-image":"url('https://images.pexels.com/photos/5273211/pexels-photo-5273211.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')",
                                "background-color":"rgba(0,0,0,0.5)",
                                "background-blend-mode":"color-burn",
                                "background-repeat":"no-repeat",
                                "background-size":"cover",
                                "color":"white",
                            },
                            justify="center",
                            align="center",
                        ),
                        rx.vstack(
                            rx.vstack(
                                rx.heading("¡Registrate a TourGo!", font_size="60px", margin_y=".5em", line_height="1.5"),
                                rx.form(
                                    rx.vstack(
                                        rx.text("Nombre:", size="4"),
                                        rx.input(placeholder="Ingrese un nombre de usuario", name="username", type="text", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    rx.vstack(
                                        rx.text("Contraseña:", size="4"),
                                        rx.input(placeholder="Ingrese la contraseña para su cuenta", name="password", type="password", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    rx.vstack(
                                        rx.text("Correo Electronico:", size="4"),
                                        rx.input(placeholder="Ingrese el correo electronico para su cuenta", name="email", type="email", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    rx.vstack(
                                        rx.text("Ya tienes una? ", rx.link("Inicia Sesion!", href="/login"), size="4"),
                                        margin_y="1em",
                                        justify="center",
                                        align="center",
                                    ),
                                    rx.vstack(
                                        rx.button("Registrarme", size="3", width="100%", style={"cursor":"pointer"}),
                                        margin_y="1.5em",
                                    ),
                                    on_submit=RegisterState.add_new_user,
                                ),
                                width="85%",
                                padding="1em",
                                style={
                                    "background": "rgba( 0, 0, 0, 0.3 )",
                                    "backdrop-filter": "blur(20px)",
                                    "-webkit-backdrop-filter": "blur(20px)",
                                    "border-radius": "10px",
                                    "border": "1px solid rgba( 255, 255, 255, 0.18 )",
                                },
                            ),
                            width="100%",
                            height="100dvh",
                            justify="center",
                            align="center",
                        ),
                        width="100%",
                    ),
                ),
                rx.mobile_and_tablet(
                    rx.box(
                        rx.vstack(
                            rx.vstack(
                                rx.heading("¡Registrate a TourGo!", font_size="60px", line_height="1.5"),
                                rx.form(
                                    rx.vstack(
                                        rx.text("Nombre:", size="4"),
                                        rx.input(placeholder="Ingrese un nombre de usuario", name="username", type="text", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    rx.vstack(
                                        rx.text("Contraseña:", size="4"),
                                        rx.input(placeholder="Ingrese la contraseña para su cuenta", name="password", type="password", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    rx.vstack(
                                        rx.text("Correo Electronico:", size="4"),
                                        rx.input(placeholder="Ingrese el correo electronico para su cuenta", name="email", type="email", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    rx.vstack(
                                        rx.text("Ya tienes una? ", rx.link("Inicia Sesion!", href="/login"), size="4"),
                                        margin_y="1em",
                                        justify="center",
                                        align="center",
                                    ),
                                    rx.vstack(
                                        rx.button("Registrarme", type="submit", size="3", width="100%", style={"cursor":"pointer"}),
                                        margin_y="1.5em",
                                    ),
                                ),
                                width="70%",
                                padding="1em",
                                style={
                                    "background": "rgba( 0, 0, 0, 0.3 )",
                                    "backdrop-filter": "blur(20px)",
                                    "-webkit-backdrop-filter": "blur(20px)",
                                    "border-radius": "10px",
                                    "border": "solid 1px white",
                                },
                            ),
                            width="100%",
                            height="100dvh",
                            justify="center",
                            align="center",
                        ),
                        width="100%",
                    ),
                    style={
                        "background-image":"url('https://images.pexels.com/photos/5273211/pexels-photo-5273211.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')",
                        "background-color":"rgba(0,0,0,0.5)",
                        "background-blend-mode":"color-burn",
                        "background-repeat":"no-repeat",
                        "background-size":"cover",
                    },
                ),
                width="100%",
            ),
            height="100%"
        )
    )
