from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key

######### Add multiple browser ################
@pytest.fixture
def setup(browser):
  if browser == 'firefox':
     driver = webdriver.Firefox()
  elif browser == 'edge':
     driver = webdriver.Edge()
  else:
      driver = webdriver.Chrome()
  return driver

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