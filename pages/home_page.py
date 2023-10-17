# хедер кнопки поле поиска

from pages.base.base_page import BasePage
from pages.header import Header



class HomePage(BasePage):

    def __init__(self, web_driver) -> None:
        super().__init__(web_driver)
        self.header = Header(web_driver)
      
  