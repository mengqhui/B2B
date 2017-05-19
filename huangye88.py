# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,random,codecs

titiles=codecs.open(u'黄页88标题生成20151208_175612(1).txt','r','utf-8').readlines()
keywords=codecs.open(u'keys.txt','r','utf-8').readlines()
myinfo='''15110208454
18621631419
www.sonnenlicht029.com/
www.upszhijia.com/
'''
class Huangye88(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Ie()
		self.driver.implicitly_wait(30)
		self.base_url = "http://fabuxinxi.huangye88.com/"
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_huangye88(self):
		for i in range(5):
			driver = self.driver
			driver.get(self.base_url + "/")
			'''
			driver.find_element_by_id("mainV").clear()
			driver.find_element_by_id("mainV").send_keys("UPS")
			driver.find_element_by_link_text(u"消费品>IT>网络设备>ups电源").click()
			'''
			try:
				driver.find_element_by_xpath('//*[@id="recoveryModal"]/div[3]/button[2]').click()
				#button2.click()
				#driver.find_element_by_link_text("不恢复").click()
			finally:
				print i
				fpath='a/'+str(random.randrange(1,200))+'.txt'
				contexts=codecs.open(fpath,'r','utf-8').readlines()
				context='\n'.join(contexts)
				driver.find_element_by_id("subject").clear()
				driver.find_element_by_id("subject").send_keys(random.choice(titiles))
				driver.find_element_by_id("content").click()
				driver.find_element_by_id("content").clear()
				driver.find_element_by_id("content").send_keys(context+myinfo)
				driver.find_element_by_css_selector("input.input-small.ml5").clear()
				driver.find_element_by_css_selector("input.input-small.ml5").send_keys(random.choice(keywords))
				driver.find_element_by_css_selector("input.input-small.ml5").clear()
				driver.find_element_by_css_selector("input.input-small.ml5").send_keys(random.choice(keywords))
				driver.find_element_by_css_selector("input.input-small.ml5").clear()
				driver.find_element_by_css_selector("input.input-small.ml5").send_keys(random.choice(keywords))
				driver.find_element_by_id("productname0").clear()
				driver.find_element_by_id("productname0").send_keys(random.choice(keywords))
				driver.find_element_by_id("productname1").clear()
				driver.find_element_by_id("productname1").send_keys(random.choice(keywords))
				driver.find_element_by_id("productname2").clear()
				driver.find_element_by_id("productname2").send_keys(random.choice(keywords))
				driver.find_element_by_css_selector("button.dropdown-toggle.sugBtn").click()
				driver.find_element_by_xpath(u"//span[@value='台']").click()
				driver.find_element_by_name("unitnum[]").clear()
				driver.find_element_by_name("unitnum[]").send_keys("1")
				driver.find_element_by_name("unitprice[]").clear()
				driver.find_element_by_name("unitprice[]").send_keys("1")
				driver.find_element_by_id("4").clear()
				driver.find_element_by_id("4").send_keys("100")
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
