import requests

import re
from bs4 import BeautifulSoup
# html = requests.get(url='http://apis.juhe.cn/fapig/nba/query?key = ')
#
# print(html)
# print(html.text)
import pymysql

import requests
from prettytable import PrettyTable
\

import datetime
import json


def getMatch():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    today = datetime.datetime.now().strftime('%Y-%m-%d')  # 获得当天日期 如2018-10-26

    print(today)
    # 将上述中复制的url粘贴于此,需要做一些日期上的修改，如下把起止日期都改为今天
    url = "http://matchweb.sports.qq.com/kbs/list?from=NBA_PC&columnId=100000&startTime={0}&endTime={1}&callback=ajaxExec&_=1540442149442".format(
        today, today)  # http://nba.stats.qq.com/schedule/
    web_data = requests.get(url, headers=header)
    web_data.content.decode("utf-8")
    web_data = web_data.json()

    # print(web_data)
    data_nba =  web_data["data"]
    # print(web_data.content)
    # print(type(web_data.content))
    # datas = web_data.text[9:-1]
    # print(type(data_nba["2021-12-13"]))
    # print(data_nba["2021-12-13"])
    # print(len(data_nba["2021-12-13"]))
    # print(data_nb
    # return data_nba
    nba_list = []
    for data in  data_nba["%s"%(today)]:
        nba_list.append(data)
    return nba_list
    #     # print(data["matchDesc"],data["leftName"],data["leftGoal"],data["rightName"],data["rightGoal"])
    #     return data
    # # # print(datas)# dumps是将dict转化成str格式，loads是将str转化成dict格式。
    # # todaydata = datas['data'][today]
    # # print(todaydata)
    # # print(todaydata)
    # # pt = PrettyTable()
    # # pt._set_field_names(('leftEnName rightEnName leftGoal rightGoal quarter quarterTime startTime').split(' '))
    # # for one in todaydata:
    # #     # print(one)
    # #     rightEnName = one['rightEnName']  # rightName
    # #     leftEnName = one['leftEnName']  # leftName
    # #     leftGoal = one['leftGoal']
    # #     rightGoal = one['rightGoal']
    # #     starttime = one['startTime']  # 开始时间
    # #     quarter = one['quarter'][1:2]  # 第几节
    # #     quartertime = one['quarterTime']  # 每一节剩余时间
    # #     pt.add_row([leftEnName, rightEnName, leftGoal, rightGoal, quarter, quartertime, starttime])
    # # print(pt)
    #
    #
    # # db = pymysql.connect(user = 'root',
    # #                      password='wbf980728',
    # #                      database='wang',
    # #                      charset='utf8')#打开数据库连接
    # # cursor = db.cursor()#获取操作游标
    # # demo = cursor.execute('select * from students')#运行SOL语句
    # # lists = cursor.fetchall()#接收返回的结果
    # # # print(lists)
    # # for i in lists:
    # #     print(i)


# 主函数
if __name__ == "__main__":
    getMatch()
