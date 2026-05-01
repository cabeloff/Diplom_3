from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import allure

class TestMainPage:

    @allure.title('Проверка увеличения счётчика "Выполнено за всё время" при создании нового заказа') 
    @allure.description('Проверка текущего значения счетчика "Выполнено за всё время", создание заказа, авторизация, оформление заказа, проверка увеличения счетчика')
    def test_create_order_increases_orders_all_time_counter_success(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        init_counter = order_feed_page.check_orders_all_time_counter()
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.transfer_fluorescent_bun_to_constructor()
        main_page.click_account_login_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field()
        login_page.fill_password_field()
        login_page.clik_login_button()
        main_page.click_create_an_order_button()
        order_feed_page.open_order_feed_page()

        assert order_feed_page.check_orders_all_time_counter() == init_counter + 1, 'Счетчик "Выполнено за все время" не увеличился'
        
    @allure.title('Проверка увеличения счётчика "Выполнено за сегодня" при создании нового заказа') 
    @allure.description('Проверка текущего значения счетчика "Выполнено за сегодня", создание заказа, авторизация, оформление заказа, проверка увеличения счетчика')
    def test_create_order_increases_orders_today_counter_succes(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        init_counter = order_feed_page.check_orders_today_counter()
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.transfer_fluorescent_bun_to_constructor()
        main_page.click_account_login_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field()
        login_page.fill_password_field()
        login_page.clik_login_button()
        main_page.click_create_an_order_button()
        order_feed_page.open_order_feed_page()

        assert order_feed_page.check_orders_today_counter() == init_counter + 1, 'Счетчик "Выполнено за сегодня" не увеличился'
    
    @allure.title('Проверка появления номера заказа в списке "В работе" после оформления') 
    @allure.description('Создание заказа, авторизация, оформление заказа, проверка номера заказа в списке "В работе"')
    def test_order_number_appears_in_in_progress_list_succes(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.transfer_fluorescent_bun_to_constructor()
        main_page.click_account_login_button()
        login_page = LoginPage(driver)
        login_page.fill_email_field()
        login_page.fill_password_field()
        login_page.clik_login_button()
        main_page.click_create_an_order_button()
        order_number = main_page.get_order_number()
        order_feed_page.open_order_feed_page()

        assert order_number in order_feed_page.get_number_in_progress(order_number), 'Номер заказа в списке "В работе" не появился'
