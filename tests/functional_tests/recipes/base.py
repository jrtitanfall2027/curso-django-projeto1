import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.browser import make_chrome_browser

from recipes.tests.test_recipe_base import RecipeMixin


class RecipeBaseFunctionalTest(StaticLiveServerTestCase, RecipeMixin):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_text_in_element(self, by, value, text, timeout=10):
        def _predicate(driver):
            try:
                return text in driver.find_element(by, value).text
            except (NoSuchElementException, StaleElementReferenceException):
                return False

        return WebDriverWait(self.browser, timeout).until(_predicate)

    def submit_form(self, form):
        submit_button = form.find_element(By.XPATH, './/button[@type="submit"]')
        submit_button.click()
