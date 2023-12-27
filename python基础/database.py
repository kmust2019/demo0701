import pymysql
import random


# 打开数据库连接
db = pymysql.connect(host='192.168.0.111',
                         user='root',
                         password='123456',
                         database='ucrs_stg1')

def get_city_invest_customer_info():
    cursor = db.cursor()
    # query_string ="SELECT customer_nm,cert_no,area_code from  ucrs_city_invest_info ORDER BY RAND() LIMIT 10"
    begin = random.randint(100, 980)
    query_string = "SELECT customer_nm,cert_no,area_code from  ucrs_city_invest_info LIMIT " + str(begin) + ',10'
    cursor.execute(query_string)
    customer_info_list = cursor.fetchall()
    return customer_info_list
