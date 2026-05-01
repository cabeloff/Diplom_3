import allure
from urls import ORDER_FEED
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    
    @allure.step('Открытие страницы Лента Заказов')
    def open_order_feed_page(self):
        self.open_page(ORDER_FEED)
        self.wait_for_loading()
        self.wait_for_element_visible(OrderFeedPageLocators.TODAY_COUNTER)
    
    @allure.step('Проверить счетчик "Выполнено за сегодня"')
    def check_orders_today_counter(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_COUNTER))
        
    @allure.step('Проверить счетчик "Выполнено за все время"')
    def check_orders_all_time_counter(self):
        return int(self.get_text(OrderFeedPageLocators.ALL_TIME_COUNTER))
    
    @allure.step('Получение списка "В работе"')
    def get_in_progress_list(self):
        return self.get_text(OrderFeedPageLocators.ORDER_IN_PROGRESS)
    
    @allure.step('Получение номера заказа из списка "В работе" с ожиданием появления')
    def get_number_in_progress(self, order_number):
        number_in_progress = '0' + order_number
        self.wait_change_text(OrderFeedPageLocators.ORDER_IN_PROGRESS, number_in_progress)
        return number_in_progress
