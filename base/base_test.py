import pytest

from pages.home_page import HomePage
from pages.text_input_page import TextInputPage


class BaseTest:

    home_page: HomePage
    text_input_page: TextInputPage

    @pytest.fixture(autouse=True)
    def setup(self,request, driver):
        request.cls.driver = driver
        request.cls.home_page = HomePage(driver)
        request.cls.text_input_page = TextInputPage(driver)