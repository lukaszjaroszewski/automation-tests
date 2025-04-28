import pytest
from pages.business_home_page import BusinessHomePage
from pages.cloud_data_center_page import CloudDataCenterPage
from pages.home_page import HomePage
from pages.business_cloud_page import BusinessCloudPage
from pages.private_cloud_page import PrivateCloudPage
import time


@pytest.mark.business_journey
def test_business_journey(driver):
    home_page = HomePage(driver)
    business_home_page = BusinessHomePage(driver)
    cloud_data_center_page = CloudDataCenterPage(driver)
    business_cloud_page = BusinessCloudPage(driver)
    private_cloud_page = PrivateCloudPage(driver)

    # Accept cookies (if present)
    home_page.accept_cookies()

    # Step 1: Click on 'Średnie i duże firmy'
    home_page.select_business_section()

    # Step 2: Assert h1 on Business HomePage
    business_home_page.assert_superteam_header()

    # Step 3: Click on 'Cloud & Data Center'
    business_home_page.select_cloud_data_center()

    # Step 4: Assert h1 on Cloud & Data Center Page
    cloud_data_center_page.assert_cloud_data_center_header()

    # Step 5: Click 'Sprawdź szczegóły' on Business Cloud
    cloud_data_center_page.select_business_cloud()

    # Step 6: Assert URL on Business Cloud page
    business_cloud_page.assert_business_cloud_url()

    # Step 7: Click on 'Dowiedz się więcej' under Private Cloud
    business_cloud_page.select_private_cloud()

    # Step 8: Assert h1 on Private Cloud page
    private_cloud_page.assert_private_cloud_header()

    # Step 9: Assert URL on Private Cloud page
    private_cloud_page.assert_private_cloud_url()

    # Step 10: Click 'Zapytaj o ofertę'
    private_cloud_page.click_inquiry_button()

    time.sleep(10)