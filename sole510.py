# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Sole510(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://user.51sole.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sole510(self):
        driver = self.driver
		driver.get(self.base_url + "/user/commerces/createinfornew.aspx?bigtype=1&type=0")
		driver.find_element_by_id("txtKeyword1421").clear()
		driver.find_element_by_id("txtKeyword1421").send_keys(u"德国阳光")
		driver.find_element_by_id("txtCommerceTitle").clear()
		driver.find_element_by_id("txtCommerceTitle").send_keys(u"北京销售阳光蓄电池A512/1.2 S 行业领先")
		driver.find_element_by_id("rbtnlsCommerceIndustry_3").click()
		driver.find_element_by_id("Radio_60787").click()
		driver.find_element_by_id("txt_69778").clear()
		driver.find_element_by_id("txt_69778").send_keys("6-fm-120")
		driver.find_element_by_id("Radio_60950").click()
		driver.find_element_by_id("Radio_60961").click()
		driver.find_element_by_id("Radio_60963").click()
		driver.find_element_by_id("Radio_333338").click()
		driver.find_element_by_id("pickongjian").click()
		driver.find_element_by_link_text(u"×").click()
		driver.find_element_by_id("pickfilesUpload").click()
		driver.find_element_by_id("html5_1bgco4neuklpcvd1r8g3071c3j3").clear()
		driver.find_element_by_id("html5_1bgco4neuklpcvd1r8g3071c3j3").send_keys("")
		driver.find_element_by_id("txtBrand245").clear()
		driver.find_element_by_id("txtBrand245").send_keys(u"德国阳光")
		driver.find_element_by_id("txtCaseDetail").clear()
		driver.find_element_by_id("txtCaseDetail").send_keys(u"包装")
		driver.find_element_by_id("txtProductSpec").clear()
		driver.find_element_by_id("txtProductSpec").send_keys("A412/65G6")
		driver.find_element_by_id("txtCommerceContent").clear()
		driver.find_element_by_id("txtCommerceContent").send_keys(u"规格及型号\n①事实上，理论框架建立过程的本身，就是一项综合评价工作。\n※ 蓄电池到了寿命末期(是初期放电时间的50%时)使用可能时间明显缩短。并且最终会造成\n转换时间\n1000(7*)\n6.1极板车间主要设备的计算机选型\n　反充\n 1A050，1A051\nCB3\n　　域名对网站来说是极其重要的一个部分，是网站的\"商标\"。所谓域名，是指一种基于IP 地址的层次化的主机命名方式。从技术上讲，域名是一种用于解决IP地址不易记忆的方法； 从管理角度来看，层次化的域名体系使IP地址的使用更有秩序、更容易管理，是比IP地址更 高级的地址形式。域名具有世界惟一性，域名注册机构保证全球范围内没有重复的域名。\n毕业设计开题报告\n38\n电池特性\n-9. 54\n2PL\n建立从业人员安全培训教育档案。\n电池\nmov ah,3Eh\n3.1网络服务器的选择	85\n查文件：\n外形尺寸（mm）深×宽×高\n　　Proxy代理服务器软件包括WinGate、CC代理服务器和Win代理服务器；NAT类型代理 服务器软件包括MS代理服务器、WinRoute和SyGate等。\n15110208454\n18621631419\nwww.sonnenlicht029.com\nwww.upszhijia.com")
		driver.find_element_by_id("btn_newCommerce").click()
    
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
