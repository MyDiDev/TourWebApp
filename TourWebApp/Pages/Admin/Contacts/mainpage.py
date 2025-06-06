import reflex as rx

class State(rx.State):
    pass

def main_page() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.desktop_only(
                
            ),
            rx.tablet_only(),
            rx.desktop_only(),
        )
    )