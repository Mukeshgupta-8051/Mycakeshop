from views.orderview import OrderView
class OrderTemplate:
    def operations(self,choice):
        orderviewobj=OrderView()
        if choice==1:
            print("------place order-------")
            cemail=input("Enter email:")
            orderviewobj.placeOrder(cemail)

        if choice==2:
            print("-----my orders------")
            cemail = input("Enter email:")
            orderlist=orderviewobj.showMyOrder(cemail)
            for order in orderlist:
                print(order)



print("---------Orders--------")
print("------------------------")
print("1.place order")
print("2.show my orders")
print("3.show all orders")
choice=int(input("Enter your choice:"))
ordertemp=OrderTemplate()
ordertemp.operations(choice)