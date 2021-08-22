class Orders:
    def __init__(self,orderid=0,custemail=None,orderdate=None,totalprice=0,orderstatus=None,cake=None):
        self.orderid=orderid
        self.custemail=custemail
        self.orderdate=orderdate
        self.totalprice=totalprice
        self.orderstatus=orderstatus
        self.cake=cake

    def __str__(self):
        return "order[order id={},custemail={},orderdate={},totalprice={},orderstatus={},cake={}]".format(self.orderid,self.custemail,self.orderdate,self.totalprice,self.orderstatus,self.cake)
