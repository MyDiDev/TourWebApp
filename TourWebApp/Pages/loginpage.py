import reflex as rx
from ..DB.connection import User

# Handle inputs, add in the database, and redirect to home page 

class LoginState(rx.State):
    is_logged = False
    is_admin = False
    username = ""
    id = -1

    @rx.event
    def login(self, data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            yield rx.toast.error("Llene las Entradas", close_button=True)  
            return
        
        user_connection = User(username, "", password, "")
        result = user_connection.read_user_login()

        print(result)

        if len(result) > 0:
            self.set(
                is_logged=True,
                id = int(result[0][0]),
                username=str(result[0][1]),
                is_admin=str(result[0][4]).lower() == "admin"
            )
            print("logged in")
            yield rx.redirect(path="/home")
        else:
            yield rx.toast.error("Usuario Invalido, Intente otra vez") 

def login_page() -> rx.Component:
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
                                "background-image":"url('https://images.pexels.com/photos/12735904/pexels-photo-12735904.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')",
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
                                rx.heading("Inicia Sesion", font_size="60px", margin_y=".5em"),
                                rx.form(
                                    rx.vstack(
                                        rx.text("Nombre:", size="4"),
                                        rx.input(placeholder="Ingrese su nombre o nombre de usuario", name="username", type="text", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    rx.vstack(
                                        rx.text("Contraseña:", size="4"),
                                        rx.input(placeholder="Ingrese la contraseña de su cuenta", name="password", type="password", size='3', width="100%"),
                                        spacing="3",
                                        margin_y="1.5em",
                                    ),
                                    rx.vstack(
                                        rx.text("No tienes una? ", rx.link("Registrate!", href="/register"), size="4"),
                                        margin_y="1em",
                                        justify="center",
                                        align="center",
                                    ),
                                    rx.vstack(
                                        rx.button("Iniciar Sesion", type="submit", size="3", width="100%", style={"cursor":"pointer"}),
                                        margin_y="1.5em",
                                    ),
                                    on_submit=LoginState.login
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
                                rx.heading("Inicia Sesion",font_size="50px", line_height="1.5"),
                                rx.form(
                                    rx.vstack(
                                        rx.text("Nombre:", size="3"),
                                        rx.input(placeholder="Ingrese su nombre o nombre de usuario", name="username", type="text", size='3', width="100%", style={
                                            "background":"none",
                                            "border":"solid 1px white",
                                            "color":"white",
                                        }),
                                        spacing="3",
                                        margin_y="1em",
                                    ),
                                    rx.vstack(
                                        rx.text("Contraseña:", size="3"),
                                        rx.input(placeholder="Ingrese la contraseña de su cuenta", name="password", type="password", size='3', width="100%", style={
                                            "background":"none",
                                            "border":"solid 1px white",
                                            "color":"white",
                                        }),
                                        spacing="3",
                                        margin_y="1em",
                                    ),
                                    rx.vstack(
                                        rx.text("No tienes una? ", rx.link("Registrate!"), size="4"),
                                        margin_y="1em",
                                        justify="center",
                                        align="center",
                                    ),
                                    rx.vstack(
                                        rx.button("Iniciar Sesion", type="submit",  size="3", width="100%", style={"cursor":"pointer"}),
                                        margin_y="1.5em",
                                    ),
                                    padding=".5em",
                                ),
                                width="60%",
                                padding="1.5em",
                                style={
                                    "background": "rgba( 0, 0, 0, 0.3 )",
                                    "backdrop-filter": "blur(20px)",
                                    "-webkit-backdrop-filter": "blur(20px)",
                                    "border-radius": "10px",
                                    "border": "1px solid white",
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
                        "background-image":"url('https://images.pexels.com/photos/12735904/pexels-photo-12735904.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')",
                        "background-color":"rgba(0,0,0,0.5)",
                        "background-blend-mode":"color-burn",
                        "background-repeat":"no-repeat",
                        "background-position":"center",
                        "background-size":"cover",
                    },
                ),
                width="100%",
            ),
            height="100%",
        ),
    )
