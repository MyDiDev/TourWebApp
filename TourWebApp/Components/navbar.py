import reflex as rx

class NavState(rx.State):
    pass

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.heading("TurisGo", size="9"),
                rx.hstack(
                    rx.link("Inicio", color="white", size="5"),
                    rx.link("Descripciones", color="white", size="5"),
                    rx.link("Agendar", color="white", size="5"),
                    justify="center",
                    align="center",
                    padding_top="1em",
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Registrate",
                        background="none",
                        color="white",
                        style={
                            "border":"solid 1px white",
                            "cursor":"pointer",
                        },
                        size="3"
                    ),
                    rx.button(
                        "Inicia Sesion",
                        background_color="white",
                        color="black",
                        size="3"
                    ),
                    padding_top="1em",
                ),
                spacing="6",
                style={
                    "justify-content":"space-evenly",
                },
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.heading("TurisGo", size="7"),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(""),
                    ),
                    rx.menu.content(
                        rx.menu.item(
                            rx.link("Inicio", color="white", size="5"),
                        ),
                        rx.menu.item(
                            rx.link("Descripciones", color="white", size="5"),
                        ),
                        rx.menu.item(
                            rx.link("Agendar", color="white", size="5"),
                        ),
                        rx.separator(),
                        rx.menu.item(
                            rx.button(
                                "Registrate",
                                background="none",
                                color="white",
                                style={
                                    "border":"solid 1px white",
                                    "cursor":"pointer",
                                },
                                size="3"
                            ),
                            rx.button(
                                "Inicia Sesion",
                                background_color="white",
                                color="black",
                                size="3"
                            ),
                        ),
                    ),
                ),
                spacing="6",
                style={
                    "justify-content":"space-evenly",
                },
                width="100%",
            ),
        ),
        padding="1em",
    )