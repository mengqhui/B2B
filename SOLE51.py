# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SOLE51(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://user.51sole.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_s_o_l_e51(self):
        driver = self.driver
		driver.get(self.base_url + "/user/commerces/createinfornew.aspx?bigtype=1&type=0")
		driver.find_element_by_id("Rd_0").click()
		driver.find_element_by_id("next_step").click()
		driver.find_element_by_id("txtKeyword1715").clear()
		driver.find_element_by_id("txtKeyword1715").send_keys("12V100AH")
		driver.find_element_by_id("txtCommerceTitle").clear()
		driver.find_element_by_id("txtCommerceTitle").send_keys(u"北京代理阳光蓄电池A512/1.2 S 低价促销")
		driver.find_element_by_id("rbtnlsCommerceIndustry_3").click()
		#driver.find_element_by_css_selector("div.showbtn > span").click()
		driver.find_element_by_id("Radio_60789").click()
		driver.find_element_by_id("txt_69778").clear()
		driver.find_element_by_id("txt_69778").send_keys("6-FM-100")
		driver.find_element_by_id("Radio_60950").click()
		driver.find_element_by_id("Radio_60961").click()
		driver.find_element_by_id("Radio_60963").click()
		driver.find_element_by_id("Radio_333338").click()
		driver.find_element_by_id("pickongjian").click()
		driver.find_element_by_css_selector(u"img[alt=\"阳光电池20.jpg\"]").click()
		driver.find_element_by_id("insertOk").click()
		driver.find_element_by_id("txtBrand329").clear()
		driver.find_element_by_id("txtBrand329").send_keys(u"松下")
		driver.find_element_by_id("txtCaseDetail").clear()
		driver.find_element_by_id("txtCaseDetail").send_keys(u"包装")
		driver.find_element_by_id("txtProductSpec").clear()
		driver.find_element_by_id("txtProductSpec").send_keys("6-FM-100")
		driver.find_element_by_id("txtCommerceContent").clear()
		driver.find_element_by_id("txtCommerceContent").send_keys(u"kJ/次\n        几乎所有的蓄电池生产厂都在各种用途的铅膏中加入BaSO4。\n深放电\n启动开关 强制应急启动开关\n②、\n　　放电2：  10A电流放至10.5V；\n(1)\n25.3(68.2 %)\n80\nInlet1\n143\n　　充电电路的功能是在市电正常时对蓄电池组进行充电，并对蓄电池组进行日常维护性浮充充电，以满足蓄电池组自故电的要求。在充电初期，以恒流方式充电；在充电后期，以恒压方式充电；最后以浮充方式充电。充电电路是由主电路和控制电路组成，其电路如图5-1所示。\n     ⑶直流屏交流进线连接应先接好屏端连线，断开屏内交流进线开关，再检查源端断路器是否处于断开状态，确认后方可连接电源端连线；连好后应检查屏内交流进线开关前端电压是否正确。\n　　如果考虑到与使用原来版本的客户兼容(网络中还存在其他的Windows NT Server 4.0域) 以及域的可用性等问题,第3种方案将是最佳方案。这样在Windows 2000 Server与Windows NT Server之间发生了复制问题时可以有一条退路，或者当主域控制器出现问题时还有另一个 Windows 2000 Server域控制器保证域的正常使用。")
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
