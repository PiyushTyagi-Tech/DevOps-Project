from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_page():
    # Set the path to your webdriver executable (e.g., chromedriver.exe)
    
    driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')

    # Navigate to the Login page
    driver.get('https:localhost:5000')

    # Wait for page elements to load
    wait = WebDriverWait(driver, 10)

    # Verify labels, text boxes, buttons, and links
    verify_elements_presence(driver, wait)

    # Verify font type and size
    verify_font_type_and_size(driver, wait)

    # Verify size, color, and UI
    verify_element_styles(driver, wait)

    # Verify responsive UI
    verify_responsive_ui(driver, wait)

    # Close the browser
    driver.quit()

# Run the test
if __name__ == "__main__":
    test_login_page()
