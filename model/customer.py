class Customer:
    # if we want to all values,use constructor __init__ method
    def __init__(self, cid=0, cname=None, cemail=None, ccontact=None, caddress=None, cpassword=None,
                 cconfirmpassword=None):
        self.cid = cid
        self.cname = cname
        self.cemail = cemail
        self.ccontact=ccontact
        self.caddress = caddress
        self.cpassword = cpassword
        self.cconfirmpassword = cconfirmpassword

    def setCustomerId(self, cid):
        self.cd = cid

    def getCustomerId(self):
        return self.cid

    def setCustomerName(self, cname):
        self.cname = cname

    def getCustomerName(self):
        return self.cname

    def setCustomerEmail(self, cemail):
        self.cemail = cemail

    def getCustomerEmail(self):
        return self.cemail

    def setCustomerAddress(self, caddress):
        self.caddress = caddress

    def getCustomerPassword(self):
        return self.cpassword

    def setCustomerConfirmPassword(self, cconfirmpassword):
        self.cconfirmpassword = cconfirmpassword

    def getCustomerConfirmPassword(self):
        return self.cconfirmpassword

        # if we want to display all values/string representation of database

    def __str__(self):
        return "customer id={},customer name={},customer email={},customer address={},customer password={},customer confirm password={}".format(self.cid,self.cname,self.ccontact,self.cemail,self.caddress,self.cpassword,self.cconfirmpassword)
