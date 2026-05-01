from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    
    ALL_TIME_COUNTER = [By.XPATH, './/p[text()="Выполнено за все время:"]/parent::div/p[2]']
    TODAY_COUNTER = [By.XPATH, './/p[text()="Выполнено за сегодня:"]/parent::div/p[2]']
    ORDER_IN_PROGRESS = [By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li']
