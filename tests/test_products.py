import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.data_reader import read_csv


product_data = read_csv("products.csv")

product_names = [
    product["product_name"]
    for product in product_data
]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "product_name",
    product_names,
    ids=product_names
)
def test_search_for_product(page: Page, product_name: str):
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.go_to_products_page()

    products_page.verify_products_page_is_open()
    products_page.search_for_product(product_name)
    products_page.verify_product_is_displayed(product_name)