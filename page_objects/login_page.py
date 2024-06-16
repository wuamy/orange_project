from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class LoginPage(BasePage):

  # page element locators
  txtbox_username_xpath = (By.XPATH, '//input[@placeholder="Username"]')
  txtbox_password_xpath = (By.XPATH, '//input[@placeholder="Password"]')
  btn_login_xpath = (By.XPATH, "//button[@type='submit']")

  def set_username(self, username):
    # self.driver.find_element(*self.txtbox_username_xpath).send_keys(username)
    self.locator(self.txtbox_username_xpath).send_keys(username)
    
  def set_password(self, password):
    # self.driver.find_element(*self.txtbox_password_xpath).send_keys(password)
    self.locator(self.txtbox_password_xpath).send_keys(password)

  def click_login(self):
    # self.driver.find_element(*self.btn_login_xpath).click()
    self.locator(self.btn_login_xpath).click()

  
