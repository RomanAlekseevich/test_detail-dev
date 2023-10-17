# кнопка
from pages.base.component import Component


class Button(Component):
    
    @property
    def type_of(self) -> str:
        return 'button'
    
    def hover(self):
        pass