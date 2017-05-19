#coding:utf-8

import random

file1=u"电池word.txt"
file2=u"电池淘宝.txt"
fo1 =open(file1,'r')
fo2 =open(file1,'r')
li=fo1.readlines()

li2=fo2.readlines()
li.extend(li2)

for inin in range(200):
	line=''
	while 1:
		line=line + random.choice(li)
		lenn =len(line)
		if lenn>=5000:
			break
	print(inin)
	fio=open(str(inin)+'.txt','w')
	fio.write(line)
	fio.close()
