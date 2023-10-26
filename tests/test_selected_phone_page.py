from pages.selected_phone_page import SelectedPhone
from pages.sign_in_page import SignInPage
import pytest


@pytest.mark.selected_phone_page
def test_open_smartfonemodel(driver):
    selected_phone_page = SelectedPhone(driver)
    selected_phone_page.open_selected_phone_page()
    assert selected_phone_page.check_that_page_of_selected_phone_was_opened()


def test_choose_payment_method(driver):
    selected_phone_page = SelectedPhone(driver)
    selected_phone_page.open_selected_phone_page()
    selected_phone_page.choose_a_way_of_payment()
    assert selected_phone_page.check_that_way_of_payment_six_months()

