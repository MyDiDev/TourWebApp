import reflex as rx

class FooterState(rx.State):
    pass

def footer() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.heading("TourGo", size="8"),
                rx.text("© Copyright - 2025", text_align="center"),
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
        style={"background-color":"rgb(24,24,24)"},
        padding="2em",
        margin_top="20dvh",
    )