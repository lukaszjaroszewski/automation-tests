from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[3]/span[1]")
    DEVICES_CATEGORY = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/button[1]")
    PHONES_SUBCATEGORY = (By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/ul[1]/li[3]/ul[1]/li[1]/a[1]/div[1]/span[1]')
    BUSINESS_OPTION = (By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/header[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]/span[1]')

    # Actions
    def accept_cookies(self):
        """Accept cookies banner if displayed."""
        try:
            accept_button = self.wait.until(EC.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON))
            accept_button.click()
        except Exception as e:
            print(f"Accept cookies button not found or not clickable: {e}")

    def open_devices_menu(self):
        """Click on 'Urządzenia' on the menu."""
        devices_menu = self.wait.until(EC.element_to_be_clickable(self.DEVICES_CATEGORY))
        devices_menu.click()

    def select_phones_category(self):
        """Click on the 'Smartfony' category from the 'Urządzenia' submenu."""
        phones_category = self.wait.until(EC.element_to_be_clickable(self.PHONES_SUBCATEGORY))
        phones_category.click()

        # Assert that the h1 contains the text "Urządzenia"
        h1_text = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text
        assert h1_text == 'Urządzenia', f"Expected 'Urządzenia' but got '{h1_text}'"

    def select_business_section(self):
        """Select 'Średnie i duże firmy' option."""
        business_button = self.wait.until(EC.element_to_be_clickable(self.BUSINESS_OPTION))
        business_button.click()