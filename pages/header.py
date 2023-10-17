from pages.base.base_page import BasePage
from pages.base.button import Button
from pages.base.input import Input
from pages.base.link import Link


class Header(BasePage):
    def __init__(self, web_driver) -> None:
        super().__init__(web_driver)
        self.catalog = Button(web_driver, "Каталог", xpath='//nav//li[contains(., "аталог")]')
        self.search_field = Input(web_driver, "Поиск", xpath='//*[@name="q"]')
        self.search_icon = Button(web_driver, "Иконка_поиска", xpath='//*[@class="search_bar"]')
        
        
    def search(self, value: str):
        self.search_icon.click()
        assert self.search_field.should_be_visible()
        self.search_field.fill(value)
        self.search_field.send_enter()
        self.wait_page_loaded()