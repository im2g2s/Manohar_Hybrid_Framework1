from threading import Thread

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from Utilities.readProperties import Readconfig
import time
from  Utilities.customLogger import LogGen
from Utilities import XLUtils
import pytest
import time
from PageObjects.AddNewCustomerPage import AddCustomer
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    BaseURl = Readconfig.getApplicationURl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger  = LogGen.loggen()


    # def generate_random_string(length=8):
    #     characters = string.ascii_letters + string.digits
    #     return ''.join(random.choice(characters) for _ in range(length))
    # pytest TestCases / test_add_customer.py

    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_download(self, setup):
        filePath =r"C:\Users\manoh\PycharmProjects\Manohar_Hybrid_Framework\Utilities\download.xlsx"
        self.logger.info("************* Test upload **********")
        self.driver = setup
        self.driver.get(self.BaseURl)

        self.driver.implicitly_wait(5000)
        # self.lp = LoginPage(self.driver)
        # self.lp.setUsername(self.username)
        self.driver.find_element(By.XPATH,"//input[@type='file']").send_keys(filePath)




        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


