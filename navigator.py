from selenium import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import sys


browser = webdriver.Firefox()

browser.get("https://archive.physionet.org/cgi-bin/atm/ATM")

#Select drpDatabase = new Select(driver.findElement(By.name("database")))
select = browser.find_element_by_name('database')


options = [x.get_attribute('value') for x in select.find_elements_by_tag_name("option")]


print("ESCOLHA UMA OPÇÃO")
for index, option in enumerate(options):
    print(f"{index}: {option}")

user_option = int(input("Opção: "))


select = Select(select)
select.select_by_value(options[user_option])


select_box = browser.find_element_by_name("rbase") 


options = [x for x in select_box.find_elements_by_tag_name("option")]

f = open("databases.txt", "w")

for element in options:
    print(element.get_attribute("value")) 
    f.write(element.get_attribute("value") + "\n")

f.close()
