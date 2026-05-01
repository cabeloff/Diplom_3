from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
import allure

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Поиск элементов')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)     

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание исчезновения элемента')
    def wait_for_element_invisible(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_clackable(self, locator):
        return WebDriverWait(self.driver, 25).until(expected_conditions.element_to_be_clickable(locator))
    
    @allure.step('Клик по элементу')
    def click(self, locator):
        self.wait_for_element_visible(locator)
        self.wait_for_element_clackable(locator).click()
 
    @allure.step('Ввод данных в поле')
    def send_keys(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)
    
    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    
    @allure.step('Получение URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Перемещение элемента')
    def tranfer_element(self, source, target):
        drag_and_drop(self.driver, self.driver.find_element(*source), self.driver.find_element(*target))
        
    @allure.step('Ожидание загрузки')
    def wait_for_loading(self):
        if self.driver.find_element(*BasePageLocators.LOADING_MODAL).is_displayed():
            self.wait_for_element_invisible(BasePageLocators.LOADING_MODAL)
        
    @allure.step("Ожидание изменения текста элемента")
    def wait_change_text(self, locator, expected_text):
        return WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, expected_text))
