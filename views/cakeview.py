import pymysql
from dbconnection.dbconnect import *
from model.cake import Cake
#this class is going to connect with db
class CakeView:
    def addCake(self,cake):
        #conn=pymysql.connect(host="localhost",user="root",password="root",db="mycakeshop")
        #cursor=conn.cursor()
        try:
            sql = "insert into cake(cakename,cakeprice,cakeweight,cakecategory)values('{}',{},{},'{}')".format(
                cake.getCakeName(), cake.getCakePrice(), cake.getCakeWeight(), cake.getCakeCategory())
            i = mycur.execute(sql)
            conn.commit()
            return i

        except Exception as e:
            print('Error is ', e)



    def updateCake(self,cake):
        try:
            sql="update cake set cakename='{}',cakeprice={},cakeweight={},cakecategory='{}' where cakeid={}".format(cake.getCakeName(),cake.getCakePrice(),cake.getCakeWeight(),cake.getCakeCategory(),cake.getCakeId())
            print(sql)
            i=mycur.execute(sql)
            conn.commit()
            return i
        except Exception as e:
            print(e)

    def deleteCake(self,cakeid):
        try:
            sql="delete from cake where cakeid={}".format(cakeid)
            print(sql)
            i=mycur.execute(sql)
            conn.commit()
            return i

        except Exception as e:
            print(e)

    def showCakeList(self):
        try:
            cakelist=[]
            sql="select *from cake"
            noofrows=mycur.execute(sql)
            print(noofrows)
            data=mycur.fetchall()
            for row in data:
                cakeobj=Cake(cakeid=row[0],cakename=row[1],cakeprice=row[2],cakeweight=row[3],cakecategory=row[4])
                cakelist.append(cakeobj)
            return cakelist

        except Exception as e:
            print('Error is ', e)



    def searchCakeById(self,cakeid):
        try:

            sql = "select *from cake where cakeid={}".format(cakeid)
            noofrows = mycur.execute(sql)
            print(noofrows)
            data = mycur.fetchone()

            return data

        except Exception as e:
            print('Error is ', e)

    def searchCakeByName(self,cakename):
        try:
            cakelist = []
            sql = "select *from cake where cakename='{}'".format(cakename)
            noofrows = mycur.execute(sql)
            print(noofrows)
            data = mycur.fetchall()
            for row in data:
                cakeobj = Cake(cakeid=row[0], cakename=row[1], cakeprice=row[2], cakeweight=row[3], cakecategory=row[4])
                cakelist.append(cakeobj)
            return cakelist

        except Exception as e:
            print('Error is ', e)

    def searchCakeByCategory(self,cakecategory):
        try:
            cakelist = []
            sql = "select *from cake where cakecategory='{}'".format(cakecategory)
            noofrows = mycur.execute(sql)
            print(noofrows)
            data = mycur.fetchall()
            for row in data:
                cakeobj = Cake(cakeid=row[0], cakename=row[1], cakeprice=row[2], cakeweight=row[3], cakecategory=row[4])
                cakelist.append(cakeobj)
            return cakelist

        except Exception as e:
            print('Error is ', e)