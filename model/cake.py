
class Cake:
    #for entering and fetching every details
    def __init__(self,cakeid=0,cakename=None,cakeprice=None,cakeweight=None,cakecategory=None):
        self.cakeid=cakeid
        self.cakename=cakename
        self.cakeprice=cakeprice
        self.cakeweight=cakeweight
        self.cakecategory=cakecategory

    #for entering and fetching indiviual details
    def setCakeId(self,cakeid):
        self.cakeid=cakeid
    def getCakeId(self):
        return self.cakeid

    def setCakeName(self,cakename):
        self.cakename=cakename
    def getCakeName(self):
        return self.cakename

    def setCakePrice(self,cakeprice):
        self.cakeprice=cakeprice
    def getCakePrice(self):
        return self.cakeprice

    def setCakeWeight(self,cakeweight):
        self.cakeweight=cakeweight
    def getCakeWeight(self):
        return self.cakeweight

    def setCakeCategory(self,cakecategory):
        self.cakecategory=cakecategory

    def getCakeCategory(self):
        return self.cakecategory
    #string represntation of an object
    def __str__(self):
        return "Cake [cake id={} ,cakename ={}, cakeprice={} cakeweight ={} cakecategory={}]".format(self.cakeid,self.cakename,
                                                                                                     self.cakeprice,self.cakeweight,self.cakecategory)

