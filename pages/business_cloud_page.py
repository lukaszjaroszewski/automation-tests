from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BusinessCloudPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    BUSINESS_CLOUD_URL = "https://biznes.t-mobile.pl/pl/business_cloud"
    PRIVATE_CLOUD_MORE_INFO_BUTTON = (By.XPATH, '/html[1]/body[1]/div[2]/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/a[1]')

    # Actions
    def assert_business_cloud_url(self):
        """Assert that the current URL is the Business Cloud page URL."""
        expected_url = self.BUSINESS_CLOUD_URL
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    def select_private_cloud(self):
        """Click on 'Dowiedz się więcej' button under Private Cloud."""
        private_cloud_button = self.wait.until(EC.element_to_be_clickable(self.PRIVATE_CLOUD_MORE_INFO_BUTTON))
        private_cloud_button.click()
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
