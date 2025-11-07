import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Text input Page")
class TestTextInputPage(BaseTest):

    @allure.title('Open Text Input Page')
    @pytest.mark.smoke
    def test_valid_login(self):
        self.home_page.open()
        self.home_page.click_text_input_link()
        self.text_input_page.is_opened()
