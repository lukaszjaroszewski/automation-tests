import pytest
from pages.home_page import HomePage
from pages.phones_without_contract_page import PhonesWithoutContractPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.mark.customer_journey
def test_customer_buy_phone(driver):
    """Test for a customer buying a phone on T-Mobile website."""

    # Create HomePage object
    home_page = HomePage(driver)

    # Accept cookies (if present)
    home_page.accept_cookies()

    # Open 'Urządzenia' menu to find phones
    home_page.open_devices_menu()

    # Select 'Smartfony' category from the menu
    home_page.select_phones_category()

    # Create PhonesWithoutContractPage object
    phones_page = PhonesWithoutContractPage(driver)

    # Assert that we're on the correct phones section page
    phones_page.assert_phones_section_page()

    # Choose the first phone on the "Urządzenia bez abonamentu" page
    phones_page.select_first_phone()

    # On the product page - take necessary actions
    product_page = ProductPage(driver)

    # Select green color
    product_page.select_green_color()

    # Select one-time payment
    product_page.select_one_time_payment()

    # Add device to cart
    product_page.add_to_cart()

    # Navigate to CartPage
    cart_page = CartPage(driver)

    # Assert the page title
    cart_page.assert_cart_page_title()

    # Reveal payment details
    cart_page.reveal_payment_details()

    # Click 'Dalej' button to proceed
    cart_page.proceed_to_next_step()

    # Assert that the customer details section is displayed correctly
    cart_page.assert_customer_details_section()