from selenium import webdriver
import pytest

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