from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


payment_option_field = (By.CSS_SELECTOR, 'span[class="select2-selection select2-selection--single"]')
name_of_the_phone = (By.CSS_SELECTOR, 'h1[class="h h--1 pdp-header-heading"]')
six_month_option = (By.CSS_SELECTOR, 'div[class="value"]')
payment_choice = (By.CSS_SELECTOR, 'span[class="select2-selection__rendered"]')
enter_and_buy_btn = (By.XPATH, '//button[@data-product-offer="17.1018803-6902_CURRENT" and '
                               '@class="button button--primary button--large"]')


class SelectedPhone(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def check_the_name_from_selected_phone(self):
        phone_name = self.find_element(name_of_the_phone).text
        return 'Apple iPhone 13 128GB темная ночь [A2633]' == phone_name

    # открыть браузер на странице выбранного телефона (Apple iPhone 13 128GB темная ночь [A2633])
    def open_selected_phone_page(self):
        self.driver.get(self.selected_phone_url)

    # проверка, что была открыта необходимая страница
    def check_that_page_of_selected_phone_was_opened(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(name_of_the_phone,
                                                    'Apple iPhone 13 128GB темная ночь [A2633]'))
        return True

    # справа из выпадающего списка выбрать вариант оплаты в рассрочку на 6 месяцев: «6 мес по ххх руб/мес»
    def choose_a_way_of_payment(self):
        self.find_element(payment_option_field).click()
        option_list = self.find_elements(six_month_option)
        option_list[2].click()

    # проверить что выбран способ оплаты «6 мес по ххх руб/мес»
    def check_that_way_of_payment_six_months(self):
        payment_detail = self.find_element(payment_choice).text
        #a = re.search('6 мес', payment_detail)
        return payment_detail

    # вывести сообщение с названием выбранного оборудования и текст выбранного варианта оплаты,
    # включая стоимость
    def view_purchase_details(self):
        phone_name = self.find_element(name_of_the_phone).text
        payment_details = self.find_element(payment_choice).text
        print(f'Выбран {phone_name}, вариант оплаты: {payment_details}')

    # нажать кнопку «Войти и купить»
    def go_on_to_purchase(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(enter_and_buy_btn))
        enter_btn = self.find_element(enter_and_buy_btn)
        self.driver.execute_script("arguments[0].click();", enter_btn)







