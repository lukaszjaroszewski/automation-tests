from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PhonesWithoutContractPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    FIRST_PHONE = (By.XPATH, "/html[1]/body[1]/div[2]/div[4]/main[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/a[1]")
    PHONES_SECTION_URL = "https://www.t-mobile.pl/sklep/kategoria/telefony/lista/produkty?hardwareOnlySale=true"

    # Actions
    def assert_phones_section_page(self):
        """Assert that we have landed on the expected phones section page."""
        current_url = self.driver.current_url
        assert self.PHONES_SECTION_URL in current_url, f"Expected to be on the phones section page, but got {current_url}"

    def select_first_phone(self):
        """Select the first phone from the list of phones without subscription."""
        phone = self.wait.until(EC.element_to_be_clickable(self.FIRST_PHONE))
        phone.click()

        # Assert that the h1 contains the phone name "Xiaomi Redmi Note 14 5G"
        h1_text = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text
        assert h1_text == 'Xiaomi Redmi Note 14 5G', f"Expected 'Xiaomi Redmi Note 14 5G' but got '{h1_text}'"