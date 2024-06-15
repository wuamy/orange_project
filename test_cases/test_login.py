from selenium import webdriver
import pytest
from page_objects.login_page import LoginPage
import time
from utilities.read_properties import ReadConfig 

class Test_001_Login:

  # baseURL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
  # username = 'Admin'
  # password = 'admin123'
  
  baseURL = ReadConfig.get_app_url()
  username = ReadConfig.get_app_username()
  password = ReadConfig.get_app_password()

  def test_home_page(self, setup):
    self.driver = setup
    self.driver.get(self.baseURL)
    time.sleep(3)
    act_title = self.driver.title
    self.driver.close()
    if act_title == 'OrangeHRM':
      assert True
    else:
      assert False

  def test_login_page(self, setup):
    # self.driver = setup
    self.driver = setup
    self.driver.get(self.baseURL)
    
    self.pl = LoginPage(self.driver)
    time.sleep(2)
    
    self.pl.set_username(self.username)
    self.pl.set_password(self.password)
    self.pl.click_login()
    time.sleep(2)
    self.driver.close()



    



