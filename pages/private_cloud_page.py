from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PrivateCloudPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    H1_HEADER = (By.TAG_NAME, "h1")
    INQUIRY_BUTTON = (By.XPATH, '/html[1]/body[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[2]/a[1]')

    # Actions
    def assert_private_cloud_header(self):
        """Assert that the page header is 'Private Cloud'."""
        header = self.wait.until(EC.visibility_of_element_located(self.H1_HEADER))
        assert header.text == "Private Cloud", f"Expected: Private Cloud, but got: {header.text}"

    def assert_private_cloud_url(self):
        """Assert that the current URL is correct."""
        expected_url = "https://biznes.t-mobile.pl/pl/produkty-i-uslugi/centra-danych/iaas-private-cloud"
        assert expected_url in self.driver.current_url, "Incorrect Private Cloud page URL."

    def click_inquiry_button(self):
        """Click on 'Zapytaj o ofertę' button."""
        inquiry_button = self.wait.until(EC.element_to_be_clickable(self.INQUIRY_BUTTON))
        inquiry_button.click()
