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

class QinfafaIde(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Ie()
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.qinfawang.com"
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_qinfafa_ide(self):
		for i in range(5):
			driver = self.driver
			driver.get(self.base_url + "/member/fabu.php?mid=5&action=add")
			driver.find_element_by_id("title").clear()
			driver.find_element_by_id("title").send_keys(random.choice(titiles))
			driver.find_element_by_id("key1").clear()
			driver.find_element_by_id("key1").send_keys(random.choice(keywords))
			driver.find_element_by_id("key2").clear()
			driver.find_element_by_id("key2").send_keys(random.choice(keywords))
			driver.find_element_by_id("key3").clear()
			driver.find_element_by_id("key3").send_keys(random.choice(keywords))
			Select(driver.find_element_by_css_selector("select")).select_by_visible_text(u"机械设备")
			frame = driver.find_element_by_xpath('//*[@id="dform"]/table/tbody/tr[6]/td[2]/div/div[2]/iframe')
			#//*[@id="dform"]/table/tbody/tr[6]/td[2]/div/div[2]/iframe
			#//*[@id="dform"]/table/tbody/tr[2]/td[2]/div/div[2]/iframe
			driver.switch_to_frame(frame)
			
			fpath='a/'+str(random.randrange(1,200))+'.txt'
			contexts=codecs.open(fpath,'r','utf-8').readlines()
			lili=""
			for context in contexts:
				lili=lili+context.strip('\n')+'<br>'
	
			myinf="15110208454<br>18621631419<br>www.sonnenlicht029.com<br>www.upszhijia.com"
			'''
			js ='document.body.innerHTML="'+unicode(lili)+myinf+'"'
			#print js
			driver.execute_script(js)
			'''
			bod=driver.find_element_by_class_name('ke-content')
			bod.clear()
			bod.click()
			bod.send_keys(lili+myinf)
			driver.switch_to.default_content()
	
			driver.find_element_by_css_selector("option[value=\"1043\"]").click()
			driver.find_element_by_id("showthumb").click()
			driver.find_element_by_id("upalbum").clear()
			driver.find_element_by_id("upalbum").send_keys(u"D:\\工作资料\\[德国阳光工业集团电池图片]\\2v3351.jpg")
			driver.find_element_by_name("post[elite]").click()
			driver.find_element_by_name("submit").click()
	'''
			try:
				EC.alert_is_present
				print("Alert exists")
				alert=driver.switch_to_alert()
				print ('alert.text:',alert.text)
				alert.accept()
				print("Alert accepted")
			except:
				print("NO alert exists except")
			else:
				print("NO alert exists")
'''
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
