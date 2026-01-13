first_name="Jaspinder"
middle_name="Kaur"

print(f'Name:{first_name} {middle_name}')

my_cart = [ 
{"name": "Laptop", "price": 40000, "qty": 1}, 
{"name": "Mouse", "price": 500, "qty": 2},
{"name": "HDMI Cable", "price": 200, "qty": 3} 
] 

total=0

for items in my_cart:
    total=items["price"]*items["qty"]+total
    
print("Total:",total)

user_coupon = "VIDYA20"



if user_coupon:
    discount=total*0.20
    newprice=total-discount
    print("newprice",newprice)
    total_price=0.18*newprice
    print("TotalPrice:",total_price)
    precalculate=total_price+newprice
    print("TotalCalculate:",precalculate)

if total_price<500:
    final_price=total_price+50
    print("Price:",final_price)


