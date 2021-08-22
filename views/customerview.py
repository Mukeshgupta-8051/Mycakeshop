from dbconnection.dbconnect import *
class CustomerView:
    def addCustomer(self,customer):
        try:
            sql = "insert into customer(cname,cemail,ccontact,caddress,cpassword,cconfirmpassword)values('{}','{}',{},'{}','{}','{}')".format(
                customer.getCustomerName(), customer.getCustomerEmail(), customer.getCustomerContact(),
                customer.getCustomerAddress(), customer.getCustomerPassword(),
                customer.getCustomerConfirmPassword())
            i = mycur.execute(sql)
            conn.commit()
            return i



        except Exception as e:
            print('Error is ', e)


    def updateCustomer(self,customer):
        pass

    def deleteCustomer(self,custid):
        pass

    def showCustomerList(self):
        pass

    def searchCustomerById(self,custid):
        pass

    def searchCustomerByEmail(self,custemail):
        pass