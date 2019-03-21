from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import json
import pymysql
import time
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)








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
        sql = "UPDATE auth_users SET status =%s WHERE user = '%s' " % (1, user)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()
        except Exception as e:
            print(e)
            self.db.rollback()
            self.db.close()

def index(request):
    return HttpResponse("success!!")

def html(request):
    return render(request, 'demo.html')



def demo(request):
    db = mysql()
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        print(username, password)
        result = ''
        print(db.check_users(username, password))
        result = str(db.check_users(username, password))
        if result == '()':
            web = 'http://127.0.0.1:8000/blog/html'
        else:
            db.login_success(username)
            web = 'http://127.0.0.1:8000/blog/index'
    return HttpResponse(json.dumps(web , ensure_ascii=False, cls=DateEncoder), content_type="application/json")
    # return HttpResponse("success!!")
