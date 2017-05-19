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

class QinfafaNew(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.qinfawang.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_qinfafa_new(self):
		for i in range(5):
			driver = self.driver
			driver.get(self.base_url + "/member/news.php?action=add")
			driver.find_element_by_id("title").clear()
			driver.find_element_by_id("title").send_keys(random.choice(titiles))
			#<iframe class="ke-edit-iframe" hidefocus="true" frameborder="0" tabindex="" style="width: 100%; height: 261px;"></iframe>
			#//*[@id="dform"]/table/tbody/tr[2]/td[2]/div/div[2]/iframe
			frame = driver.find_element_by_xpath('//*[@id="dform"]/table/tbody/tr[2]/td[2]/div/div[2]/iframe')
			driver.switch_to.frame(0)
		
			fpath='a/'+str(random.randrange(1,200))+'.txt'
			contexts=codecs.open(fpath,'r','utf-8').readlines()
			myinf=u"15110208454<br>18621631419<br>www.sonnenlicht029.com<br>www.upszhijia.com"
			context='<br>'.join(contexts)+myinf
			bod=driver.find_element_by_class_name('ke-content')
			bod.clear()
			bod.send_keys(context)
			driver.switch_to.default_content()
			
			driver.find_element_by_name("submit").click()
		
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
