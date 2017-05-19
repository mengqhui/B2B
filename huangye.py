# -*-coding:utf-8-*-

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, codecs

#导入 WebDriverWait包
from  selenium.webdriver.support.ui import WebDriverWait

'''
import sys
reload(sys)
sys.setdefaultencoding('utf8') # 设置编码
'''
titiles=open(u'黄页88标题生成20151208_175612(1).txt','r').readlines()
keywords=open(u'keys.txt','r').readlines()
myinfo='''15110208454
18621631419
www.sonnenlicht029.com/
www.upszhijia.com/
'''
##############
'''
cookie={
	"__cfduid":"dd5021492a60d52a3d6815da94616f24b1489735490",
	"_ga":"GA1.2.1951789113.1489735501",
	"_gat":"1",
	"gr_session_id_aa3229224cce7805":"e7b8a7d8-fa9a-401e-b02c-cb5e0d53406f",
	"gr_user_id":"38be0737-34fc-487f-bdfd-7f429f8552fe",
	"hy88loginid":"1629897",
	"hy88realname":"%E8%B5%B5%E7%9B%9B",
	"hy88usergroup":"11",
	"hy88username":"sonnen",
	"hy_itemproductnames":"%E5%BE%B7%E5%9B%BD%E9%98%B3%E5%85%89%E8%93%84%E7%94%B5%E6%B1%A0%E5%AF%B9%E6%AF%94%2C%E5%BE%B7%E5%9B%BD%E9%98%B3%E5%85%8960%E8%93%84%E7%94%B5%E6%B1%A0%2C%E8%BF%9B%E5%8F%A3%E5%BE%B7%E5%9B%BD%E9%98%B3%E5%85%89%E8%93%84%E7%94%B5%E6%B1%A0",
	"hy_itemsubjects":"%E5%8C%97%E4%BA%AC%E9%94%80%E5%94%AE%E9%98%B3%E5%85%89%E8%93%84%E7%94%B5%E6%B1%A0A512%2F2S%E4%BC%98%E8%B4%A8%E6%9C%8D%E5%8A%A1",
	"pgv_pvi":"9402268672",
	}

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER "
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)
'''
driver = webdriver.Ie()
huangye="http://fabuxinxi.huangye88.com/"

def huangye88():
	#time.sleep(2)
	try:driver.find_element_by_xpath('//*[@id="recoveryModal"]/div[3]/button[2]').click()
	except:print 'onclick!'
	finally:
		driver.find_element_by_xpath('//*[@id="subject"]').send_keys(unicode(random.choice(titiles)))
		#<textarea type="text" id="content" name="info[content]" rows="15" class="span7 mt5"></textarea>
		driver.find_element_by_xpath('//*[@id="content"]').send_keys(context)
		print('//*[@id="content"]context')
		driver.find_element_by_xpath('//*[@id="content"]').send_keys(myinfo)
		print('//*[@id="content"]myinfo')
		for ii in range(3):
			#关键词<input class="input-small ml5" type="text" alt="关键字:长度@4-20/特殊字符/开头" onkeydown="keydownaddtag(event)">
			driver.find_element_by_xpath('//*[@alt="关键字:长度@4-20/特殊字符/开头"]').send_keys(unicode(random.choice(keywords)))
			#<a class="btn" type="button" id="addkey">点击增加新关键词</a>
			driver.find_element_by_link_text('点击增加新关键词').click()
			ii=ii+1
	
		#<input style="width:100px" id="productname0" name="info[productname][]" value="" autocomplete="off" type="text" alt="商品别名:空/长度@4-20/怪异字符">
		driver.find_element_by_xpath('//*[@id="productname0"]').send_keys(unicode(random.choice(keywords)))
		driver.find_element_by_xpath('//*[@id="productname1"]').send_keys(unicode(random.choice(keywords)))
		driver.find_element_by_xpath('//*[@id="productname2"]').send_keys(unicode(random.choice(keywords)))
		#<input placeholder="请选择" class="span2 suggest" type="text" name="unitname" id="unitname" value="" onfocus="showUnit(this)" readonly="">
		#//*[@id="postform"]/div[12]/div[1]/div/div/button/span
		##postform > div:nth-child(17) > div:nth-child(1) > div > div > div > ul > li.none > span:nth-child(24)
		# 去掉元素的readonly属性
		js = 'document.getElementById("unitname").removeAttribute("readonly");'
		driver.execute_script(js)
		# 清空文本后输入值
		driver.find_element_by_id("unitname").clear()
		driver.find_element_by_id("unitname").send_keys(u"台")
		'''
		driver.find_element_by_xpath('//*[@id="unitname"]').click()
		#<span class="item-span" value="台">台</span>
		driver.find_element_by_xpath('//*[@value="台"]').click()
		#<a style="position: absolute;right:15px" onclick="$('.all-unit').hide()">X</a>
		driver.find_element_by_xpath('//*[@id="postform"]/div[12]/div[1]/div/div/div/ul/li[5]/a').click()
		'''
		driver.find_element_by_xpath('//*[@id="unitTable"]/tbody/tr[1]/td[1]/input').send_keys(1)
		#购买数量<input class="numb" type="text" name="unitnum[]" onblur="checkUnit(this)" value="" style="border: 1px solid rgb(70, 136, 71); border-radius: 4px;">
		driver.find_element_by_xpath('//*[@id="unitTable"]/tbody/tr[1]/td[2]/input').send_keys(1)
		#产品单价<input class="numb" type="text" name="unitprice[]" onblur="checkUnit(this)" value="" style="border: 1px solid rgb(70, 136, 71); border-radius: 4px;">
		driver.find_element_by_xpath('//*[@alt="供货总量:价格"]').send_keys(100)
		#供货总量<input id="4" name="unittotal" type="text" alt="供货总量:价格" value="">
		#//*[@id="postform"]/p[1]/a <a class="btn btn-large btn-warning" onclick="JavaScript:go();">已填好，我要发布</a>
		driver.find_element_by_partial_link_text("我要发布").click()
		time.sleep(1)
	return

for i in range(25):
	print u'序号:',i
	driver.implicitly_wait(30)
	fpath='a/'+str(random.randrange(1,200))+'.txt'
	context=open(fpath,'r').readlines()
	#driver.add_cookie(cookie)
	driver.get(huangye)
	huangye88()
	
driver.close()

