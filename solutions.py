from customer import *
from coffee import *
from order import *

#instances of customers
cust1=Customer("Mike")
# cust1.name = "Robert"
cust2=Customer("mike")
cust3=Customer("juju")

# print(cust1.name)

# #instances of coffee
latte=Coffee("edy")
latte2=Coffee("edy")
# latte.name = "Capuchino"
print(latte.name)

# #instances of orders
Order1=Order(customer=cust1,coffee=latte,price=9.8)
# order2=Order(cust2,latte,7.8)
order3=Order(cust1, latte, 8)

# print(order3.price)

# print(latte.orders()) #a list of all orders of that coffee
# print(latte.customers())#returns a list of unique customers who ordered that coffee. 
# print(cust1.orders()) #list of all orders by a specific customer
# print(cust1.coffees())#a list of unique coffees ordered by a customer
# print(cust2.create_order(latte2,8.5)) #creates an order of latte2 for customer cust2
# print(cust2.create_order(latte,9.8))
# print(cust2.orders()) #confirm that cust2 now has an order
# print(cust1.coffees())
# print(latte2.num_orders())#num of times a coffee has been ordered
# print(latte2.average_price()) #average price of a coffee based on its orders
# print(Customer.most_aficionado(latte2)) #customer instance  that has spent most money on the coffee instance --None if no customer
