import reflex as rx
from .Pages.homepage import home_page
from .Pages.loginpage import login_page
from .Pages.registerpage import register_page
from .Pages.Admin.adminpage import admin_page
from rxconfig import config

app = rx.App(
    theme=rx.theme(
        accent_color="blue",
        panel_background="solid",
        appearance="dark",
        color_mode="dark",
    )
)

# Registration Managment Pages
app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register"),

# Pages
app.add_page(home_page, route="/home")

#Admin page
app.add_page(admin_page, route="/admin")