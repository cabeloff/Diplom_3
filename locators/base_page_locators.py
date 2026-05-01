from selenium.webdriver.common.by import By

class BasePageLocators:
    CONSTRUCTOR_BUTTON = [By.XPATH, './/p[text()="Конструктор"]']
    ORDER_FEED_BUTTON = [By.XPATH, './/p[text()="Лента Заказов"]']
    LOADING_MODAL = [By.XPATH, ".//img[contains(@class, 'modal__loading')]/.."]
