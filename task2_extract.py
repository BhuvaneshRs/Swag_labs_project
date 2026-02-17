from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.service import Service
import time

service = Service("msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_value("za")

time.sleep(2)

products = driver.find_elements(By.CLASS_NAME, "inventory_item")

print("\nFirst 3 Products After Sorting (Z to A):\n")

for index, product in enumerate(products[:3], start=1):

    title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = product.find_element(By.CLASS_NAME, "inventory_item_price").text

    print(f"Product {index}")
    print("Title:", title)
    print("Price:", price)
    print("----------------------")

input("Press Enter to close...")
driver.quit()
