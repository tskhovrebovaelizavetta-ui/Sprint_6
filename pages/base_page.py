import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Клик по элементу: {locator}')
    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Ввод текста "{text}" в элемент: {locator}')
    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step('Получение текста элемента: {locator}')
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step('Ожидание видимости элемента: {locator}')
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента: {locator}')
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Скролл к элементу: {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Принять cookie, если кнопка отображается')
    def accept_cookie(self):
        try:
            self.click_element(BasePageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
       
    @allure.step('Получить текущий URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться, что URL содержит: {url_part}')
    def wait_for_url_contains(self, url_part):
        self.wait.until(lambda d: url_part in d.current_url)

    @allure.step('Дождаться открытия страницы Яндекса или Дзена')
    def wait_for_yandex_or_dzen_url(self):
        self.wait.until(
            lambda d: 'dzen.ru' in d.current_url or 'yandex.ru' in d.current_url
        )