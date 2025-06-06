import reflex as rx

class FooterState(rx.State):
    pass

def footer() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.heading("TourGo", size="8"),
                rx.text("© Copyright - 2025", text_align="center"),
                rx.hstack(
                    rx.button("Registrate", background="none", border="solid 1px white", style={"cursor":"pointer"}),
                    rx.button("Inicia Sesion", style={"cursor":"pointer"}),
                ),
                justify="between",
                align="center",
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
                rx.hstack(
                rx.heading("TourGo", size="6"),
                rx.text("©2025"),
                justify="between",
                align="center",
                width="100%",
            ),
        ),
        padding="1em",
        margin_top="20dvh",
    )