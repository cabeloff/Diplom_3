from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT_FIELD = [By.XPATH, './/form[starts-with(@class,"Auth_form")]//label[text()="Email"]/parent::*/input']
    PASSWORD_INPUT_FIELD = [By.XPATH, './/form[starts-with(@class,"Auth_form")]//label[text()="Пароль"]/parent::*/input']
    LOGIN_BUTTON = [By.XPATH, './/button[text()="Войти"]']

