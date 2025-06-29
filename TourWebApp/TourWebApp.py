import reflex as rx
from .Pages.homepage import home_page
from .Pages.descriptionpage import description_page
from .Pages.paymentpage import payment_page
from .Pages.loginpage import login_page
from .Pages.registerpage import register_page
from .Pages.Admin.adminpage import admin_page
from .Pages.Admin.Contacts.mainpage import contacts_page
from .Pages.Admin.Offers.mainpage import offers_page
from .Pages.Admin.Schedules.mainpage import schedules_page
from .Pages.Admin.Transactions.mainpage import transaction_page
from .Pages.Admin.Users.mainpage import users_page
from rxconfig import config

app = rx.App(
    theme=rx.theme(
        accent_color="blue",
        panel_background="solid",
        appearance="dark",
        color_mode="dark",
    ),
)

# Registration Managment Pages
app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register"),

# Pages
app.add_page(home_page, route="/home")
app.add_page(description_page, route="/description")
app.add_page(payment_page, route="/payment")

#Admin
app.add_page(admin_page, route="/admin")
app.add_page(contacts_page, route="/admin/contacts")
app.add_page(offers_page, route="/admin/offers")
app.add_page(schedules_page, route="/admin/schedules")
app.add_page(transaction_page, route="/admin/transactions")
app.add_page(users_page, route="/admin/users")