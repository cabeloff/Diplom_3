import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from data import account_username, account_password

class LoginPage(BasePage):
    
    @allure.step('Заполнить поле Email')
    def fill_email_field(self):
        self.send_keys(LoginPageLocators.EMAIL_INPUT_FIELD, account_username)
        
    @allure.step('Заполнить поле Пароль')
    def fill_password_field(self):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT_FIELD, account_password)    
    
    @allure.step('Клик по кнопке войти')
    def clik_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_loading()
        self.wait_for_element_visible(MainPageLocators.ORDER_BUTTON)
