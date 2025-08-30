menu = {
    'pizza':40,
    'coffe':80,
    'paneer':90,
    'barger':80,
}

# greet
print("wwlcome to our resturnt :")
print("pizza:40 \ncoffe:80 \npaneer:90 \nbarger:80")


order_total = 0  

item_1=input("enter the name of item you want oder = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} is added")

else:
    print(f"this item {item_1} not avaiable yet!")

another_order = input("Do you want order a another item ? (yes/no)")

if another_order == "yes":
    
    item_2= input("enter the second item = ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"your order added {item_2}")
    else:
        print(f"order item {item_2} is not avaialbe !")


print(f"the order the item is pay {order_total}")






