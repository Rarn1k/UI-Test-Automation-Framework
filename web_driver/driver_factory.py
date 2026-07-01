from typing import ClassVar, Type

from utils.config.config_manager import ConfigManager
from web_driver.base_driver import BaseDriver
from web_driver.chrome_driver import ChromeDriver
from web_driver.firefox_driver import FirefoxDriver


class DriverFactory:
    _drivers: ClassVar[dict[str, Type[BaseDriver]]] = {
        "chrome": ChromeDriver,
        "firefox": FirefoxDriver,
    }

    @classmethod
    def create_driver(cls) -> BaseDriver:
        driver_name = ConfigManager().instance().browser().lower()
        if driver_name not in cls._drivers:
            raise ValueError(f"Неизвестный браузер: {driver_name}")
        return cls._drivers[driver_name]()
