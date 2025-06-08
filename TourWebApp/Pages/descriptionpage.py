import reflex as rx
from .homepage import render_page
from ..DB.connection import Offer

class DescriptionState(rx.State):
    offer: list[dict] = []
    id: int= -1
    title: str = ""
    desc:str = ""
    image_url:str = ""
    details:str = ""
    itinerary:str = ""
    price:float = 0

    @rx.event
    def get_offers(self):
        id = self.router.page.params.get("offer_id")
        
        print(id)

        offer_conn = Offer("","","","","",0)
        id = int(id)
        offer_data = offer_conn.read_offer_by_id(id=id)
        
        for offer_row in offer_data:
            self.id = int(offer_row[0])
            self.title = str(offer_row[1])
            self.desc = str(offer_row[2])
            self.image_url = str(offer_row[3])
            self.details = str(offer_row[4])
            self.itinerary = str(offer_row[5])
            self.price = float(offer_row[6])


def description_page() -> rx.Component:
    rx
    return render_page(
        rx.box(
            rx.desktop_only(
                rx.hstack(
                    rx.vstack(
                        rx.image(src=DescriptionState.image_url, width="700px", height="600px", style={"object-fit":"cover"}, border_radius="5px")
                    ),
                    rx.vstack(
                        rx.vstack(
                            rx.heading(DescriptionState.title, size="9"),
                            rx.text(DescriptionState.desc, size="4",
                            margin_left=".5em"),
                            rx.hstack(
                                rx.icon("list-collapse"),
                                rx.heading(" - Detalles", size="5"),
                                spacing="2",
                                justify="center",
                                align="center",
                                margin_left=".5em"
                            ),
                            rx.text(DescriptionState.details, size="3",
                            margin_left=".5em"),
                            rx.hstack(
                                rx.icon("receipt-text"),
                                rx.heading(" - Itinerario", size="5"),
                                spacing="2",
                                justify="center",
                                align="center",
                                margin_left=".5em"
                            ),
                            rx.text(DescriptionState.itinerary, size="3", margin_left=".5em"),
                            rx.heading("Precio:\n", f"{DescriptionState.price:,} RD$", margin_left=".5em"),
                            rx.link(
                                rx.button("Pagar", width="100%", size="3", margin_y=".5em"),
                                href=f"/payment?id={DescriptionState.id}",
                                width="100%",
                                margin_left=".5em",
                                style={"cursor":"pointer"}
                            ),
                            spacing="5",
                            width="600px"
                        ),
                        justify="center",
                        spacing="7",
                    ),
                    spacing="4",
                    width="100%",
                    style={
                        "justify-content":"space-evenly",
                    },
                    align="center",
                ),
            ),
            padding="2.5em",
            heigth="100dvh",
            on_mount=DescriptionState.get_offers,
        )
    )