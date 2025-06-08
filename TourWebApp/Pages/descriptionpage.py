import reflex as rx
from .homepage import render_page
from ..DB.connection import Offer

class DescriptionState(rx.State):
    offer: list[dict] = []
    
    @rx.event
    def get_offer(self) -> None:
        offer_conn = Offer("","","","","",0)
        id = int(rx.State.router_data.get("id"))
        offer_data = offer_conn.read_offer_by_id(id=id)

        self.offer = [
            {
                "id":int(offer_row[0]),
                "title":str(offer_row[1]),
                "description":str(offer_row[2]),
                "image_url":str(offer_row[3]),
                "details":str(offer_row[4]),
                "itinerary":str(offer_row[5]),
                "price":float(offer_row[6]),
            }
            for offer_row in offer_data
        ]

        print(self.offer)
        print(self.offer[0][0])


def description_page() -> rx.Component:
    return render_page(
        rx.box(
            rx.desktop_only(
                rx.hstack(
                    rx.vstack(
                        rx.image(DescriptionState.offer["image_url"], width="700px", height="500px", style={"object-fit":"cover"}, border_radius="5px")
                    ),
                    rx.vstack(
                        rx.box(
                            rx.heading(str(DescriptionState.offer["title"]).capitalize(), size="8"),
                            rx.text(DescriptionState.offer["description"], size="4"),
                        ),
                        rx.box(
                            rx.text(DescriptionState.offer["details"], size="4"),
                            rx.text(DescriptionState.offer["itinerary"], size="4"),
                        ),
                        rx.box(
                            rx.heading("Precio:", rx.text(str(DescriptionState.offer["price"]))),
                            rx.link(
                                rx.button("Pagar", width="100%", size="3"),
                                href=f"/payment?id={DescriptionState.offer['id']}"
                            )
                        )
                    ),
                )
            ),
            rx.tablet_only(),
            rx.mobile_only(),
        )
    )