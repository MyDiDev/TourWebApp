import reflex as rx
from ....DB.connection import Offer
from ....Uploader.uploader import upload_image

class State(rx.State):
    data: list[dict] = []
    image_url: str = ""

    def get_data(self):
        offer_connection = Offer("", "", "","","",0)
        tuple_data = offer_connection.read_offer()
        
        self.data = [
            {
                "id":int(offer[0]),
                "title":str(offer[1]),
                "description":str(offer[2]),
                "image_url":str(offer[3]),
                "details":str(offer[4]),
                "itinerary":str(offer[5]),
                "price":float(offer[6]),
            }
            for offer in tuple_data
        ]

        print(self.data)

    def handle_upload(self, file: list[rx.UploadFile]):
        for uploaded_file in file:
            self.image_url = upload_image(uploaded_file.file.read())
            print("image uploaded")

    def delete_row(self, id:str):
        print(f"Deleting row with ID: {id}")
        offer_connection = Offer("", "", "","","",0)
        offer_connection.del_offer(int(id))

        self.get_data()
        yield rx.toast.info("Registro Eliminado")
        return

    def add_row(self, data):
        title = data.get("title")
        description = data.get("description")
        image = data.get("description")
        image_url = self.image_url
        details = data.get("details")
        itinerary = data.get("itinerary")
        price = float(data.get("price"))
        

        offer_connection = Offer(title, description, image_url, details, itinerary, price)
        offer_connection.add_offer()
        self.get_data()
        yield rx.toast.success("Oferta Agregada Exitosamente", close_button=True)

    def update_row(self, data):
        id = int(data["id"])
        title = data.get("title")
        description = data.get("description")
        image = data.get("description")
        image_url = self.image_url
        details = data.get("details")
        itinerary = data.get("itinerary")
        price = data.get("price")
        

        offer_connection = Offer(title, description, image_url, details, itinerary, price)
        offer_connection.upt_offer(id)
        self.get_data()
        yield rx.toast.success("Registro Actualizado Exitosamente", close_button=True)


def data_row(offer) -> rx.Component:
    return rx.table.row(
        rx.table.cell(offer["id"]),
        rx.table.cell(offer["title"]),
        rx.table.cell(offer["description"]),
        rx.table.cell(offer["image_url"]),
        rx.table.cell(offer["details"]),
        rx.table.cell(offer["itinerary"]),
        rx.table.cell(offer["price"]),
        rx.table.cell(
            rx.hstack(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button("Actualizar", size="1"),
                    ),
                    rx.dialog.content(
                        rx.heading("Actualizar Registro", font_size="40px", margin_y=".5em"),
                        rx.form(
                            rx.input(display="none", name="id", default_value=offer["id"]),
                            rx.vstack(
                                rx.text("Ingrese la imagen:", size="4"),
                                rx.upload(id="upload"),
                                rx.button(
                                    "Subir Imagen",
                                    on_click=State.handle_upload(rx.upload_files("upload")),
                                ),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Titulo:", size="4"),
                                rx.input(placeholder="Ingrese el titulo", name="title", type="text", size='3', width="100%", default_value=offer["title"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Descripcion:", size="4"),
                                rx.input(placeholder="Ingrese la descripcion", name="description", type="text", size='3', width="100%", default_value=offer["description"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Detalles:", size="4"),
                                rx.input(placeholder="Ingrese los detalles", name="details", type="text", size='3', width="100%", default_value=offer["details"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Itinerario:", size="4"),
                                rx.input(placeholder="Ingrese el itinerario", name="itinerary", type="text", size='3', width="100%", default_value=offer["itinerary"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Precio:", size="4"),
                                rx.input(placeholder="Ingrese el precio", name="price", type="number", size='3', width="100%", default_value=offer["price"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.button("Actualizar", type="submit", size="3", width="100%", style={"cursor":"pointer"}),
                                margin_y="1.5em",
                            ),
                            on_submit=State.update_row,
                        ),
                        width="85%",
                        padding="1em",
                        style={
                            "background": "rgba( 0, 0, 0, 0.3 )",
                            "backdrop-filter": "blur(20px)",
                            "-webkit-backdrop-filter": "blur(20px)",
                            "border-radius": "10px",
                            "border": "1px solid rgba( 255, 255, 255, 0.18 )",
                        },
                    ),
                ),
                rx.button("Eliminar", size="1", on_click=lambda id=offer["id"]: State.delete_row(id), color_scheme="red"),
            )
        )
    )


def offers_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID", size="6"),
                rx.table.column_header_cell("Titulo", size="6"),
                rx.table.column_header_cell("Descripcion", size="6"),
                rx.table.column_header_cell("URL Imagen", size="6"),
                rx.table.column_header_cell("Detalles", size="6"),
                rx.table.column_header_cell("Itinerario", size="6"),
                rx.table.column_header_cell("Precio", size="6"),
                rx.table.column_header_cell("", size="6"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State.data, 
                data_row
            ),
        ),
        on_mount=State.get_data,
        style={
            "background": "rgba( 0, 0, 0, 0.3 )",
            "backdrop-filter": "blur(20px)",
            "-webkit-backdrop-filter": "blur(20px)",
            "border-radius": "10px",
            "border": "1px solid rgba( 255, 255, 255, 0.18 )",
        },
        padding="1em",
        width="100%",
    )

def offers_page() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.desktop_only(
                rx.vstack(
                    rx.box(
                        rx.box(
                            rx.heading("Ofertas", size="9", margin_y=".5em"),
                            rx.dialog.root(
                                rx.dialog.trigger(
                                  rx.button("Agregar", size="3", width="25%", style={"cursor":"pointer"}),
                                ),
                                rx.dialog.content(
                                    rx.heading("Agregar Oferta", font_size="40px", margin_y=".5em"),
                                    rx.form(
                                        rx.vstack(
                                            rx.text("Ingrese la imagen:", size="4"),
                                            rx.upload(id="upload"),
                                            rx.button(
                                                "Subir Imagen",
                                                on_click=State.handle_upload(rx.upload_files("upload")),
                                            ),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Titulo:", size="4"),
                                            rx.input(placeholder="Ingrese el titulo", name="title", type="text", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Descripcion:", size="4"),
                                            rx.input(placeholder="Ingrese la descripcion", name="description", type="text", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Detalles:", size="4"),
                                            rx.input(placeholder="Ingrese los detalles", name="details", type="text", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Itinerario:", size="4"),
                                            rx.input(placeholder="Ingrese el itinerario", name="itinerary", type="text", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Precio:", size="4"),
                                            rx.input(placeholder="Ingrese el precio", name="price", type="number", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.button("Agregar", type="submit", size="3", width="100%", style={"cursor":"pointer"}),
                                            margin_y="1.5em",
                                        ),
                                        on_submit=State.add_row
                                    ),
                                    width="85%",
                                    padding="1em",
                                    style={
                                        "background": "rgba( 0, 0, 0, 0.3 )",
                                        "backdrop-filter": "blur(20px)",
                                        "-webkit-backdrop-filter": "blur(20px)",
                                        "border-radius": "10px",
                                        "border": "1px solid rgba( 255, 255, 255, 0.18 )",
                                    },
                                ),
                            ),
                            margin_y="1.5em",
                        ),
                        offers_table(),
                        width="75%",
                    ),
                    justify="center",
                    align="center",
                    width="100%"
                ),
            ),
            rx.tablet_only(),
            rx.desktop_only(),
        )
    )