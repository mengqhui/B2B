# -*-coding:utf-8-*-

import random
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC

#导入 WebDriverWait包
from  selenium.webdriver.support.ui import WebDriverWait
#导入 time 包
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8') # 设置编码

titiles=open(u'黄页88标题生成20151208_175612(1).txt','r').readlines()
keywords=open(u'keys.txt','r').readlines()

driver = webdriver.Ie()
#wait=WebDriverWait(webdriver.Ie(),30)
url="http://www.qinfawang.com/member/news.php?action=add"

def qinfafa():
	driver.get(url)
	time.sleep(3)
	#//*[@id="title"]<input name="post[title]" type="text" id="title" size="40" value="">
	driver.find_element_by_id("title").send_keys(unicode(random.choice(titiles)))
	
	#//*[@id="dform"]/table/tbody/tr[2]/td[2]/div/div[2]/iframe
	#<iframe class="ke-edit-iframe" hidefocus="true" frameborder="0" tabindex="" style="width: 100%; height: 261px;"></iframe>
	frame = driver.find_element_by_xpath('//*[@id="dform"]/table/tbody/tr[2]/td[2]/div/div[2]/iframe')
	driver.switch_to_frame(frame)

	fpath='a/'+str(random.randrange(1,200))+'.txt'
	contexts=open(fpath,'r').readlines()
	lili=""
	for context in contexts:
		lili=lili+context.strip('\n')+'<br>'
	#/html/body <body class="ke-content"></body>
	myinf="15110208454<br>18621631419<br>www.sonnenlicht029.com<br>www.upszhijia.com"
	js ='document.body.innerHTML="'+unicode(lili)+myinf+'"'
	print js
	driver.execute_script(js)
	
	driver.switch_to.default_content()
	
	#<input type="submit" name="submit" value=" 提 交 " class="btn_g">
	driver.find_element_by_xpath('//*[@value=" 提 交 "]').click()
	
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
	
	return
	
for i in range(5):
	print u'序号:',i
	qinfafa()
	
driver.close()