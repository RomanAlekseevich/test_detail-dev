import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, web_driver) -> None:
        self.web_driver = web_driver
    
    def get(self, url):
        self.web_driver.get(url)
        self.wait_page_loaded()
        
    def go_back(self):
        self.web_driver.back()
        self.wait_page_loaded()
    
    def refresh(self):
        return self.web_driver.refresh()
    
    def check_js_errors(self, ignore_list=None):
        """ This function checks JS errors on the page. """

        ignore_list = ignore_list or []

        logs = self.web_driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'WARNING':
                ignore = False
                for issue in ignore_list:
                    if issue in log_message['message']:
                        ignore = True
                        break

                assert ignore, 'JS error "{0}" on the page!'.format(log_message)
    
    def wait_page_loaded(self, timeout=60, check_js_complete=True, 
                         check_page_changes=False, wait_for_element=None,
                         wait_for_xpath_to_disappear='', sleep_time=2):
        page_loaded = False
        double_check = False
        k = 0
        
        if sleep_time:
            time.sleep(sleep_time)
            
        # Get source code of the page to track changes in HTML:
        source = ''
        try:
            source = self.web_driver.page_source
        except:
            pass
        
        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            time.sleep(0.5)
            k += 1
            
            if check_js_complete:
                # Scroll down and wait when page will be loaded:
                try:
                    self.web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self.web_driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass
            
            if page_loaded and check_page_changes:
                # Check if the page source was changed
                new_source = ''
                try:
                    new_source = self.web_driver.page_source
                except:
                    pass
                
                page_loaded = new_source == source
                source = new_source
            
            # Wait when some element will disappear:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self.web_driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass  # Ignore timeout errors

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self.web_driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass  # Ignore timeout errors
            
            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True
                
        # Go up:
        self.web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')