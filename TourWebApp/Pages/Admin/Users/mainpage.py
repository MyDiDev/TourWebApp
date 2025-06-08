import reflex as rx
from ....DB.connection import User

class State(rx.State):
    data: list[dict] = []
    image_url: str = ""

    def get_data(self):
        user_connection = User("","","","")
        tuple_data = user_connection.read_user()
        
        self.data = [
            {
                "id":int(user[0]),
                "name":str(user[1]),
                "email":str(user[2]),
                "password":str(user[3]),
                "type":str(user[4]),
            }
            for user in tuple_data
        ]

        print(self.data)


    def delete_row(self, id:str):
        print(f"Deleting row with ID: {id}")
        user_connection = User("","","","")
        user_connection.del_user(int(id))

        self.get_data()
        yield rx.toast.info("Registro Eliminado")
        return

    def add_row(self, data):
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        type = data.get("type")
        
        user_connection = User(username, email, password, type)
        user_connection.add_user()
        self.get_data()
        yield rx.toast.success("Registro Agregado Exitosamente", close_button=True)

    def update_row(self, data):
        id = int(data["id"])
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        type = data.get("type")

        user_connection = User(username, email, password, type)
        user_connection.upt_user(id)
        self.get_data()
        yield rx.toast.success("Registro Actualizado Exitosamente", close_button=True)


def data_row(user_data) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user_data["id"]),
        rx.table.cell(user_data["name"]),
        rx.table.cell(user_data["email"]),
        rx.table.cell(user_data["password"]),
        rx.table.cell(user_data["type"]),
        rx.table.cell(
            rx.hstack(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button("Actualizar", size="1"),
                    ),
                    rx.dialog.content(
                        rx.heading("Actualizar Registro", font_size="40px", margin_y=".5em"),
                        rx.form(
                            rx.input(display="none", name="id", default_value=user_data["id"]),
                            rx.vstack(
                                rx.text("Nombre:", size="4"),
                                rx.input(placeholder="Ingrese el nombre", name="username", type="text", size='3', width="100%", default_value=user_data["name"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Email:", size="4"),
                                rx.input(placeholder="Ingrese el correo", name="email", type="email", size='3', width="100%", default_value=user_data["email"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Contraseña:", size="4"),
                                rx.input(placeholder="Ingrese la contraseña", name="password", type="password", size='3', width="100%", default_value=user_data["password"]),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Tipo:", size="4"),
                                rx.input(placeholder="Ingrese el Tipo de usuario que es", name="type", type="text", size='3', width="100%", default_value=user_data["type"]),
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
                rx.button("Eliminar", size="1", on_click=lambda id=user_data["id"]: State.delete_row(id), color_scheme="red"),
            )
        )
    )


def users_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID", size="6"),
                rx.table.column_header_cell("Nombre", size="6"),
                rx.table.column_header_cell("Email", size="6"),
                rx.table.column_header_cell("Contraseña", size="6"),
                rx.table.column_header_cell("Tipo de usuario", size="6"),
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

def users_page() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.desktop_only(
                rx.vstack(
                    rx.box(
                        rx.box(
                            rx.heading("Usuarios", size="9", margin_y=".5em"),
                            rx.dialog.root(
                                rx.dialog.trigger(
                                  rx.button("Agregar", size="3", width="25%", style={"cursor":"pointer"}),
                                ),
                                rx.dialog.content(
                                    rx.heading("Agregar Oferta", font_size="40px", margin_y=".5em"),
                                    rx.form(
                                        rx.vstack(
                                            rx.text("Nombre:", size="4"),
                                            rx.input(placeholder="Ingrese el nombre", name="username", type="text", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Email:", size="4"),
                                            rx.input(placeholder="Ingrese el correo", name="email", type="email", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Contraseña:", size="4"),
                                            rx.input(placeholder="Ingrese la contraseña", name="password", type="password", size='3', width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Tipo:", size="4"),
                                            rx.input(placeholder="Ingrese el Tipo de usuario que es", name="type", type="text", size='3', width="100%"),
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
                        users_table(),
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