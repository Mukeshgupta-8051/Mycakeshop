from model.cart import Cart
from views.cartview import CartView
class CartTemplate:
    def operation(self,choice):
        cartviewobj=CartView()
        if choice==1:
            print("==========Add to cart===========")
            cakeid=int(input("Enter cake id:"))
            cemail=input("Enter Customer email:")
            cartobj=Cart(cakeid=cakeid,cemail=cemail)
            result=cartviewobj.addToCart(cartobj)
            if result>0:
                print("added successfully")
            else:
                print("not addred in cart!! please try again")

        if choice==2:
            print("=======cartlist============")
            clist=cartviewobj.showCartList()
            print(type(clist))
            for cart in clist:
                print(cart)

        if choice==3:
            print("===========My Cart===========")
            cemail=input("Enter email:")
            clist = cartviewobj.showMyCart(cemail)
            if len(clist)>0:
                for cart in clist:
                     print(cart)
            else:
                print("Cart is not visible")


print("========Cart Operations==========")


print("---------------------------------")
print("1.Add to cart")
print("2.show cart list")
print("3.show my cart")
print("4.delete cart")
choice=int(input("Enter your choice:"))
carttemp=CartTemplate()
carttemp.operation(choice)