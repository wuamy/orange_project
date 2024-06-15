import configparser

config = configparser.RawConfigParser()
config.read('.\\configuration\\config.ini')

class ReadConfig:
  @staticmethod
  def get_app_url():
    url = config.get('common info', 'baseURL')
    return url

  @staticmethod
  def get_app_username():
    username = config.get('common info', 'username')
    return username

  @staticmethod
  def get_app_password():
    password = config.get('common info', 'password')
    return password