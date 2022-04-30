# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
PATH = '/Users/jonathantan/Documents/Python Project/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://www.app.greaterchange.co.uk/donation/create")
time.sleep(1)
#login screen
input_email = driver.find_element_by_id("email")
input_password = driver.find_element_by_id("password")

input_email.send_keys("USERNAME")
input_password.send_keys("PASSWORD")

login_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/form/div[3]/div[2]/div/button")
login_button.click()

time.sleep(1)

#donation form input
for x in range(11):
    input_cause_id = Select(driver.find_element_by_id("cause_id"))
    input_donation = driver.find_element_by_id("amount")
    input_reference = driver.find_element_by_id("payment_reference")

    input_cause_id.select_by_value("176")
    input_donation.send_keys("10")
    input_reference.send_keys("Correction")

    save_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/form/div/div/div/div/div[4]/div/button")
    save_button.click()

    time.sleep(1)

    add_another_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/form/div/div/div[2]/div/div[4]/div/a[2]")
    add_another_button.click()
    x+=1

else:
    print("Function was looped for "+str(x)+" times")
