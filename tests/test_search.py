
from pages.home_page import HomePage


def test_search(home_page: HomePage):
    
    home_page.get('https://detailclub.ru/')
    assert home_page.web_driver.current_url == 'https://detailclub.ru/'
    
    home_page.header.search('очиститель')
    