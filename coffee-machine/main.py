resources={
       "Water":500,
       "Milk":1000,
       "Coffee":500,
      
   }
Money=0
latte={
        "Water":10,
        "Milk":20,
        "Coffee":20,
       
    }
espresso={
        "Water":10,
        "Milk":30,
        "Coffee":40,
       
}
cappucino={
        "Water":10,
        "Milk":20,
        "Coffee":50,
        
    }
Cost={
    "latte":150,
    "espresso":500,
    "cappucino":600
}
lack_quantity=""
def make_coffee(coffee_types):
    for i in resources:
        resources[i]-=coffee_types[i]
def current_resources_value():
    water=resources["Water"]
    milk=resources["Milk"]
    coffee=resources["Coffee"]
    print(f"Water={water}ml")
    print(f"Milk={milk}ml")
    print(f"Coffee={coffee}g")
    print(f"Money={Money}Rs")
   
def payment(coin_five,coin_ten,coin_twenty,type_coffee,recipe):
    total=coin_five*5+coin_ten*10+coin_twenty*20
    if Cost[type_coffee]==total or total>Cost[type_coffee]:
        if total>Cost[type_coffee]:
          change=total-Cost[type_coffee]
          print(f"Here is your Rs.{change} in change")
        global Money
        Money+=Cost[type_coffee]
        make_coffee(recipe)
        print(f"Here is your {type_coffee}")
    else:
        print(f"Sorry there is not enough Money.Money {total} refunded")
def check_sufficient_resources(recipe):
   for i in resources:
      
       if resources[i]<recipe[i]:
           global lack_quantity
           lack_quantity=i
           return False
   return True


off=True
while off:
    coffee_type=input("What would you like to have?(latte/espresso/cappucino):")
    if coffee_type=="off":
        off=False
    elif coffee_type=="report":
        current_resources_value()
    else:
        if coffee_type=="latte":
            recipe=latte
        elif coffee_type=="espresso":
            recipe=espresso
        else:
            recipe=cappucino
        available_or_not=check_sufficient_resources(recipe)
        if available_or_not:
            print("please insert your coins")
            five_rs=int(input("How many 5Rs coins:"))
            ten_rs=int(input("How many 10Rs coins:"))
            twenty_rs=int(input("How many 20Rs coins:"))
            payment(five_rs,ten_rs,twenty_rs,coffee_type,recipe)
        else:
            print(f"Sorry There is not enough {lack_quantity}.")