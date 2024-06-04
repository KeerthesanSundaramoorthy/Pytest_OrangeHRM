from configparser import ConfigParser

def get_config(category,key):
    con = ConfigParser()
    con.read("E:\\Pytest_OrangeHRM\\Configurations\\config.ini")
    return con.get(category,key)