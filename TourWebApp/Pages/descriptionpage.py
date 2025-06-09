import reflex as rx
from .homepage import render_page
from ..DB.connection import Offer

class DescriptionState(rx.State):
    offer: list[dict] = []
    id: int | str = 0
    title: str = ""
    desc:str = ""
    image_url:str = ""
    details:str = ""
    itinerary:str = ""
    price:float = 0
    uid: int | str = 0

    @rx.event
    def get_offers(self):
        self.id = self.router.page.params.get("offer_id")
        self.uid = self.router.page.params.get("uid")
        
        print(self.id)

        offer_conn = Offer("","","","","",0)
        self.id = int(self.id)
        offer_data = offer_conn.read_offer_by_id(id=self.id)
        
        for offer_row in offer_data:
            self.title = str(offer_row[1])
            self.desc = str(offer_row[2])
            self.image_url = str(offer_row[3])
            self.details = str(offer_row[4])
            self.itinerary = str(offer_row[5])
            self.price = float(offer_row[6])


def description_page() -> rx.Component:
    return render_page(
        rx.vstack(
            rx.desktop_only(
                rx.hstack(
                    rx.vstack(
                        rx.image(src=DescriptionState.image_url, width="700px", height="600px", style={"object-fit":"cover"}, border_radius="5px")
                    ),
                    rx.vstack(
                        rx.vstack(
                            rx.heading(DescriptionState.title, size="9"),
                            rx.separator(),
                            rx.text(DescriptionState.desc, size="4"
                            ),
                            rx.hstack(
                                rx.heading("Detalles", size="5"),
                                spacing="2",
                                justify="center",
                                align="center",
                            ),
                            rx.text(DescriptionState.details, size="3",
                            ),
                            rx.hstack(
                                rx.heading("Itinerario", size="5"),
                                spacing="2",
                                justify="center",
                                align="center",
                            ),
                            rx.text(DescriptionState.itinerary, size="3"),
                            rx.heading("Precio:\n", f"{DescriptionState.price:,} RD$"),
                            rx.link(
                                rx.button("Pagar", width="100%", size="3", margin_y=".5em", style={"cursor":"pointer"}),
                                href=f"/payment?id={DescriptionState.id}&uid={DescriptionState.uid}",
                                width="100%",
                                style={"cursor":"pointer"}
                            ),
                            spacing="4",
                            width="600px"
                        ),
                        justify="center",
                        spacing="4",
                        padding="1em",
                        style={
                            "background": "rgba( 0, 0, 0, 0.3 )",
                            "backdrop-filter": "blur(20px)",
                            "-webkit-backdrop-filter": "blur(20px)",
                            "border-radius": "10px",
                            "border": "1px solid rgba( 255, 255, 255, 0.18 )",
                        },
                    ),
                    spacing="6",
                    width="100%",
                    style={
                        "justify-content":"space-evenly",
                    },
                    align="center",
                ),
            ),
            padding="2.5em",
            justify="center",
            align="center",
            min_height="100dvh",
            on_mount=DescriptionState.get_offers,
        )
    )