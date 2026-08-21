import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage


@pytest.mark.smoke
def test_add_product_to_cart(page: Page):
    product_name = "Blue Top"

    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.go_to_products_page()

    products_page.verify_products_page_is_open()
    products_page.search_for_product(product_name)
    products_page.verify_product_is_displayed(product_name)

    products_page.add_product_to_cart(product_name)
    products_page.go_to_cart_from_modal()

    cart_page.verify_cart_page_is_open()
    cart_page.verify_product_is_in_cart(product_name)