from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = [By.XPATH, './/button[text()="Войти в аккаунт"]']
    FLUORESCENT_BUN = [By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]/parent::a']
    FLUORESCENT_BUN_COUNTER = [By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]/parent::a//p']
    OPEN_DETAILS_CLASS = [By.XPATH, './/section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]']
    DETAIL_CROSS_BUTTON = [By.XPATH, './/section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//button']
    CONSTRUCTOR_BASKET_LIST = [By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_']
    ORDER_BUTTON = [By.XPATH, './/button[text()="Оформить заказ"]']
    ORDER_NUMBER = [By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]']
