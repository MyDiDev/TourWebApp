import reflex as rx
from ....DB.connection import Transactions

class State(rx.State):
    data: list[dict] = []

    def get_data(self):
        transaction_conn = Transactions("","",0)
        tuple_data = transaction_conn.read_payments()
        
        self.data = [
            {
                "id":int(transaction[0]),
                "metodo_pago": str(transaction[1]),
                "estado_pago": str(transaction[2]),
                "monto": float(transaction[3]),
            }
            for transaction in tuple_data
        ]

        print(self.data)

    def delete_row(self, id:str):
        print(f"Deleting row with ID: {id}")
        transaction_conn = Transactions("","",0)
        transaction_conn.del_payment(int(id))

        self.get_data()
        yield rx.toast.info("Registro Eliminado")
        return

    def add_row(self, data):
        metodo_pago = data.get("metodo_pago")
        estado_pago = data.get("estado_pago")
        monto = data.get("monto")

        transaction_conn = Transactions(metodo_pago, estado_pago, monto)
        try:
            transaction_conn.add_payment()
        except Exception as e:
            yield rx.toast.error("error {e}".format(e))

        self.get_data()
        yield rx.toast.success("Pago Agregada Exitosamente", close_button=True)

    def update_row(self, data):
        metodo_pago = data.get("metodo_pago")
        estado_pago = data.get("estado_pago")
        monto = data.get("monto")     

        transaction_conn = Transactions(metodo_pago, estado_pago, monto)
        try:
            transaction_conn.upt_payment(id)
        except Exception as e:
            yield rx.toast.error("error {e}".format(e))
            
        self.get_data()
        yield rx.toast.success("Registro Actualizado Exitosamente", close_button=True)


def data_row(transaction) -> rx.Component:
    return rx.table.row(
        rx.table.cell(transaction["id"]),
        rx.table.cell(transaction["metodo_pago"]),
        rx.table.cell(transaction["estado_pago"]),
        rx.table.cell(str(transaction["monto"])),
        rx.table.cell(
            rx.hstack(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button("Actualizar", size="1"),
                    ),
                    rx.dialog.content(
                        rx.heading("Actualizar Registro", font_size="40px", margin_y=".5em"),
                        rx.form(
                            rx.input(display="none", name="id", default_value=transaction["id"]),
                            rx.vstack(
                                rx.text("Método de Pago:", size="4"),
                                rx.input(name="metodo_pago", placeholder="Ingrese el método de pago", type="text", default_value=transaction["metodo_pago"], width="100%"),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Estado de Pago:", size="4"),
                                rx.input(name="estado_pago", placeholder="Ingrese el estado de pago", type="text", default_value=transaction["estado_pago"], width="100%"),
                                spacing="3",
                                margin_y="1.5em",
                            ),
                            rx.vstack(
                                rx.text("Monto:", size="4"),
                                rx.input(name="monto", placeholder="Ingrese el monto", type="number", default_value=transaction["monto"], width="100%"),
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
                rx.button("Eliminar", size="1", on_click=lambda id=transaction["id"]: State.delete_row(id), color_scheme="red"),
            )
        )
    )


def transaction_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID", size="6"),
                rx.table.column_header_cell("Método de Pago", size="6"),
                rx.table.column_header_cell("Estado del Pago", size="6"),
                rx.table.column_header_cell("Monto", size="6"),
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

def transaction_page() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.desktop_only(
                rx.vstack(
                    rx.box(
                        rx.box(
                            rx.heading("Pagos", size="9", margin_y=".5em"),
                            rx.dialog.root(
                                rx.dialog.trigger(
                                  rx.button("Agregar", size="3", width="25%", style={"cursor":"pointer"}),
                                ),
                                rx.dialog.content(
                                    rx.heading("Agregar Pago", font_size="40px", margin_y=".5em"),
                                    rx.form(
                                        rx.vstack(
                                            rx.text("Método de Pago:", size="4"),
                                            rx.input(name="metodo_pago", placeholder="Ingrese el método de pago", type="text", width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Estado de Pago:", size="4"),
                                            rx.input(name="estado_pago", placeholder="Ingrese el estado de pago", type="text", width="100%"),
                                            spacing="3",
                                            margin_y="1.5em",
                                        ),
                                        rx.vstack(
                                            rx.text("Monto:", size="4"),
                                            rx.input(name="monto", placeholder="Ingrese el monto", type="number", width="100%"),
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
                        transaction_table(),
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