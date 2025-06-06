import reflex as rx
from homepage import render_page

class DescriptionState(rx.State):
    pass

def description_page() -> rx.Component:
    return render_page(
        rx.box(
            rx.desktop_only(),
            rx.tablet_only(),
            rx.mobile_only(),
        )
    )