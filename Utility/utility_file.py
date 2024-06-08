from configparser import ConfigParser

def get_config(category,key):
    con = ConfigParser()
    con.read("D:\\Pytest_Clone_HRM\\Pytest_OrangeHRM\\Configurations\\config.ini")
    return con.get(category,key)