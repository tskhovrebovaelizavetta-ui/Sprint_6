import allure
import pytest
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.page_order import OrderPageLocators


@allure.feature('Оформление заказа')
class TestOrderPage:
    @allure.title('Позитивный сценарий оформления заказа')
    @allure.description(
        'Тест проверяет успешное оформление заказа через верхнюю кнопку Заказать.'
    )
    def test_make_order_success_from_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.click_top_order_button()

        order_page = OrderPage(driver)
        order_page.fill_first_step(
            'Елизавета',
            'Трофимова',
            'Москва, ул. Профсоюзная, 100',
            'Беляево',
            '+79381657744'
        )
        order_page.fill_second_step(
            '20.04.2026',
            OrderPageLocators.PERIOD_1,
            OrderPageLocators.BLACK_COLOR_CHECKBOX,
            'Позвоните за час'
        )
        order_page.submit_order()

        success_text = order_page.get_success_text()
        assert 'Заказ оформлен' in success_text

    @allure.title('Позитивный сценарий оформления заказа через нижнюю кнопку')
    @allure.description(
        'Тест проверяет успешное оформление заказа через нижнюю кнопку Заказать.'
    )
    def test_make_order_success_from_bottom_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.click_bottom_order_button()

        order_page = OrderPage(driver)
        order_page.fill_first_step(
            'Елизавета',
            'Трофимова',
            'Москва, ул. Кремль, 1',
            'Сокольники',
            '+79381657744'
        )
        order_page.fill_second_step(
            '21.04.2026',
            OrderPageLocators.PERIOD_2,
            OrderPageLocators.GREY_COLOR_CHECKBOX,
            'Домофон не работает'
        )
        order_page.submit_order()

        success_text = order_page.get_success_text()
        assert 'Заказ оформлен' in success_text