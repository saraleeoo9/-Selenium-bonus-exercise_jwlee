from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import locator
from csv import reader
from selenium.webdriver.support.ui import Select
import random

# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://automationpractice.com/")
driver.maximize_window()

with open('data.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:
        assert driver.find_element(*locator["contact_us_button"]).is_displayed()
        driver.find_element(*locator["contact_us_button"]).click()
        select = Select(driver.find_element_by_id('id_contact'))
        select.select_by_value('2')
        #select = Select(driver.find_element_by_id("selector_dropdown"))
        #select = Select(driver.find_element(*locator["days_dropdown"]))
        #select.select_by_index(1)
        driver.find_element(*locator["email_field"]).send_keys(row[0])
        driver.find_element(*locator["order_field"]).send_keys(row[1])
        driver.find_element(*locator["message_field"]).send_keys(row[2])
        driver.find_element(*locator["send_button"]).click()

        assert driver.find_element(*locator["success_message"]).text == "Your message has been successfully sent to our team."
               #row[3]

driver.quit()


























