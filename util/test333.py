import urllib.request
import json
#json文件的URL地址
url="https://matchweb.sports.qq.com/kbs/list?from=NBA_PC&columnId=100000&startTime=2020-03-11&endTime=2020-03-31&from=sporthp&callback=ajaxExec&_=1583909839470"
#补充请求头信息
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Referer': 'https://nba.stats.qq.com/schedule/'
    }
#获取数据
req=urllib.request.Request(url=url,headers=headers)
text=urllib.request.urlopen(req).read().decode('gbk')
#去文件开头的无用子串“ajaxExec”
text=text.strip("ajaxExec")
#去掉文件头尾的小括号
text=text[1:len(text)-1]
#加载为Python对象dic
content=json.loads(text)
#取出当前日期
date=list(content['data'].keys())[0]
print(date)
#输出当日所有比赛的比分
for i in content['data'][date]:
    print(i['leftName'],end='')
    print(" ",end='')
    print(i['leftGoal'],end='')
    print(":",end='')
    print(i['rightGoal'],end='')
    print(" ",end='')
    print(i['rightName'])