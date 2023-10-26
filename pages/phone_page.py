from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

btn_go_to_purchase = (By.XPATH, '//a[@class=" button--centered button button--primary" '
                                'and @id="product-tile-button_2"]')
name_of_the_selected_phone = (By.XPATH, '//div[text(), "Apple iPhone 13 128GB темная ночь [A2633]"')


class PhonePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # открыть браузер на странице "главная/интернет-магазин/телефоны"
    def open_phone_page(self):
        self.driver.get(self.phone_url)

    # проверка, что была открыта необходимая страница
    def check_that_a_necessary_page_was_opened(self):
        current_url = self.driver.current_url
        return current_url == self.phone_url, 'Message: Wrong page opened'

    # на странице выбрать случайным образом блок со смартфоном и нажать на кнопку «Перейти к покупке»
    # (Apple iPhone 13 128GB темная ночь [A2633])
    def go_to_the_purchase_of_the_selected_phone(self):
        btn = self.find_element(btn_go_to_purchase)
        try:
            btn.click()
        except ElementClickInterceptedException:
            print("Going to the purchase causes the ElementClickInterceptedException")
        finally:
            self.driver.execute_script("arguments[0].click();", btn)












