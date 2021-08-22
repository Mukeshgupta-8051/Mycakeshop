from model.cake import Cake
from views.cakeview import CakeView
class CakeTemplate:

    def operations(self,choice):
        cakeviewobj = CakeView()
        if choice==1:
            print("------Add Cake------")
            #taking all deatils of cake
            cname=input("Enter cake name:")
            cprice=input("Enter cake price:")
            cweight=input("Enter cake weight:")
            ccate=input("Enter cake category:")
            #storing all cake details in cakeobj
            cakeobj=Cake(cakename=cname,cakeprice=cprice,cakeweight=cweight,cakecategory=ccate)
            print(cakeobj)
            #calling addCake() from cakeview for storing cake details in database
            result =cakeviewobj.addCake(cakeobj)
            if result>0:
                print("record inserted")
            else:
                print("record not inserted")


print("===========Cake Operations===========")
print("-------------------------------------")
print("1.Add Cake")
print("2.Update Cake")
print("3.Delete Cake")
print("4,ShowCakeList")
print("5.Search Cake by Id")
print("6.Search Cake by Name")
print("7.Search Cake By Category")
choice=int(input("Enter choice:"))
caketempobj=CakeTemplate()
caketempobj.operations(choice)