from playwright.sync_api import Page
from pages.products_page import ProductsPage
from pages.login_page import LoginPage


def test_sort_price_low_to_high(page: Page):
    """P1"""
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    products.select_sort_option("lohi")

    prices = products.get_all_prices()
    assert prices == sorted(prices)


def test_sort_price_high_to_low(page: Page):
    """P1"""
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    products.select_sort_option("hilo")

    prices = products.get_all_prices()
    assert prices == sorted(prices, reverse=True)


def test_sort_name_a_to_z(page: Page):
    """P1"""
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    products.select_sort_option("az")

    names = products.product_names.all_inner_texts()
    assert names == sorted(names)


def test_sort_name_z_to_a(page: Page):
    """P1"""
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    products.select_sort_option("za")

    names = products.product_names.all_inner_texts()
    assert names == sorted(names, reverse=True)