import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instrutor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://bjiwan.pythonanywhere.com/admin/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://rdanuwar1.pythonanywhere.com/")
       assert "Logged In"
       time.sleep(3)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

