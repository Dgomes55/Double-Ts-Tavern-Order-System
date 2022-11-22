"""
Created on Thu Nov 17 11:25am 2022

@authors: Dylan Gomes & Jensen Packard
"""
# Initalize Variables
menu_items = ['Classic','Bacon Cheese Burger','Double Ts Burger','Steak Tip Sandwich','Double Ts Fried Chicken Sandwhich','Jordan Chicken Sandwich','Ultimate Chicken Sandwich','Sausage Peppers + Onion Sandwhich','TTs Famous Steak Tips','TTs Famous Chicken Kebab','Grilled Italian Hot Sausage','Souvlaki','Double TS Baked Haddock','Double TS Combo','Armenian Platter','Clam Chowder','Chicken Wings','Fried Pickles','Fried Zucchini','Hummus Platter','Marlborough Putine','Double Ts Coconut Chicken Tenders','Fried Pepperoni','Fried Ravioli','House Salad','Classic Caesar','BLT Wedge','Fries','Salad','Rice Pilaf','Green Beans']


# Application Design
print("#"*30+"\n    Welcome to Double Ts Tavern\n"+"#"*30+ \
"\nPlease Chose your Order:")
# Declare Variables
menu_prices = {"Classic":11.00,
"Bacon Cheese Burger":13.00,
"Double Ts Burger":18.00,
"Steak Tip Sandwich":14.00,
"Double Ts Fried Chicken Sandwhich":13.00,
"Jordan Chicken Sandwich":15.00,
"Ultimate Chicken Sandwich":17.00,
"Sausage Peppers + Onion Sandwhich":12.00,
"TTs Famous Steak Tips":21.95,
"TTs Famous Chicken Kebab":17.95,
"Grilled Italian Hot Sausage":17.95,
"Souvlaki":18.95,
"Double TS Baked Haddock":18.95,
"Double TS Combo":24.95,
"Armenian Platter":18.95,
"Clam Chowder":7.50,
"Chicken Wings":11.00,
"Fried Pickles":8.00,
"Fried Zucchini":11.00,
"Hummus Platter":11.00,
"Marlborough Putine":9.00,
"Double Ts Coconut Chicken Tenders":12.00,
"Fried Pepperoni":7.99,
"Fried Ravioli":8.99,
"House Salad":9.50,
"Classic Caesar":9.00,
"BLT Wedge":10.00,
"Fries":7.00,
"Salad":6.00,
"Rice Pilaf":6.00,
"Green Beans":7.00}
# Show all menu items
for item,price in menu_prices.items():
        print(str(menu_items.index(item))+': ' + item.title()+" - Price: $"+str(price))
print('#'*30)

# Add items
x = True
total_price = 0 # total price
orders = [] # store selected items 
while x:
    order = input("Enter Item Name or Number, If multiple; followed by the quantity separated by a comma:")
    print("To finish your order type 'done', to view current order type 'show'")

    ord_split = order.split(',')
    

    if ord_split[0].isnumeric():
        items = menu_items[int(ord_split[0])]
    else:
        items = order
    
    x = items
    if x == 'done':
        x = False
    elif x == 'show':
        print('current order:',orders)
    elif len(ord_split) > 1:
        quantity = int(ord_split[1])
        print(quantity)
        for i in range(quantity):
            orders.append(items)
            total_price +=(menu_prices[items])
        
    else:
        total_price += (menu_prices[items])
        orders.append(items)
        print(items, 'added')
print('#'*30)

state_tax = 1.0625

# Final Total
print("Items in your cart: ")
for i in range(len(orders)):
    print(str(i+1)+" - "+orders[i].title() +" - $"+str(menu_prices[orders[i]]))
print("Your Total Price: "+'$'+str(total_price*state_tax))
#End
print('#'*30+"\nThanks! Order Again.\n")
