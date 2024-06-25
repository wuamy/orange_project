from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
import time

######### Add multiple browser ################
@pytest.fixture
def browser_sel(browser,request):
  
  if browser == 'firefox':
     driver = webdriver.Firefox()
  elif browser == 'edge':
     driver = webdriver.Edge()
  else:
      driver = webdriver.Chrome()

  # Teardown (finalizer) to quit the browser
  def teardown():
        driver.quit()
  
  request.addfinalizer(teardown)
  return driver

@pytest.fixture
def setup(browser_sel):
  baseURL = ReadConfig.get_app_url()
  username = ReadConfig.get_app_username()
  password = ReadConfig.get_app_password()

  browser_sel.get(baseURL)
  time.sleep(2)
  LoginPage(browser_sel).set_username(username)
  LoginPage(browser_sel).set_password(password)
  LoginPage(browser_sel).click_login()
  
  return browser_sel


def pytest_addoption(parser):
  parser.addoption("--browser")

@pytest.fixture
def browser(request):
  return request.config.getoption("--browser")

######## genetate html report #############

#### Add a report title #######
def pytest_html_report_title(report):
    report.title = "Orange Project Test Report"

#### Add test env information #####
def pytest_configure(config):
    config.stash[metadata_key]["Test Project"] = "Orange Project"
    config.stash[metadata_key]["Tester"] = "Amy"
  
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)