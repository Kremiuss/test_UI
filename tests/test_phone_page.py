import pytest
from pages.phone_page import PhonePage
from pages.selected_phone_page import SelectedPhone
from pages.e_shop_page import ShopPage


def test_goto_phone_page(driver):
    shop_page = ShopPage(driver)
    shop_page.open_shop_page()
    assert shop_page.check_that_a_necessary_page_was_opened()


@pytest.mark.phones_page
def test_check_page_opened(driver):
    phone_page = PhonePage(driver)
    phone_page.open_phone_page()
    assert phone_page.check_that_a_necessary_page_was_opened()


def test_choose_the_purchase(driver):
    phone_page = PhonePage(driver)
    phone_page.open_phone_page()
    phone_page.go_to_the_purchase_of_the_selected_phone()
    selected_phone_page = SelectedPhone(driver)
    selected_phone_page.open_selected_phone_page()
    assert selected_phone_page.check_the_name_from_selected_phone


