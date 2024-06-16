from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig 
from utilities.custom_logger import LogGen
import time

class Test_001_Login:

  # baseURL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
  # username = 'Admin'
  # password = 'admin123'
  
  baseURL = ReadConfig.get_app_url()
  username = ReadConfig.get_app_username()
  password = ReadConfig.get_app_password()

  # define log object
  log = LogGen.logger()

  def test_login_page_title(self, setup):
    self.log.info("**************** test_login_page title **************************")
    self.log.info("**************** verify login page title ************************")
    self.driver = setup
    self.driver.get(self.baseURL)
    time.sleep(3)
    act_title = self.driver.title
    
    if act_title == 'OrangeHRM':
      assert True
      self.driver.close()
      self.log.info("*************** test_login_page title Pass *************")
      
    else:
      self.driver.close()
      self.log.info("*************** test_login_page title Fail *************")
      assert False

  def test_login(self, setup):
    self.log.info("****************test login process **************")
    # self.driver = setup
    self.driver = setup
    self.driver.get(self.baseURL)
    
    self.pl = LoginPage(self.driver)
    time.sleep(2)
    
    self.pl.set_username(self.username)
    self.pl.set_password(self.password)
    self.pl.click_login()
    time.sleep(2)

    page_title = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text
    # print(page_title)
    if page_title == 'Dashboard':
      assert True
      self.driver.close()
      self.log.info("************** test login process PASS **********")
    else:
      self.driver.close()
      self.log.info("************** test login process Failed*********")
      assert False



    



