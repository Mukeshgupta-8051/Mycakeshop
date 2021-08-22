import pymysql

conn = pymysql.connect(host="localhost", user="root", password="atul123@", db="mycakeshop")
mycur=conn.cursor()
