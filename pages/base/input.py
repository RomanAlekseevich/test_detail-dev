import time

from pages.base.component import Component


class Input(Component):
    
    @property
    def type_of(self) -> str:
        return 'input'
    
    
    def fill(self, value: str, **kwargs):
        element = self.get_presence_element(**kwargs)
        element.click()
        element.clear()
        element.send_keys(value)
        time.sleep(1)
        
    