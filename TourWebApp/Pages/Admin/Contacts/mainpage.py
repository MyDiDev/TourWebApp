import reflex as rx
from ....DB.connection import Contact

class State(rx.State):
    contacts: list[dict] = []

    def get_data(self):
        contact_connection = Contact("", "", "")
        tuple_data = contact_connection.read_contact()
        
        self.contacts = [
            {
                "id":str(contact[0]),
                "name":str(contact[1]),
                "email":str(contact[2]),
                "message":str(contact[3]),
            }
            for contact in tuple_data
        ]

        print(self.contacts)

    def delete_row(self, id:str):
        print(f"Deleting row with ID: {id}")
        contact_connection = Contact("", "", "")
        contact_connection.del_contact(int(id))

        self.get_data()
        yield rx.toast.info("Registro Eliminado")
        return

    def add_row(self, data):
        name = data["name"]
        email = data["email"]
        message = data["message"]

        contact_connection = Contact(name, email, message)
        contact_connection.add_contact()
        self.get_data()
        yield rx.toast.success("Registro Agregado Exitosamente", close_button=True)

    def update_row(self, data):
        id = int(data["id"])
        name = data["name"]
        email = data["email"]
        message = data["message"]

        contact_connection = Contact(name, email, message)
        contact_connection.upt_contact(id)
        self.get_data()
        yield rx.toast.success("Registro Actualizado Exitosamente", close_button=True)


def contact_row(contact) -> rx.Component:
    return rx.table.row(
        rx.table.cell(contact["id"]),
        rx.table.cell(contact["name"]),
        rx.table.cell(contact["email"]),
        rx.table.cell(contact["message"]),
        rx.table.cell(
            rx.hstack(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button("Actualizar", size="1"),
                    ),
                    rx.dialog.content(
                        rx.heading("Actualizar Registro", font_size="40px", margin_y=".5em"),
                        rx.form(
                            rx.input(name="id", type="hidden", value=contact["id"], display="none"),
                            rx.vstack(
                                rx.text("Nombre:", size="4"),
                                rx.input(placeholder="Ingrese el nombre o nombre de usuario", name="name", type="text", size='3', width="100%", default_value=contact["name"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Email:", size="4"),
                                rx.input(placeholder="Ingrese el email de la cuenta", name="email", type="email", size='3', width="100%", default_value=contact["email"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Mensaje:", size="4"),
                                rx.input(placeholder="Ingrese el Mensaje", name="message", type="text", size='3', width="100%", default_value=contact["message"]),
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
                rx.button("Eliminar", size="1", on_click=lambda id=contact["id"]: State.delete_row(id), color_scheme="red"),
            )
        )
    )


def contact_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID", size="6"),
                rx.table.column_header_cell("Nombre", size="6"),
                rx.table.column_header_cell("Email", size="6"),
                rx.table.column_header_cell("Mensaje", size="6"),
                rx.table.column_header_cell("Acciones", size="6"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                State.contacts, 
                contact_row
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

def contacts_page() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.desktop_only(
                rx.vstack(
                    rx.box(
                        rx.box(
                            rx.heading("Contactos", size="9", margin_y=".5em"),
                            rx.dialog.root(
                                rx.dialog.trigger(
                                  rx.button("Agregar", size="3", width="25%", style={"cursor":"pointer"}),
                                ),
                                rx.dialog.content(
                                    rx.heading("Agregar Registro", font_size="40px", margin_y=".5em"),
                                    rx.form(
                                        rx.vstack(
                                            rx.text("Nombre:", size="4"),
                                            rx.input(placeholder="Ingrese el nombre o nombre de usuario", name="name", type="text", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Email:", size="4"),
                                            rx.input(placeholder="Ingrese el email de la cuenta", name="email", type="email", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Mensaje:", size="4"),
                                            rx.input(placeholder="Ingrese el Mensaje", name="message", type="text", size='3', width="100%"),
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
                        contact_table(),
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