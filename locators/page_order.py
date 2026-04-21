from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'* Адрес: куда привезти заказ')]"
    )
    METRO_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'* Станция метро')]"
    )
    PHONE_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]"
    )
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'* Когда привезти самокат')]"
    )
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-control')
    COMMENT_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Комментарий для курьера')]"
    )

    BLACK_COLOR_CHECKBOX = (By.ID, 'black')
    GREY_COLOR_CHECKBOX = (By.ID, 'grey')

    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"
    )
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    SUCCESS_MODAL_HEADER = (
        By.XPATH,
        "//div[contains(@class,'Order_ModalHeader')]"
    )
    PERIOD_1 = (
        By.XPATH, 
        "//div[text()='сутки']"
    )
    PERIOD_2 = (
        By.XPATH, "//div[text()='двое суток']"
    )