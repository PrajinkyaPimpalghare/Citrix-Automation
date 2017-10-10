"""============================================================================
INFORMATION ABOUT CODE         Coding: ISO 9001:2015
===============================================================================
For Automating Citirix reciver getway
It opens Explorer and Remote desktop Connection windows directly
*Change Tkinker name in Python 3

Author: Prajinkya Pimpalghare

Date: 10-October-2017
Version: 1.0
Input Variable: Citrix[#01] URL and Username/Password[#02]
Basic Requirement Selenium module, and Web driver for chrome
============================================================================"""

import os
import time
from selenium import webdriver


class CitrixAutomation(object):
    """ For Automating Login in Citrix and opening its resources"""

    def __init__(self, username, password, url):
        """
        For Taking the basic elements required for accessing Citrix
        :param username:
        :param password:
        :param url:
        """
        self.path = os.environ["USERPROFILE"]
        self.username = username
        self.password = password
        self.url = url
        self.chrome_option = webdriver.ChromeOptions()

    def run_automation(self):
        """
        It actually runs and automate the whole process
        """
        [os.remove(os.path.join(self.path, "Downloads", path)) for path in
         os.listdir(os.path.join(self.path, "Downloads")) if
         path.endswith(".ica")]  # Removing .ica file: Downloaded after running citrix browser
        self.chrome_option.add_argument("--proxy-server=")  # For disabling proxy
        browser = webdriver.Chrome(chrome_options=self.chrome_option)
        browser.get(self.url)
        login = browser.find_element_by_id("Enter user name")
        password = browser.find_element_by_name("passwd")
        login.send_keys(self.username)
        password.send_keys(self.password)
        browser.find_element_by_id("Log_On").click()
        browser.find_element_by_id("folderLink_0").click()
        remote_desktop_id = "idCitrix.MPS.App.XA_005feurope_005fPROD.RDP_0020Client6E8A"
        browser.find_element_by_id(remote_desktop_id).click()
        internet_explorer = "idCitrix.MPS.App.XA_005feurope_005fPROD.Internet_0020Explorer_002011"
        browser.find_element_by_id(internet_explorer).click()
        time.sleep(3)
        [os.startfile(os.path.join(self.path, "Downloads", path)) for path in
         os.listdir(os.path.join(self.path, "Downloads")) if path.endswith(".ica")]
        exit(0)


if __name__ == '__main__':
    USERNAME = "username"  # Add username
    PASSWORD = "password"  # Add password
    URL = "https://portal.url/vpn/index.html"  # Add url
    TEMP = CitrixAutomation(username=USERNAME, password=PASSWORD, url=URL)
    TEMP.run_automation()
