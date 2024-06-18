import time

# base class
'''
  1. locate elements
  2. open browser and access url
  3. close browser and release resource
'''

class BasePage:

  # define constructure
  def __init__(self, driver):
    self.driver = driver

  def locator(self, loc):
    return self.driver.find_element(*loc)

  def quit(self):
    time.sleep(2)
    self.driver.quit()   