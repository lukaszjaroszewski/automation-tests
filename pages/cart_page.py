from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    CART_PAGE_TITLE = (By.XPATH, "//h1[text()='Twój koszyk']")
    REVEAL_PAYMENT_DETAILS_BUTTON = (By.XPATH,
                                     "/html[1]/body[1]/div[2]/div[4]/div[4]/section[1]/section[1]/div[7]/article[1]/div[2]/div[2]/div[1]/div[1]/span[1]")
    NEXT_BUTTON = (By.XPATH,
                   "/html[1]/body[1]/div[2]/div[4]/div[4]/div[2]/div[1]/div[3]/button[1]/span[1]")
    CUSTOMER_DETAILS_TEXT = (By.XPATH,
                             "/html[1]/body[1]/div[2]/div[4]/div[2]/section[1]/div[1]/main[1]/div[3]/div[1]/div[2]")

    # Actions
    def assert_cart_page_title(self):
        """Assert that the cart page title is correct."""
        title = self.wait.until(EC.presence_of_element_located(self.CART_PAGE_TITLE)).text
        assert title == "Twój koszyk", f"Expected 'Twój koszyk' but got '{title}'"

    def reveal_payment_details(self):
        """Click to reveal payment details."""
        payment_button = self.wait.until(EC.element_to_be_clickable(self.REVEAL_PAYMENT_DETAILS_BUTTON))
        payment_button.click()

    def proceed_to_next_step(self):
        """Click 'Dalej' button to proceed to the next step."""
        next_button = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        next_button.click()

    def assert_customer_details_section(self):
        """Assert that the text inside the customer details section is correct."""
        customer_details = self.wait.until(EC.presence_of_element_located(self.CUSTOMER_DETAILS_TEXT)).text
        assert customer_details == "Dane zamawiającego", f"Expected 'Dane zamawiającego' but got '{customer_details}'"
