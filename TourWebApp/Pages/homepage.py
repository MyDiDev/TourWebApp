import reflex as rx
from ..Components.navbar import navbar


class State(rx.State):
    pass

def render_page(child:rx.Component, *args, **kwargs) -> rx.Component:
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
                rx.box(
                    navbar(),
                    rx.vstack(
                        rx.heading("Vive experiencias únicas", font_size="120px", line_height="1.5", style={"cursor":"Default"}),
                        rx.text("Descubre y reserva tu próxima aventura con confianza.", size="7", style={"cursor":"Default"}),
                        rx.button("¿Que Esperas?", background_color="white", color="black", size="4", width="50%", style={"cursor":"pointer"}),
                        spacing="5",
                        justify="center",
                        align="center",
                        height="100%",
                    ),
                    rx.hstack(
                        rx.image(src="https://images.pexels.com/photos/810775/pexels-photo-810775.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", max_width="800px"),
                        rx.vstack(
                            rx.heading("¡Busca tu viaje!", size="9"),
                            rx.text("Elige destino, fecha y número de personas para encontrar el tour ideal!.", size="6"),
                            rx.button("Agenda el tuyo!", background_color="black", color="white", size="3", width="100%"),  
                            spacing="6",   
                            justify="center",
                        ),
                        spacing="6",
                        justify="center",
                        align="center",
                        
                        color="black",
                        width="100%",
                        height="85dvh",
                        padding="1em",
                    ),
                    style={
                        "background-image":"url('https://images.pexels.com/photos/5273055/pexels-photo-5273055.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')",
                        "background-color":"rgba(0,0,0,0.5)",
                        "background-blend-mode":"color-burn",
                        "background-position":"center",
                        "background-size":"cover",
                        "background-repeat":"no-repeat",
                    },
                    color="white",
                    height="100dvh",
                ),
            ),
            rx.tablet_only(),
            rx.mobile_only(),
        ),
    )