from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('C:/Install/chromedriver.exe')

def first_task():
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.ebay.com")
    print("Current URL:", driver.current_url)
    driver.quit()


def second_task():
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.ebay.com")
    timer = 0
    while timer < 10:
        locator = driver.find_elements(By.XPATH, '//div[@id="gh-ac-box2"]')
        if len(locator) > 0:
            break
        else:
            sleep(1)
            timer += 1
    print("Current URL:", driver.current_url)
    driver.quit()

def third_task():
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.ebay.com")
    print("Current URL:", driver.current_url)
    search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="gh-ac-box2"]//input')))
    search_box.send_keys("women watch")
    search_box.submit()
    driver.quit()

def forth_task():
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.ebay.com")
    print("Current URL:", driver.current_url)
    search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="gh-ac-box2"]//input')))
    search_box.send_keys("women watch")
    search_box.submit()
    header = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//h1[@class="srp-controls__count-heading"]')))
    if "results for women watch" in header.text.lower():
        print("Search results verified: Header contains 'results for women watch'")
    else:
        print("Search results verification failed: Header does not contain 'results for women watch'")
    driver.quit()

first_task()
second_task()
third_task()
forth_task()