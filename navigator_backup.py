#from selenium import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
browser = webdriver.Firefox()

browser.get("https://archive.physionet.org/cgi-bin/atm/ATM")

#Select drpDatabase = new Select(driver.findElement(By.name("database")))
select = Select(browser.find_element_by_name('database'))

select.select_by_visible_text('ECG-ID Database (ecgiddb)')

#time.sleep(5)


select_box = browser.find_element_by_name("rbase") 


options = [x for x in select_box.find_elements_by_tag_name("option")]

for element in options:
    print element.get_attribute("value") 
