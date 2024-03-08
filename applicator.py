from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the web page
driver.get("https://example.com")

# Find the button element by its ID, class name, or XPath
button = driver.find_element_by_id("button-id")

# Click the button
button.click()

# Close the browser
driver.quit()