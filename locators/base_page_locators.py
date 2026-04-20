from selenium.webdriver.common.by import By

BASE_URL = 'https://qa-scooter.praktikum-services.ru/'


class BasePageLocators:
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    SCOOTER_LOGO = (By.CSS_SELECTOR, 'a.Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'a.Header_LogoYandex__3TSOI')