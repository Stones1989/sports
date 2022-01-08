import requests

import re
from bs4 import BeautifulSoup

html = requests.get(url='http://www.lszhibo8.com/')
html.encoding='GB2312'
soup = BeautifulSoup(html.text, 'lxml')  #以上是网络获取html
print(soup.prettify)
# print (soup.attrs) 
# print (soup)
# print (soup.a.attrs)
# print (type(soup.a.attrs))
# print (soup.b)
# print (soup.p)
# print(soup.prettify())  # 用标准html 显示方法打印html
# ret  = soup.find_all(id='category_2021-12-05')

ret_class= soup.find_all("div", class_="tit")

# for i in ret_class:
#     print(i)

print(ret_class[1].text.strip().split())
# a = ret_class[0].get("span")


# for  x  in ret_class:
# 	print(x.text)