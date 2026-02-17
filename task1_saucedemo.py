from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.service import Service
import time

# Setup Edge
service = Service("msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Sort Options list
sort_options = ["lohi", "hilo", "az"]

for option in sort_options:

    print(f"\nTesting sort option: {option}")

    # Select sorting
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value(option)

    time.sleep(2)

    # Get all products
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    first_product = products[0]

    product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
    product_price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text

    print("Selected Product:", product_name)
    print("Price:", product_price)

    # Add to cart
    first_product.find_element(By.TAG_NAME, "button").click()

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    cart_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    cart_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    cart_quantity = driver.find_element(By.CLASS_NAME, "cart_quantity").text

    # Verification
    assert cart_name == product_name
    assert cart_price == product_price
    assert cart_quantity == "1"

    assert cart_price == product_price


    # Remove item & go back
    driver.find_element(By.CLASS_NAME, "cart_button").click()
    driver.find_element(By.ID, "continue-shopping").click()

time.sleep(5)
driver.quit()
