import selenium 
from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.covid19india.org/")
time.sleep(10)

attributes = []
root = driver.find_element_by_id("root")
level = root.find_element_by_class_name("Level")
h5 = level.find_elements_by_tag_name("h5")
for h in h5:
    attributes.append(h.text)
print(attributes)
driver.quit()
