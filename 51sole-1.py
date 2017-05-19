# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,random,codecs

titiles=open(u'黄页88标题生成20151208_193812.txt','r').readlines()
keywords=open(u'keys.txt','r').readlines()
myinfo='''15110208454
18621631419
www.sonnenlicht029.com/
www.upszhijia.com/
'''
fpath='a/'+str(random.randrange(1,200))+'.txt'
context=open(fpath,'r').readlines()

driver = webdriver.Chrome()
driver.implicitly_wait(30)
base_url = "http://user.51sole.com/user/commerces/createinfornew.aspx?bigtype=1&type=0"
#http://user.51sole.com/user/commerces/createinfornew.aspx?bigtype=1&type=0&AccountID=LaRiMac
driver.get('http://user.51sole.com/')
try:
	assert u"发布商机" in driver.title
	print ('Assertion test pass.')
except Exception as e:
	print ('Assertion test fail.', format(e))
	time.sleep(30)

print('Get ready!')
print(driver.title)
#time.sleep(60)
print('Go!')

def sole():
	driver.get(base_url)
	print(driver.title)
	driver.find_element_by_id("Rd_0").click()
	driver.find_element_by_id("next_step").click()
	time.sleep(3)
	'''
	driver.find_element_by_id("txtCommerceTitle").clear()
	driver.find_element_by_id("txtCommerceTitle").send_keys(unicode(random.choice(titiles)))
	driver.find_element_by_id("rbtnlsCommerceIndustry_2").click()
	driver.find_element_by_css_selector("div.showbtn > span").click()
	driver.find_element_by_id("Radio_60793").click()
	driver.find_element_by_id("Radio_60788").click()
	driver.find_element_by_id("rbtnlsCommerceIndustry_3").click()
	driver.find_element_by_id("txt_69778").clear()
	driver.find_element_by_id("txt_69778").send_keys("A412/65G6")
	driver.find_element_by_id("Radio_60950").click()
	driver.find_element_by_id("Radio_60961").click()
	driver.find_element_by_id("Radio_60963").click()
	driver.find_element_by_xpath("(//span[@onclick='ShowAllAttr(this)'])[5]").click()
	driver.find_element_by_id("Radio_333340").click()
	driver.find_element_by_id("Radio_333338").click()
	driver.find_element_by_id("pickongjian").click()
	driver.find_element_by_css_selector("img[alt=\"50a (4).jpg\"]").click()
	driver.find_element_by_id("insertOk").click()
	driver.find_element_by_id("txtBrand668").clear()
	driver.find_element_by_id("txtBrand668").send_keys(u"德国阳光")
	driver.find_element_by_id("txtCaseDetail").clear()
	driver.find_element_by_id("txtCaseDetail").send_keys(u"全包装")
	driver.find_element_by_id("txtProductSpec").clear()
	driver.find_element_by_id("txtProductSpec").send_keys("A412/65G6")
	driver.find_element_by_id("txtCommerceContent").clear()
	driver.find_element_by_id("txtCommerceContent").send_keys(context)
	driver.find_element_by_id("txtCommerceContent").send_keys(myinfo)
	driver.find_element_by_id("btn_newCommerce").click()
	#'''
	
for i in range(2):
	print u'序号:',i
	sole()

driver.quit()