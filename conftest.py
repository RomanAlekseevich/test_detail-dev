import pytest

from selenium import webdriver

@pytest.fixture
def get_driver(request):
    driver = webdriver.Chrome()
    # request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()
    
