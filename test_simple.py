from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Test_Simple:


  website = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
  path = "C:\project\selenium_driver\chromedriver.exe"
  # driver = webdriver.Chrome(service=Service(path))
  driver = webdriver.Chrome()
  driver.get(website)
  time.sleep(2)
  driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys('Admin')
  driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('admin123')
  driver.find_element(By.XPATH, "//button[@type='submit']").click()

  # working on admin tab
  time.sleep(2)
  driver.find_element(By.XPATH, '//a[@href="/web/index.php/admin/viewAdminModule"]').click()
  time.sleep(2)
  # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
  driver.find_element(By.XPATH, '//button[normalize-space()="Add"]').click()

           
