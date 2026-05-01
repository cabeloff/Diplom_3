from pages.main_page import MainPage
from urls import BASE_PAGE, ORDER_FEED
import allure

class TestHeaderButtonsNavigation:

    @allure.title('Проверка перехода на главную страницу при клике по кнопке "Конструктор"') 
    @allure.description('Клик по кнопке "Конструктор" в шапке сайта и проверка текущего url')
    def test_click_constructor_button_opens_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed_button_in_header()
        main_page.click_constructor_button_in_header()
        
        assert main_page.get_current_url() == BASE_PAGE, 'Текущая страница не является главной'
    
    @allure.title('Проверка перехода на ленту заказов при клике по кнопке "Лента Заказов"') 
    @allure.description('Клик по кнопке "Лента Заказов" в шапке сайта и проверка текущего url')
    def test_click_order_feed_button_opens_order_feed_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed_button_in_header()
        
        assert main_page.get_current_url() == ORDER_FEED, 'Текущая страница не является лентой заказов'
