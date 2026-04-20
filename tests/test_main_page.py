import allure
import pytest

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.feature('Главная страница')
class TestMainPageFaq:
    @allure.title('Проверка ответов в блоке FAQ')
    @allure.description(
        'Тест проверяет, что при открытии каждого вопроса в блоке FAQ '
        'отображается ожидаемый текст ответа.'
    )
    @pytest.mark.parametrize(
        'question_locator, answer_locator, expected_text',
        [
            (
                MainPageLocators.QUESTION_0,
                MainPageLocators.ANSWER_0,
                'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
            ),
            (
                MainPageLocators.QUESTION_1,
                MainPageLocators.ANSWER_1,
                'Пока что у нас так: один заказ — один самокат. Если хотите '
                'покататься с друзьями, можете просто сделать несколько заказов '
                '— один за другим.'
            ),
            (
                MainPageLocators.QUESTION_2,
                MainPageLocators.ANSWER_2,
                'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая '
                'в течение дня. Отсчёт времени аренды начинается с момента, когда '
                'вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, '
                'суточная аренда закончится 9 мая в 20:30.'
            ),
            (
                MainPageLocators.QUESTION_3,
                MainPageLocators.ANSWER_3,
                'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
            ),
            (
                MainPageLocators.QUESTION_4,
                MainPageLocators.ANSWER_4,
                'Пока что нет! Но если что-то срочное — всегда можно позвонить '
                'в поддержку по красивому номеру 1010.'
            ),
            (
                MainPageLocators.QUESTION_5,
                MainPageLocators.ANSWER_5,
                'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
            ),
            (
                MainPageLocators.QUESTION_6,
                MainPageLocators.ANSWER_6,
                'Да, пока самокат не привезли. Штрафа не будет, объяснительной '
                'записки тоже не попросим. Все же свои.'
            ),
            (
                MainPageLocators.QUESTION_7,
                MainPageLocators.ANSWER_7,
                'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
            ),
        ]
    )
    def test_faq_answer_match_expected_text(
        self, driver, question_locator, answer_locator, expected_text
    ):
        page = MainPage(driver)
        page.accept_cookie()
        actual_text = page.open_question_and_get_answer(
            question_locator,
            answer_locator
        )
        assert actual_text == expected_text


@allure.feature('Логотипы в хедере')
class TestMainPageLogos:
    @allure.title('Переход на главную по логотипу Самоката')
    @allure.description(
        'Тест проверяет, что при клике по логотипу Самоката '
        'пользователь остается на главной странице сервиса.'
    )
    def test_click_scooter_logo_redirects_to_main_page(self, driver):
        page = MainPage(driver)
        page.accept_cookie()
        page.click_scooter_logo()
        assert 'qa-scooter.praktikum-services.ru' in driver.current_url

    @allure.title('Переход на Дзен по логотипу Яндекса')
    @allure.description(
        'Тест проверяет, что при клике по логотипу Яндекса открывается '
        'новая вкладка с ресурсом Яндекса или Дзен.'
    )
    def test_click_yandex_logo_opens_dzen_page(self, driver):
        page = MainPage(driver)
        page.accept_cookie()
        page.click_yandex_logo()
        page.switch_to_new_tab()
        page.wait_for_yandex_or_dzen_url()

        assert 'https://dzen.ru/?yredirect=true' in driver.current_url