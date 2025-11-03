import time
import pytest
from selenium.webdriver.common.by import By

class TestLoginPage:

    def test_valid_login(self,driver):
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        username_field = driver.find_element(By.ID, "user-name")
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        actual_url = driver.current_url
        assert actual_url == "https://www.saucedemo.com/inventory.html"

        time.sleep(2)