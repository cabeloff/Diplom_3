from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import allure

class TestMainPage:

    @allure.title('Проверка появления окна с деталями при клике по ингредиенту') 
    @allure.description('Клик по ингредиенту "Флюоресцентная булка" в конструкторе и проверка класса элемента, соответствующий открытому окну "Детали ингредиента"')
    def test_click_ingredient_opens_ingredient_details_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()
        
        assert main_page.find_elements(MainPageLocators.OPEN_DETAILS_CLASS), 'Не найден элемент с классом, соответствующим открытму окну "Детали ингредиента"'
    
    @allure.title('Проверка закрытия окна с деталями при клике крестику') 
    @allure.description('Клик по крестику в окне деталей игредиента и проверка отсутствия класса элемента, соответствующий открытому окну "Детали ингредиента"')
    def test_click_cross_closes_ingredient_details_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()
        main_page.click_cross_button_details()
        
        assert not main_page.find_elements(MainPageLocators.OPEN_DETAILS_CLASS), 'Найден элемент с классом, соответствующим открытму окну "Детали ингредиента", которого не должно быть'
    
    @allure.title('Проверка увеличения счетчика при добавлении ингредиента в заказ') 
    @allure.description('Перенос ингредиента в конструктор бургера и проверка счетчика возле ингредиента')
    def test_add_ingredient_in_constructor_increases_counter_success(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        init_counter = main_page.check_fluorescent_bun_counter()
        main_page.transfer_fluorescent_bun_to_constructor()

        assert main_page.check_fluorescent_bun_counter() > init_counter, 'Счетчик ингредиента не увеличился'
        