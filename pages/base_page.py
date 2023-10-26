from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'https://www.a1.by/ru/c/shop'
        self.phone_url = 'https://www.a1.by/ru/shop/c/phones'
        self.selected_phone_url = 'https://www.a1.by/ru/shop/phones/smartphones/' \
                                 'Apple/Apple-iPhone-13/midnight/p/17.1018803'
        self.sign_in_url = 'https://asmp.a1.by/asmp/LoginMasterServlet?service=Portal&cookie=skip&level' \
                           '=20&userRequestURL=https%3A%2F%2Fwww.a1.by%2Fru%2Fsize-term%3FproductCode%3D17.' \
                           '1018803%26productOffering%3D17.1018803-4802_CURRENT%26fromSSO%3Dtrue'

    def find_element(self, args: tuple):
        by_name, by_value = args
        return self.driver.find_element(by_name, by_value)

    def find_elements(self, args: tuple):
        by_name, by_value = args
        return self.driver.find_elements(by_name, by_value)





