from configparser import ConfigParser

def get_config(category,key):
    con = ConfigParser()
    con.read("C:\\Users\\SM\\Desktop\\Pytest_clone\\Pytest_OrangeHRM\\Configurations\\config.ini")
    con.read("E:\gitpytest_clone\Pytest_OrangeHRM\Configurations\config.ini")
    return con.get(category,key)