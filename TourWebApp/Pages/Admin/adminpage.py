import reflex as rx
# from ..homepage import render_page


class AdminPageState(rx.State):
    pass

def admin_page() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.desktop_only(
                rx.vstack(
                    rx.box(
                        rx.heading("Bienvenido Administrador", size="9", margin_y=".3em"),
                        rx.text("Bienvenido a la parte administradora de TourGo", size="5"),
                        text_align="center",
                    ),

                    rx.box(
                        rx.heading("¿Que desea Ver?", size="8"),
                        rx.separator(margin_y="1.5em", size="3", width="100%"),

                        rx.vstack(
                            rx.button("Usuarios", width="100%", size="4", style={"cursor":"pointer"}),
                            rx.button("Contactos", width="100%", size="4", style={"cursor":"pointer"}),
                            rx.button("Ofertas", width="100%", size="4", style={"cursor":"pointer"}),
                            rx.button("Pagos", width="100%", size="4", style={"cursor":"pointer"}),
                            rx.button("Reservas", width="100%", size="4", style={"cursor":"pointer"}),
                            width="100%",
                            spacing="5",
                            margin_top="1em",
                        ),

                        width="500px",
                        padding="1em",
                        margin_y="1em",
                        style={
                            "background": "rgba( 0, 0, 0, 0.3 )",
                            "backdrop-filter": "blur(20px)",
                            "-webkit-backdrop-filter": "blur(20px)",
                            "border-radius": "10px",
                            "border": "1px solid rgba( 255, 255, 255, 0.18 )",
                        },
                    ),

                    width="100%",
                    justify="center",
                    align="center",
                    height="100dvh",
                    spacing="5",
                )      
            ),
            rx.tablet_only(),
            rx.mobile_only(),
            padding="1em",
        )
    )