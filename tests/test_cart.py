import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_cart_icon_is_visible(page: Page):
    login = LoginPage(page)
    login.login_as_standard_user()

    cart = CartPage(page)
    cart.verify_cart_icon_visible()


def test_add_to_cart_updates_badge(page: Page):
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    products.add_backpack_to_cart()

    cart = CartPage(page)
    cart.verify_cart_badge_shows("1")


def test_add_multiple_items_to_cart(page: Page):
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    products.add_backpack_to_cart()
    products.add_bike_light_to_cart()
    products.add_tshirt_to_cart()

    cart = CartPage(page)
    cart.verify_cart_badge_shows("3")


def test_clicking_cart_opens_cart_page(page: Page):
    login = LoginPage(page)
    login.login_as_standard_user()

    cart = CartPage(page)
    cart.click_cart_icon()
    cart.verify_on_cart_page()


def test_added_item_appears_in_cart(page: Page):
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    product_name = products.get_first_product_name()
    products.add_backpack_to_cart()

    cart = CartPage(page)
    cart.click_cart_icon()
    cart.verify_item_in_cart(product_name)


def test_remove_button_appears_after_add_to_cart(page: Page):
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    products.add_backpack_to_cart()

    remove_button = page.locator("[data-test='remove-sauce-labs-backpack']")
    expect(remove_button).to_be_visible()
    expect(remove_button).to_have_text("Remove")


def test_remove_from_cart_updates_badge(page: Page):
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    products.add_backpack_to_cart()

    cart = CartPage(page)
    cart.verify_cart_badge_shows("1")

    products.remove_backpack()
    cart.verify_cart_badge_not_visible()


def test_cart_persists_after_reload(page: Page):
    """P1"""
    login = LoginPage(page)
    login.login_as_standard_user()

    products = ProductsPage(page)
    cart = CartPage(page)

    products.add_backpack_to_cart()
    page.reload()

    expect(cart.cart_badge).to_have_text("1")