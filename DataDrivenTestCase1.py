from selenium.webdriver.common.by import By

import XLUtils

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.facebook.com/")
driver.maximize_window()

path = "C:\python-selenium\Data Driven\Excel Data\DataDriven1.xlsx"

rows = XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element(By.NAME, "email").send_keys(username)
    driver.find_element(By.NAME, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    if driver.title == "Facebook – log in or sign up or register":
        print("test is passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test passed")
    else:
        print("test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")

    driver.find_element(By.LINK_TEXT, "Log in").click()
