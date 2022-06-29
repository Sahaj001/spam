from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import sys
import time
import os
import argparse


def run(driver_path, name, files):

    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com/')

    search_box = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
    time.sleep(1)

    pyperclip.copy(name)
    search_box.send_keys(Keys.CONTROL + "v")
    time.sleep(1)

    name_title = driver.find_element(By.XPATH, f'//span[@title="{name}"]')
    name_title.click()
    time.sleep(1)

    input_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
    input_box = driver.find_element(By.XPATH, input_xpath)

    pyperclip.copy("Sending...")
    input_box.send_keys(Keys.CONTROL + "v")
    input_box.send_keys(Keys.ENTER)
    time.sleep(1)

    # sending only 10 files
    i = 1
    for file in files[:2]:
        attachment_box = driver.find_element(By.XPATH,'//div[@title="Attach"]')
        attachment_box.click()
        time.sleep(1)

        image_box = driver.find_element(By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(file)
        time.sleep(1)

        caption_box = driver.find_element(By.XPATH, input_xpath)
        
        caption = str(i) # Catption for each file
        pyperclip.copy(caption) 
        caption_box.send_keys(Keys.CONTROL + "v")

        send_btn = driver.find_element(By.XPATH,'//span[@data-icon="send"]')
        send_btn.click()
        time.sleep(1)
        i+=1


if __name__ == '__main__':
    
    DRIVER_PATH = r'D:\Softwares\chromedriver_win32\chromedriver.exe'
    FOLDER = r'C:\Users\apil0\OneDrive\Desktop\whatsapp_auto\test'

    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--name", type=str, required=True, help="WhatsApp Contact Name")
    parser.add_argument("-p","--path", type=str, help="Folder Path", default=FOLDER)
    parser.add_argument("-d","--driver", type=str, help="ChromeDriver Path", default=DRIVER_PATH)
    opt = parser.parse_args()

    name = opt.name
    path = opt.path
    driver_path = opt.driver

    files = []
    for file in os.listdir(path):
        files.append(path +'\\' + file)

    run(driver_path, name, files)