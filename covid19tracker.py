import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

def allIndiafigures():
    """function returning all India figures of confirmed, active, recovered and deceased cases"""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
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
    driver.quit()
    return attributes, values

def stateFigures():
    """fucntion returns name of states and related values of confirmed, active, recovered and deceased cases"""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get("https://www.covid19india.org/")
    time.sleep(10)
    state_names = []
    state_figures = []
    root = driver.find_element_by_id("root")
    table = root.find_element_by_class_name("table")
 
    rows = table.find_elements_by_class_name("row")
    for row in rows:
        cell = row.find_element_by_class_name("cell")
        state_names.append(cell.text)

    state_names = state_names[1:-1]
    for row in rows:
        state_vals = row.find_elements_by_class_name("total")
        for val in state_vals:
            state_figures.append(val.text)
    state_figures = state_figures[:-4]

    for val in enumerate(state_figures):
        state_figures[val[0]] = int(val[1].replace(',', ''))

    state_dict = {}
    for i in range(0, len(state_figures), 4):
        state_dict[state_names[i//4]] = state_figures[i:i+4]
    # print(state_dict)
    return state_dict

if __name__ == "__main__":
 
    stateFigures()

