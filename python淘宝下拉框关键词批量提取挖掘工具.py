#淘宝下拉框关键词批量提取挖掘工具
#by 贺开宇|http://www.hekaiyu.com 转载注意版权
#更多SEO、SEO工具 http://www.hekaiyu.com/haoseo.html
#使用方法参考http://www.hekaiyu.com/seogongju/111.html
import urllib2,re
for key in open('111.txt'):
  do = "http://suggest.taobao.com/sug?code=utf-8&q=%s" % key.rstrip()
  _re = re.findall('\[\"(.*?)\",\".*?\"\]',urllib2.urlopen(do).read())
  for i in _re : print i.decode('utf-8').encode('gbk','ignore')
