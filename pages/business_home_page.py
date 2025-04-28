from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BusinessHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    H1_HEADER = (By.TAG_NAME, "h1")
    CLOUD_DATA_CENTER_OPTION = (By.XPATH, '//*[@id="offer"]/div/div/div[4]/div/a[2]')

    # Actions
    def assert_superteam_header(self):
        """Assert that the page header is correct."""
        header = self.wait.until(EC.visibility_of_element_located(self.H1_HEADER))
        assert header.text == "Nasz SuperTeam dla cyfrowego rozwoju Twojej firmy", "Incorrect Business HomePage header."

    def select_cloud_data_center(self):
        """Click on 'Cloud & Data Center'."""
        cloud_button = self.wait.until(EC.element_to_be_clickable(self.CLOUD_DATA_CENTER_OPTION))
        cloud_button.click()
