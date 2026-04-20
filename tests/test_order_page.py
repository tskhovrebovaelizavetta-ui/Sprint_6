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
        'Тест проверяет успешное оформление заказа через верхнюю и нижнюю '
        'кнопки Заказать с разными тестовыми данными.'
    )
    @pytest.mark.parametrize(
        'button_type, name, lastname, address, metro, phone, date, period_locator, color_locator, comment',
        [
            (
                'top',
                'Елизавета',
                'Трофимова',
                'Москва, ул. Профсоюзная, 100',
                'Беляево',
                '+79381657744',
                '20.04.2026',
                (By.XPATH, "//div[text()='сутки']"),
                OrderPageLocators.BLACK_COLOR_CHECKBOX,
                'Позвоните за час'
            ),
            (
                'bottom',
                'Елизавета',
                'Трофимова',
                'Москва, ул. Кремль, 1',
                'Сокольники',
                '+79381657744',
                '21.04.2026',
                (By.XPATH, "//div[text()='двое суток']"),
                OrderPageLocators.GREY_COLOR_CHECKBOX,
                'Домофон не работает'
            )
        ]
    )
    def test_make_order_success(
        self, driver, button_type, name, lastname, address, metro, phone,
        date, period_locator, color_locator, comment
    ):
        main_page = MainPage(driver)
        main_page.accept_cookie()

        if button_type == 'top':
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page = OrderPage(driver)
        order_page.fill_first_step(name, lastname, address, metro, phone)
        order_page.fill_second_step(date, period_locator, color_locator, comment)
        order_page.submit_order()

        success_text = order_page.get_success_text()
        assert 'Заказ оформлен' in success_text