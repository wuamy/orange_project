from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class AdminPage(BasePage):

  # admin page elements
  admin_page_title_xpath = (By.XPATH, "//h6[normalize-space()='User Management']")
  btn_add_new_user_xpath = (By.XPATH, "//button[normalize-space()='Add']")
  txt_admin_xpath = (By.XPATH, "//h6[normalize-space()='Admin']")
  sel_user_role_xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div')

  def click_add_user_button(self):
    self.driver.locator(self.btn_add_new_user_xpath).click()


      
    
