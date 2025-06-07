import reflex as rx
from ....DB.connection import Schedule

class State(rx.State):
    data: list[dict] = []

    def get_data(self):
        schedule_conn = Schedule("","","",0,0,0,"",0)
        tuple_data = schedule_conn.read_schedule()
        
        self.data = [
            {
                "id":int(schedule[0]),
                "nombre_completo": str(schedule[1]),
                "email": str(schedule[2]),
                "telefono": str(schedule[3]),
                "id_tour": int(schedule[4]),
                "id_usuario": int(schedule[5]),
                "id_pago": int(schedule[6]),
                "fecha_reserva": str(schedule[7]),
                "cantidad_personas": int(schedule[8]),
            }
            for schedule in tuple_data
        ]

        print(self.data)

    def delete_row(self, id:str):
        print(f"Deleting row with ID: {id}")
        schedule_conn = Schedule("","","",0,0,0,"",0)
        schedule_conn.del_schedule(int(id))

        self.get_data()
        yield rx.toast.info("Registro Eliminado")
        return

    def add_row(self, data):
        nombre_completo = data.get("nombre_completo")
        email = data.get("email")
        telefono = data.get("telefono")
        id_tour = int(data.get("id_tour"))
        id_usuario = int(data.get("id_usuario"))
        id_pago = int(data.get("id_pago"))
        fecha_reserva = data.get("fecha_reserva")
        cantidad_personas = int(data.get("cantidad_personas"))

        schedule_conn = Schedule(nombre_completo, email, telefono, id_tour, id_usuario, id_pago, fecha_reserva, cantidad_personas)
        try:
            schedule_conn.add_schedule()
        except Exception:
            yield rx.toast.error("Ingrese identificatores registardos")

        self.get_data()
        yield rx.toast.success("Reserva Agregada Exitosamente", close_button=True)

    def update_row(self, data):
        nombre_completo = data.get("nombre_completo")
        email = data.get("email")
        telefono = data.get("telefono")
        id_tour = int(data.get("id_tour"))
        id_usuario = int(data.get("id_usuario"))
        id_pago = int(data.get("id_pago"))
        fecha_reserva = data.get("fecha_reserva")
        cantidad_personas = int(data.get("cantidad_personas"))        

        schedule_conn = Schedule(nombre_completo, email, telefono, id_tour, id_usuario, id_pago, fecha_reserva, cantidad_personas)
        try:
            schedule_conn.upt_schedule(id)
        except Exception:
            yield rx.toast.error("Ingrese identificatores registardos")
            
        self.get_data()
        yield rx.toast.success("Registro Actualizado Exitosamente", close_button=True)


def data_row(schedule) -> rx.Component:
    return rx.table.row(
        rx.table.cell(schedule["id"]),
        rx.table.cell(schedule["nombre_completo"]),
        rx.table.cell(schedule["email"]),
        rx.table.cell(schedule["telefono"]),
        rx.table.cell(str(schedule["id_tour"])),
        rx.table.cell(str(schedule["id_usuario"])),
        rx.table.cell(str(schedule["id_pago"])),
        rx.table.cell(str(schedule["fecha_reserva"])),
        rx.table.cell(str(schedule["cantidad_personas"])),
        rx.table.cell(
            rx.hstack(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button("Actualizar", size="1"),
                    ),
                    rx.dialog.content(
                        rx.heading("Actualizar Registro", font_size="40px", margin_y=".5em"),
                        rx.form(
                            rx.input(display="none", name="id", default_value=schedule["id"]),
                            rx.vstack(
                                rx.text("Nombre Completo:", size="4"),
                                rx.input(name="nombre_completo", placeholder="Ingrese el nombre completo", type="text", default_value=schedule["nombre_completo"], width="100%"),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Email:", size="4"),
                                rx.input(name="email", placeholder="Ingrese el correo electrónico", type="email", default_value=schedule["email"], width="100%"),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Teléfono:", size="4"),
                                rx.input(name="telefono", placeholder="Ingrese el número de teléfono", type="tel", default_value=schedule["telefono"], width="100%"),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("ID del Tour:", size="4"),
                                rx.input(name="id_tour", placeholder="ID del Tour", type="number", default_value=str(schedule["id_tour"]), width="100%"),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Email de Usuario:", size="4"),
                                rx.input(name="id_usuario", placeholder="ID del Usuario", type="number", default_value=str(schedule["id_usuario"]), width="100%"),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("ID de Pago:", size="4"),
                                rx.input(name="id_pago", placeholder="ID del Pago", type="number", default_value=str(schedule["id_pago"]), width="100%"),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Fecha de Reserva:", size="4"),
                                rx.input(name="fecha_reserva", placeholder="YYYY-MM-DD", type="date", default_value=schedule["fecha_reserva"], width="100%"),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Cantidad de Personas:", size="4"),
                                rx.input(name="cantidad_personas", placeholder="Cantidad", type="number", default_value=str(schedule["cantidad_personas"]), width="100%"),
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
                rx.button("Eliminar", size="1", on_click=lambda id=schedule["id"]: State.delete_row(id), color_scheme="red"),
            )
        )
    )


def schedules_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID", size="6"),
                rx.table.column_header_cell("Nombre Completo", size="6"),
                rx.table.column_header_cell("Email", size="6"),
                rx.table.column_header_cell("Teléfono", size="6"),
                rx.table.column_header_cell("ID Tour", size="6"),
                rx.table.column_header_cell("ID Usuario", size="6"),
                rx.table.column_header_cell("ID Pago", size="6"),
                rx.table.column_header_cell("Fecha de Reserva", size="6"),
                rx.table.column_header_cell("Cantidad de Personas", size="6"),
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

def schedules_page() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.desktop_only(
                rx.vstack(
                    rx.box(
                        rx.box(
                            rx.heading("Reservas", size="9", margin_y=".5em"),
                            rx.dialog.root(
                                rx.dialog.trigger(
                                  rx.button("Agregar", size="3", width="25%", style={"cursor":"pointer"}),
                                ),
                                rx.dialog.content(
                                    rx.heading("Agregar Reserva", font_size="40px", margin_y=".5em"),
                                    rx.form(
                                        rx.vstack(
                                            rx.text("Nombre Completo:", size="4"),
                                            rx.input(name="nombre_completo", placeholder="Ingrese el nombre completo", type="text", width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Email:", size="4"),
                                            rx.input(name="email", placeholder="Ingrese el correo electrónico", type="email", width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Teléfono:", size="4"),
                                            rx.input(name="telefono", placeholder="Ingrese el número de teléfono", type="tel",  width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("ID del Tour:", size="4"),
                                            rx.input(name="id_tour", placeholder="ID del Tour", type="number",  width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("ID de Usuario:", size="4"),
                                            rx.input(name="id_usuario", placeholder="ID del Usuario", type="number", width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("ID de Pago:", size="4"),
                                            rx.input(name="id_pago", placeholder="ID del Pago", type="number",  width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Fecha de Reserva:", size="4"),
                                            rx.input(name="fecha_reserva", placeholder="YYYY-MM-DD", type="date", width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Cantidad de Personas:", size="4"),
                                            rx.input(name="cantidad_personas", placeholder="Cantidad", type="number", width="100%"),
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
                        schedules_table(),
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