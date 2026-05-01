import allure
from urls import BASE_PAGE
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.login_page_locators import LoginPageLocators

class MainPage(BasePage):   
    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.open_page(BASE_PAGE)
        self.wait_for_loading()
        self.wait_for_element_visible(MainPageLocators.LOGIN_BUTTON)
    
    @allure.step('Клик по кнопке Конструктор')
    def click_constructor_button_in_header(self):
        self.click(BasePageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_loading()
        self.wait_for_element_visible(MainPageLocators.LOGIN_BUTTON)
    
    @allure.step('Клик по кнопке Лента Заказов')
    def click_order_feed_button_in_header(self):
        self.click(BasePageLocators.ORDER_FEED_BUTTON)
        self.wait_for_loading()
        self.wait_for_element_visible(OrderFeedPageLocators.TODAY_COUNTER)
        
    @allure.step('Клик по ингредиенту Флюоресцентная булка R2-D3')
    def click_ingredient(self):
        self.click(MainPageLocators.FLUORESCENT_BUN)
        self.wait_for_loading()
        self.wait_for_element_visible(MainPageLocators.OPEN_DETAILS_CLASS)
        
    @allure.step('Клик по крестику в окне деталей ингредиента')
    def click_cross_button_details(self):
        self.wait_for_loading()
        self.click(MainPageLocators.DETAIL_CROSS_BUTTON)

    @allure.step('Проверка счетчика игнгредиента Флюоресцентная булка R2-D3')
    def check_fluorescent_bun_counter(self):
        self.wait_for_loading()
        return int(self.get_text(MainPageLocators.FLUORESCENT_BUN_COUNTER))
        
    @allure.step('Перенос ингредиента Флюоресцентная булка R2-D3 в конструктор')
    def transfer_fluorescent_bun_to_constructor(self):
        self.tranfer_element(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.CONSTRUCTOR_BASKET_LIST)
        
    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_account_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)
        self.wait_for_loading()
        self.wait_for_element_visible(LoginPageLocators.LOGIN_BUTTON)
                
    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_create_an_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)
        self.wait_for_loading()
        

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        self.wait_for_loading()        
        return self.get_text(MainPageLocators.ORDER_NUMBER)
