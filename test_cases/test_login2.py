from selenium.webdriver.common.by import By
from utilities.custom_logger import LogGen
import time

class Test_001_Login:

  # define log object
  log = LogGen.logger()

  # test start here
  def test_login(self, setup):
    self.log.info("****************test login process **************")
    
    self.driver = setup
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



    



