import undetected_chromedriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

def cloudflare_bypass(url):
    DRIVER = undetected_chromedriver.Chrome()

    DRIVER.get(url)
    time.sleep(10)

    div_element = DRIVER.find_element(By.XPATH, "//div[@id='HXrjT5']")

    location = div_element.location
    size = div_element.size

    x = location['x']
    y = location['y']
    width = size['width']
    height = size['height']

    click_x = x + width * 0.1
    click_y = y + height * 0.5

    actions = ActionChains(DRIVER)
    actions.move_by_offset(-DRIVER.execute_script('return window.pageXOffset'), 
                           -DRIVER.execute_script('return window.pageYOffset')).perform()
    actions.move_by_offset(click_x, click_y).click().perform()
    actions.move_by_offset(-click_x, -click_y).perform()
