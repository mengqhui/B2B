# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class QinfafaMemberxx(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Ie()
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.qinfawang.com/"
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_qinfafa_memberxx(self):
		driver = self.driver
		driver.get(self.base_url + "/member/fabu.php?mid=5&action=add")
		driver.find_element_by_id("title").clear()
		driver.find_element_by_id("title").send_keys(u"塔城经销阳光电池A512/120A放心省心")
		driver.find_element_by_id("key1").clear()
		driver.find_element_by_id("key1").send_keys(u"德国阳光电池旭祥")
		driver.find_element_by_id("key2").clear()
		driver.find_element_by_id("key2").send_keys(u"内蒙德国阳光蓄电")
		driver.find_element_by_id("key3").clear()
		driver.find_element_by_id("key3").send_keys(u"原装德国阳光蓄电")
		Select(driver.find_element_by_css_selector("select")).select_by_visible_text(u"机械设备")
		driver.find_element_by_css_selector("option[value=\"1043\"]").click()
		Select(driver.find_element_by_xpath("//span[@id='load_category_1']/select[2]")).select_by_visible_text(u"电子设备")
		
		driver.find_element_by_id("showthumb").click()
		driver.find_element_by_id("upalbum").clear()
		driver.find_element_by_id("upalbum").send_keys(u"D:\\工作资料\\[德国阳光工业集团电池图片]\\2v3351.jpg")
		
		#driver.find_element_by_name("post[elite]").click()
		#driver.find_element_by_name("submit").click()
	
	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return True
	
	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException as e: return False
		return True
	
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True
	
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()
