# -*- coding: UTF-8 -*-
import pymysql
import time
import datetime

# db = pymysql.connect('localhost', 'root', 'savicsw,./', 'tsp', charset='utf8')
#
# cursor = db.cursor()
#
# sql = "SELECT * FROM location \
#        WHERE ID = 100"
#
#
# try:
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for row in result:
#         print('ID=', row[0], 'lat=', row[1], 'lng=', row[2])
#
# except:
#     print("Error: unable to fecth data")

class mysql(object):
    def __init__(self):
        self.config = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': '0000', 'db': 'tsp',  'charset':'utf8mb4'}
        self.db = pymysql.connect(**self.config, cursorclass = pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()
        self.db.close()

    def connect(self):
        self.db = pymysql.connect(**self.config, cursorclass = pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def check_users(self, user, password):
        self.connect()
        sql = "SELECT * FROM auth_users WHERE user= '%s' AND password= '%s'" % (user, password)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.db.close()
            return result
        except Exception as e:
            print(e)
            self.db.rollback()
            self.db.close()

    def login_success(self, user):
        self.connect()
        sql = "UPDATE auth_users SET status =%s WHERE user = '%s' " % (1,user)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()
        except Exception as e:
            print(e)
            self.db.rollback()
            self.db.close()
# dict = {'OrderId': 4457220510, 'UserName': '刘伊婷', 'UserPhone': '22217413,6695', 'CardNo': '', 'LocationName': '成都', 'LocationDetail': '马家花园路11号成都宽窄巷子希尔顿欢朋酒店', 'GetTime': '2018-12-21 14:23:00', 'Lat': 30.687349, 'Lng': 104.05939, 'GetTransferTid': '退房行李放置前台即可离店', 'DestinationDetail': '双流机场T2航站楼', 'TakeTime': '2018-12-21 18:30:00', 'ToLat': 30.575265, 'ToLng': 103.961569, 'TakeTransferTid': '行李员当面交付(出发层9号门)', 'BookingPhotos': None, 'OrderState': 5, 'Remark': '', 'FlightNumber': 'CA4417', 'CreateTime': '2018-12-21 14:22:58', 'BagCount': 2, 'CourierName': '伍贞勇', 'CourierPhone': '15982234919', 'DataChange_LastTime': '2018-12-21 19:56:08'}
# test = mysql()
# test.findlocID()
# test.findloc(30.678505002775, 104.07510771834)
# test.searchDuratin()
# test.insertOrder(dict)
# test.db.close()
# res = test.findOrderByID(4457218317)
# print(res)
# time = res[0]['GetTime']
# print(type(time), time)
# print(time)
# result = test.findOrderByDay('2018-12-21', '2018-12-22')
# for order in result:
#     print(order)
# test.insertDuration(101, 101, 1)
# test.insertRoute('asfawga')
# db = mysql()
# day = datetime.datetime.strptime(datetime.date.today().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
# route = db.findRouteByDay(day)
# route = str(route).split(',')
# print('route=', len(route))
# list = []
# for order_ID in route:
#     list.append(db.findOrderByID(order_ID))
# print('list = ', len(list))

# test = mysql()
# print("ok")
# print(test.check_users('wenjie', '0000'))
# print('ok')

#
# test = mysql()
# test.login_success("wenjie")