from views.customerview import *
from model.customer import *
class CustomerTemplate:
    def operations(self,choice):
        customerviewobj=CustomerView()
        if choice==1:
            pass


print("============Customer==============")
print("1.Add Customer")
print("2.Update Customer")
print("3.Delete Customer")
print("4.Show Customer")
print("5.Search customer by id")
print("6.search customer by email")
choice=int(input("Enter choice:"))
custtemp=CustomerTemplate()
custtemp.operations(choice)