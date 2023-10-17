import pytest

from pages.home_page import HomePage


@pytest.fixture
def home_page(get_driver):
    yield HomePage(get_driver)
    

@pytest.fixture(params = ['https://detailclub.ru/', 'https://detailclub.ru/catalog/'])
def url(request):
    yield request.param