from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    COLOR_GREEN_OPTION = (By.XPATH,
                          '/html[1]/body[1]/div[2]/div[4]/main[1]/section[1]/section[1]/div[1]/section[1]/article[1]/div[1]/article[1]/div[1]/section[2]/article[1]/section[2]/section[1]/div[2]/div[1]/div[3]/span[1]')
    ONE_TIME_PAYMENT_OPTION = (By.XPATH,
                               '/html[1]/body[1]/div[2]/div[4]/main[1]/section[1]/section[1]/div[1]/section[1]/article[1]/div[1]/article[1]/div[1]/section[2]/article[1]/section[2]/section[4]/section[1]/div[1]/div[2]')
    ADD_TO_CART_BUTTON = (By.XPATH,
                          "//div[@class='styles__StyledCard-sc-10vwz6i-0 knDjNo styles__StyledTotalPriceSticky-sc-1uypdpm-7 iRDodx stickyAreaWrapper totalPriceSticky hideDefault show vertical_view']//div[@class='sc-feUZmu kaPNdW dt_typography variant_bodyBold'][normalize-space()='Dodaj do koszyka']")

    # Actions
    def select_green_color(self):
        """Select green color if available."""
        color_button = self.wait.until(EC.element_to_be_clickable(self.COLOR_GREEN_OPTION))
        color_button.click()

    def select_one_time_payment(self):
        """Selects the one-time payment option."""
        wait = WebDriverWait(self.driver, 10)
        payment_button = wait.until(EC.element_to_be_clickable(self.ONE_TIME_PAYMENT_OPTION))
        payment_button.click()

    def add_to_cart(self):
        """Add device to cart."""
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        add_button.click()