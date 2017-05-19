# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Huangyegg(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://fabuxinxi.huangye88.com/"
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_huangyegg(self):
		
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("subject").clear()
		driver.find_element_by_id("subject").send_keys(u"北京销售阳光蓄电池A512/2S优质服务")
		driver.find_element_by_id("content").click()
		driver.find_element_by_id("content").clear()
		driver.find_element_by_id("content").send_keys(u"（4.13）\n212.50 %\n1,选用固体凝胶电解质。在对等体积下,电解质容量大,热容量大,热丧失才气强,能防止普通蓄电池易发作的热失控表象。对环境温度的习气才气（高,低温）强。\n3.1．UPS框架结构\nThe Supervision and Monitoring to the VRLA Battery in the Substation\n现场检查：\n无\n   -> Restores the contents of all the registers from the stack Arguments\nJ\n* 《电子信息系统机房施工和验收规范》（GB50462-2008）\n （1）规划、设计和建设、投产、运行等阶段；\nV\n60%\n　　					  40/80/100/160KVA机器包装箱\n是\n　　网络应允许控制用户对目录、文件和设备的访问。用户在目录一级指定的权限对所有文件 和子目录有效，用户还可进一步指定对目录下的子目录和文件的权限。对目录和文件的访问权 限一般有8种:系统管理员权限(supervisor)、读权限(read)、写权限(write)、创建权限(create)、 删除权限(erase)、修改权限(modify)、文件查找权限(file scan)、存取控制权限(access control)。8")
		driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
		driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(u"安徽德国阳光蓄电池")
		# ERROR: Caught exception [Error: Dom locators are not implemented yet!]
		driver.find_element_by_xpath("//form[@id='postform']/div[7]/div/input").clear()
		driver.find_element_by_xpath("//form[@id='postform']/div[7]/div/input").send_keys(u"鞍山德国阳光蓄电池")
		driver.find_element_by_id("productname0").clear()
		driver.find_element_by_id("productname0").send_keys(u"德国阳光蓄电池对比")
		driver.find_element_by_id("productname1").clear()
		driver.find_element_by_id("productname1").send_keys(u"德国阳光60蓄电池")
		driver.find_element_by_id("productname2").clear()
		driver.find_element_by_id("productname2").send_keys(u"进口德国阳光蓄电池")
		driver.find_element_by_xpath("//form[@id='postform']/div[12]/div/div/div/button").click()
		driver.find_element_by_xpath(u"//span[@value='台']").click()
		driver.find_element_by_name("unitnum[]").clear()
		driver.find_element_by_name("unitnum[]").send_keys("1")
		driver.find_element_by_name("unitprice[]").clear()
		driver.find_element_by_name("unitprice[]").send_keys("1")
		driver.find_element_by_name("unittotal").clear()
		driver.find_element_by_name("unittotal").send_keys("100")
		driver.find_element_by_link_text(u"已填好，我要发布").click()
	
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
