from base.BasePage import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    PAGE_URL = Links.HOMEPAGE

    SITE_HEADER = ("xpath", "//div[@class='site_header']")
    TEXT_INPUT_LINK = ("xpath", "//*[contains(text(), 'Text input')]")

    def click_text_input_link(self):
        self.wait.until(EC.element_to_be_clickable(self.TEXT_INPUT_LINK)).click()
