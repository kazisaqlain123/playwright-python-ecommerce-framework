import pytest
from playwright.sync_api import Page

from pages.account_page import AccountPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_confirmation_page import OrderConfirmationPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from utils.data_reader import read_json


payment_data = read_json("payment.json")


@pytest.mark.e2e
def test_complete_checkout(
    page: Page,
    registered_user: dict[str, str]
):
    product_name = "Blue Top"

    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)
    order_confirmation_page = OrderConfirmationPage(page)

    home_page.open()
    home_page.go_to_login_page()

    login_page.login(
        email=registered_user["email"],
        password=registered_user["password"]
    )

    account_page.verify_logged_in_as(
        registered_user["name"]
    )

    home_page.go_to_products_page()

    products_page.verify_products_page_is_open()
    products_page.search_for_product(product_name)
    products_page.add_product_to_cart(product_name)
    products_page.go_to_cart_from_modal()

    cart_page.verify_cart_page_is_open()
    cart_page.verify_product_is_in_cart(product_name)
    cart_page.proceed_to_checkout()

    checkout_page.verify_checkout_page_is_open()
    checkout_page.verify_delivery_and_billing_addresses(
        registered_user
    )
    checkout_page.add_order_comment(
        "Please process this automation test order."
    )
    checkout_page.place_order()

    payment_page.verify_payment_page_is_open()
    payment_page.enter_payment_details(payment_data)
    payment_page.pay_and_confirm_order()

    order_confirmation_page.verify_order_was_placed()