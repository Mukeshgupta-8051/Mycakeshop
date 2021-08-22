import datetime
from dbconnection.dbconnect import *
from model.order import Orders
class OrderView:
    def placeOrder(self,cemail):
        try:
            sql1="select sum(cakeprice) from cake inner join cart on cake.cakeid=cart.cakeid where cemail='{}'".format(cemail)
            i=mycur.execute(sql1)
            data=mycur.fetchone()
            totalprice=data[0]
            print("total price ",totalprice)
            orderdate=datetime.date.today()
            print("date:",orderdate)
            sql2="insert into orders(ordertotal,orderdate,cemail)values({},'{}','{}')".format(totalprice,orderdate,cemail)
            i=mycur.execute(sql2)
            conn.commit()
            if i>0:
                print("order placed")
                sqlquery3 = "select *from orders where cemail='{}' and orderdate='{}'".format(cemail,orderdate)
                i=mycur.execute(sqlquery3)
                row=mycur.fetchone()
                orderobj = Orders(row[0], row[1], row[2], row[3], row[4])
                print(orderobj)
        except Exception as e:
            print(e)

    def showMyOrder(self,cemail):
        try:
            orderlist = []
            sqlquery3 = "select *from orders where cemail='{}'".format(cemail)
            i = mycur.execute(sqlquery3)

            if i > 0:
                data = mycur.fetchall()
                for row in data:
                    orderob = Orders(row[0], row[1], row[2], row[3], row[4])
                    orderlist.append(orderob)
                return orderlist
        except Exception as e:
            print(e)


    def showAllOrders(self):
        pass