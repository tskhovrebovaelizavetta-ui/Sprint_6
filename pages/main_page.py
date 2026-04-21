import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators, HeaderLocators


class MainPage(BasePage):
    @allure.step('Нажать верхнюю кнопку Заказать')
    def click_top_order_button(self):
        self.click_element(HeaderLocators.TOP_ORDER_BUTTON)

    @allure.step('Нажать нижнюю кнопку Заказать')
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Открыть вопрос FAQ и получить ответ')
    def open_question_and_get_answer(self, question_locator, answer_locator):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)
        self.click_element(question_locator)
        return self.wait.until(
            EC.visibility_of_element_located(answer_locator)
        ).text
    
    @allure.step('Проверить, что открыта главная страница Самоката')
    def is_opened_main_page(self):
        return 'qa-scooter.praktikum-services.ru' in self.get_current_url()

    @allure.step('Проверить, что открыта страница Дзена')
    def is_opened_dzen_page(self):
        return 'dzen.ru' in self.get_current_url()