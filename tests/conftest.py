import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Fixture to set up and tear down the browser instance
@pytest.fixture()
def driver():
    # Setup: Initialize Chrome WebDriver with WebDriver Manager for automatic version management
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Maximize the browser window
    driver.maximize_window()  # Optionally, to make sure the window is maximized
    # Open the homepage
    driver.get("https://www.t-mobile.pl")

    # Yield the driver to the test
    yield driver

    # Close the browser after the test is done
    driver.quit()
