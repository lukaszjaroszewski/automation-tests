# Automated Test Suite for T-Mobile Website

This project contains an automated test suite for the T-Mobile website using **Selenium**, **pytest**, and **Python**. It covers two main customer journeys:
1. **Customer Journey** - Testing the process of purchasing a phone and navigating through the phones section.
2. **Business Journey** - Testing the process of navigating business products, specifically Cloud & Data Center offerings.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)


## Project Overview
This project automates and tests customer and business journeys on the T-Mobile website. The tests simulate real customer behavior and ensure that the website behaves correctly throughout the purchasing and browsing process.

Tests include:
- Navigating the phone category and purchasing a product.
- Navigating the business products section and exploring Cloud & Data Center services.

## Technologies Used
- **Python 3.x**
- **Selenium** for browser automation
- **pytest** for test automation
- **PyCharm** as the IDE
- **Git** for version control
- **pytest markers** to run tests based on specific customer journeys

## Installation

### Prerequisites
Before running the tests, make sure you have the following installed:

- **Python 3.x**
- **pip** (Python's package installer)
- **Git** (for version control)

### Steps to Install

1. **Clone the Repository**
   ```bash
   git clone https://github.com/lukaszjaroszewski/automation-tests.git

2. **Navigate to the Project Directory**
    ```bash
    cd your-repo-name
   
3. **Install Dependencies** Install the necessary Python packages listed in requirements.txt:
    ```bash
    pip install -r requirements.txt

4. **Download WebDriver** The tests require a browser WebDriver (e.g., ChromeDriver). Make sure to download the appropriate driver for your browser version.

### Usage
**Running the Tests**
To run the tests, simply use the following command in your terminal:
    ```bash
    pytest

**PyCharm Configuration**
If you're using PyCharm, you can set up a pytest configuration to run the tests:

1. Go to Run > Edit Configurations.
2. Create a new Python test configuration.
3. Specify the path to the test files or directories you wish to run.

### Testing
This project contains automated tests for two key customer journeys:

1. Customer Journey Tests
- Navigate to the phones section.
- Select a phone and add it to the cart.
- Proceed through the checkout process.

2. Business Journey Tests
- Navigate to the "Business" section of the website.
- Explore the Cloud & Data Center product offerings.
- Dive deeper into the Business Cloud and Private Cloud options.

Each test is designed to assert that the expected behavior occurs at each step, ensuring the site functions as intended.

**Example of Test Flow for Customer Journey:**
- Go to the phones section.
- Select a phone.
- Add the phone to the cart.
- Assert various headers and page states.

**Example of Test Flow for Business Journey:**
- Navigate to the Business section.
- Explore Cloud & Data Center options.
- Select Business Cloud and Private Cloud options.
- Click on the "Zapytaj o ofertę" button.