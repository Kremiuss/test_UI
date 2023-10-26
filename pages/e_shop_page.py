from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


btn_go_to_phone = (By.XPATH, '//span[contains(text(),"Телефоны")]')

class ShopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # открыть браузер на странице "главная/интернет-магазин/телефоны"
    def open_shop_page(self):
        self.driver.get(self.base_url)

    def go_to_phonepage(self):
        btn = self.find_element(btn_go_to_phone)
        try:
            btn.click()
        except ElementClickInterceptedException:
            print("Going to the phones causes the ElementClickInterceptedException")

    # проверка, что была открыта необходимая страница
    def check_that_a_necessary_page_was_opened(self):
        current_url = self.driver.current_url
        return current_url == self.phone_url, 'Message: Wrong page opened'
