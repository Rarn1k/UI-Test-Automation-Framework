from element_objects.base_element import BaseElement


class Label(BaseElement):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        super().__init__(locator, name)