import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.page_order import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Заполнить первый шаг оформления заказа')
    def fill_first_step(self, name, lastname, address, metro, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.LASTNAME_INPUT, lastname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.send_keys(OrderPageLocators.METRO_INPUT, metro)
        self.send_keys(OrderPageLocators.METRO_INPUT, Keys.ARROW_DOWN)
        self.send_keys(OrderPageLocators.METRO_INPUT, Keys.ENTER)
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить второй шаг оформления заказа')
    def fill_second_step(self, date, rental_period_locator, color_locator, comment):
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_element(rental_period_locator)
        self.click_element(color_locator)
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Подтвердить оформление заказа')
    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Получить текст успешного оформления заказа')
    def get_success_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_MODAL_HEADER)