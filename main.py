from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# chat bot message with COMMANDS
# - GET ALL
# - LUNCH/DINNE/BREAKFAST
# - WHAT TO DO IF DATES ARE NOT AVAILABLE (send error message)

driver = Chrome(executable_path='/usr/local/bin/chromedriver')

with Chrome() as driver:
    wait = WebDriverWait(driver, 10) #FluentWait
    driver.get("https://www.dickinson.edu/info/20205/campus_dining/197/dining_hall")
    slider = driver.find_element(By.CSS_SELECTOR, ".Slider")
    days = slider.find_elements(By.CSS_SELECTOR, '.w3-display-middle')
    result = []
    for d in days:
        element = wait.until(EC.visibility_of(d))
        # print(element.text)
        result.append(element.text)
        slider.find_element(By.CSS_SELECTOR, ".btn.sliderIcon.leftNextIcon").click()    

    for i in result:
        print(i)
    

    # driver.get("https://www.google.com/")
    # driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    # first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    # print(first_result.get_attribute("textContent"))
