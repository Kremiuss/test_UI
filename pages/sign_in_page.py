from pages.base_page import BasePage
from selenium.webdriver.common.by import By

sign_in_title = (By.CSS_SELECTOR, 'h1[class="h h--2"]')


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # открыть браузер на странице входа в аккаунт
    def open_sign_in_page(self):
        self.driver.get(self.sign_in_url)

    @property
    def check_that_jump_to_sign_in_page_was_completed(self):
        title = self.find_element(sign_in_title).text
        return 'Вход в аккаунт' == title
