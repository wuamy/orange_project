from selenium.webdriver.common.by import By

class AdminPage:

  # admin page elements
  admin_page_title = (By.XPATH, "//h6[normalize-space()='User Management']")
  btn_add_new_user_xpath = (By.XPATH, "//button[normalize-space()='Add']")


  def __init__(self, driver):
    self.driver = driver

      
    
