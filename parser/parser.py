from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
import csv


url = 'https://forum.vgd.ru/1693/115157/0.htm'

def start_webdriver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)

    return driver

def start_csv_writer(file):
    writer = csv.writer(file)
    field = ['username', 'descr', 'date_time', 'message']
    writer.writerow(field)

    return writer

def manage_pagination(driver):
    message_table = driver.find_element(By.ID, 'maintableID')
    pagination_string = message_table.find_elements(By.CLASS_NAME, 'tablehead')[1]
    forward_button = pagination_string.find_element(By.CSS_SELECTOR, 'a[title=\"К следующей странице\"]')

    return message_table, forward_button

def manage_message_blocks(writer, message_table):
    message_blocks = message_table.find_elements(By.CLASS_NAME, 'posttable')

    for message in message_blocks:
        try:
            message_username = message.find_element(By.CLASS_NAME, 'username')
            message_descr = message.find_element(By.CLASS_NAME, 'descr')
            message_datetime = message.find_element(By.CLASS_NAME, 'postnav2')
            message_text = message.find_element(By.CSS_SELECTOR, 'div[id^=\"p\"]')

            message_descr_text_parsed = message_descr.text.replace('\n', ' ')

            writer.writerow([message_username.text, message_descr_text_parsed,
                            message_datetime.text, message_text.text])
        except Exception as e:
            print("Could not extract message:", e)

driver = start_webdriver(url)

with open('message_report.csv', 'w', newline='') as file:
    writer = start_csv_writer(file)

    while True:
        try:
            message_table, forward_button = manage_pagination(driver)   
            manage_message_blocks(writer, message_table)
            forward_button.click()
        except:
            message_table = driver.find_element(By.ID, 'maintableID')
            manage_message_blocks(writer, message_table)
            break

driver.quit()