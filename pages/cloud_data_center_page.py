from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CloudDataCenterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    H1_HEADER = (By.TAG_NAME, "h1")
    BUSINESS_CLOUD_DETAILS_BUTTON = (By.XPATH, '/html[1]/body[1]/main[1]/div[1]/section[1]/ul[1]/li[2]/div[1]/div[2]/div[1]/a[1]')

    # Actions
    def assert_cloud_data_center_header(self):
        """Assert that the page header is 'Cloud & Data Center'."""
        header = self.wait.until(EC.visibility_of_element_located(self.H1_HEADER))
        assert header.text == "Cloud & Data Center", "Incorrect Cloud & Data Center page header."

    def select_business_cloud(self):
        """Click 'Sprawdź szczegóły' for Business Cloud."""
        business_cloud_button = self.wait.until(EC.element_to_be_clickable(self.BUSINESS_CLOUD_DETAILS_BUTTON))
        business_cloud_button.click()
