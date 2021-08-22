from dbconnection.dbconnect import *
from model.cart import Cart
class CartView:
    def addToCart(self,cart):
        try:
            sql="insert into cart(cakeid,cemail)values({},'{}')".format(cart.getCakeId(),cart.getCemail())
            i=mycur.execute(sql)
            conn.commit()
            return i
        except Exception as e:
            print(e)

    def showCartList(self):
        try:
            cartlist=[]
            sql="select cartid,cake.cakeid,cakename,cakeprice,cakeweight,cakecategory,cemail from cart inner join cake " \
                "on cart.cakeid=cake.cakeid"
            i=mycur.execute(sql)
            data=mycur.fetchall()
            for row in data:
                cartobj=Cart(cartid=row[0],cakeid=row[1],cakename=row[2],cakeprice=row[3],cakeweight=row[4],cakecategory=row[5],cemail=row[6])
                cartlist.append(cartobj)
            return cartlist
        except Exception as e:
            print(e)

    def showMyCart(self,cemail):
        try:
            cartlist = []
            sql = "select cartid,cake.cakeid,cakename,cakeprice,cakeweight,cakecategory,cemail from cart inner join " \
                  "cake on cart.cakeid=cake.cakeid where cemail='{}'".format(cemail)
            i = mycur.execute(sql)
            data = mycur.fetchall()
            for row in data:
                cartobj = Cart(cartid=row[0], cakeid=row[1], cakename=row[2], cakeprice=row[3], cakeweight=row[4],
                               cakecategory=row[5], cemail=row[6])
                cartlist.append(cartobj)
            return cartlist
        except Exception as e:
            print(e)

    def deleteFromCart(self,cartid):
        pass