class Cart:
    def __init__(self,cartid=0,cakeid=0,cakename=None,cakeprice=None,cakeweight=None,cakecategory=None,cemail=None):
        self.cartid=cartid;
        self.cakeid=cakeid
        self.cakename=cakename
        self.cakeprice=cakeprice
        self.cakeweight=cakeweight
        self.cakecategory=cakecategory
        self.cemail=cemail


    def setCartId(self,cartid):
        self.cartid=cartid

    def getCartId(self):
        return self.cartid

    def setCakeId(self, cakeid):
        self.cakeid = cakeid

    def getCakeId(self):
        return self.cakeid

    def setCakeName(self, cakename):
        self.cakename = cakename

    def getCakeName(self):
        return self.cakename

    def setCakePrice(self, cakeprice):
        self.cakeprice = cakeprice

    def getCakePrice(self):
        return self.cakeprice

    def setCakeWeight(self, cakeweight):
        self.cakeweight = cakeweight

    def getCakeWeight(self):
        return self.cakeweight

    def setCakeCategory(self, cakewcategory):
        self.cakewcategory = cakewcategory

    def getCakeCategory(self):
        return self.cakewcategory

    def setCemail(self, cemail):
        self.cemail = cemail

    def getCemail(self):
        return self.cemail

    def __str__(self):
        return "Cart[cartid={},cakename={},cakeprice={},cakeweight={},cakecategory={},email={}]".format(self.cartid,self.cakename,self.cakeprice,self.cakeweight,self.cakecategory,self.cemail)
