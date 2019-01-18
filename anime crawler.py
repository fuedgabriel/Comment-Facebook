import time
import os
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

login = ""
password = ""










options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(firefox_options=options)

driver.get('https://www.facebook.com/')
time.sleep(5)


username = driver.find_element_by_xpath('//*[@id="email"]')
username.send_keys(login)

username = driver.find_element_by_xpath('//*[@id="pass"]')
username.send_keys(password)
driver.find_element(By.XPATH, '//*[@id="u_0_2"]').click()


time.sleep(5)
driver.get('https://www.facebook.com/permalink.php?story_fbid=1146976122134338&id=100004658823176')
time.sleep(5)
driver.execute_script('window.scrollBy(0, 100000000)')
driver.execute_script('window.scrollBy(0, 100000000)')
driver.execute_script('window.scrollBy(0, 100000000)')
driver.execute_script('window.scrollBy(0, 100000000)')
driver.execute_script('window.scrollBy(0, 100000000)')
time.sleep(3)
def page():
    for sou_cuzao in range(315, 2000):
        print(str(sou_cuzao))
 #       msg = driver.find_element_by_css_selector("._1mf").send_keys(str(sou_cuzao))
        #time.sleep(1)
        pyautogui.moveTo(340, 647)
        pyautogui.click()
        pyautogui.typewrite(str(sou_cuzao))
        pyautogui.press("return")
        driver.execute_script('window.scrollBy(0, 100000000)')
        driver.execute_script('window.scrollBy(0, 100000000)')
        driver.execute_script('window.scrollBy(0, 100000000)')
        driver.execute_script('window.scrollBy(0, 100000000)')
        driver.execute_script('window.scrollBy(0, 100000000)')
        #msg.send_keys(str(sou_cuzao))
        #driver.findElement(By.XPATH('//*[@id="u_0_10"]/div/div[3]/div[4]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div')).sendKeys(Keys.ENTER)

        

page()
driver.close()


