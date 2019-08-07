import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.get("http://bjiwan.pythonanywhere.com/home/")
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span").click()
        time.sleep(1)


        elem = driver.find_element_by_xpath("//*[@id=\"id_cust_name\"]/option[2]").click()

        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("Room services")

        elem = driver.find_element_by_id("id_description")
        elem.send_keys("delivered food in the room")

        elem = driver.find_element_by_id("id_location")
        elem.send_keys("I like in omaha.")

        elem = driver.find_element_by_id("id_setup_time")
        elem.clear()
        elem.send_keys("8/02/2019")

        elem = driver.find_element_by_id("id_cleanup_time")
        elem.clear()
        elem.send_keys("08/03/2019")

        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("25.99")

        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        time.sleep(1)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()