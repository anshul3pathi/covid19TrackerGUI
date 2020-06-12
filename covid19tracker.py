import selenium 
from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.covid19india.org/")
time.sleep(10)

attributes = []
values = []
root = driver.find_element_by_id("root")
level = root.find_element_by_class_name("Level")
h5 = level.find_elements_by_tag_name("h5")
h1 = level.find_elements_by_tag_name("h1")
for x, y in zip(h5, h1):
    attributes.append(x.text)
    values.append(y.text)

for val in enumerate(values):
    values[val[0]] = int(val[1].replace(',', ''))

print(attributes, values)
driver.quit()
