# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, codecs

titiles = codecs.open(u'黄页88标题生成20151208_175612(1).txt', 'r','utf-8').readlines()
keywords = codecs.open(u'keys.txt', 'r', 'utf-8').readlines()
myinfo = '''15110208454
18621631419
www.sonnenlicht029.com/
www.upszhijia.com/
'''
driver = webdriver.Ie()
driver.implicitly_wait(30)
base_url = "http://fabuxinxi.huangye88.com/"
verificationErrors = []
accept_next_alert = True
#for i in range(5):
driver.get(base_url + "/")
try:
	driver.find_element_by_xpath("//div[@id='recoveryModal']/div[3]/button[2]").click()
finally:
	fpath = 'a/' + str(random.randrange(1, 200)) + '.txt'
	contexts = codecs.open(fpath, 'r', 'utf-8').readlines()
	context = ""
	context = '\n'.join(contexts) + myinfo
	driver.find_element_by_id("content").click()
	driver.find_element_by_id("content").clear()
	driver.find_element_by_id("content").send_keys(context)

	driver.find_element_by_id("subject").clear()
	driver.find_element_by_id("subject").send_keys(
		random.choice(titiles))
	for i in range(3):
		driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
		driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(random.choice(keywords))

	driver.find_element_by_id("productname0").clear()
	driver.find_element_by_id("productname0").send_keys(
		random.choice(keywords))
	driver.find_element_by_id("productname1").clear()
	driver.find_element_by_id("productname1").send_keys(
		random.choice(keywords))
	driver.find_element_by_id("productname2").clear()
	driver.find_element_by_id("productname2").send_keys(
		random.choice(keywords))
	#"//form[@id='postform']/div[12]/div/div/div/button"
	driver.find_element_by_xpath('//*[@id="unitname"]').click()
	driver.find_element_by_xpath(u"//span[@value='台']").click()
	driver.find_element_by_name("unitnum[]").clear()
	driver.find_element_by_name("unitnum[]").send_keys("1")
	driver.find_element_by_name("unitprice[]").clear()
	driver.find_element_by_name("unitprice[]").send_keys("1")
	driver.find_element_by_name("unittotal").clear()
	driver.find_element_by_name("unittotal").send_keys("100")

	driver.find_element_by_link_text(u"已填好，我要发布").click()
	driver.quit()