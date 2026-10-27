pizza=input("what type of pizza do you want(s/m/l:)")
cost=0
if pizza=="s" or pizza=="S" :
    cost+=100
   
elif pizza=="m" or pizza=="M" :
    cost+=200
    
else:
    cost+=300
   

pepporoni=input("do you want pepporoni")
if pepporoni=="yes":
        if pizza=="s" or pizza=="S":
         cost+=30
         print(f"you ordered {pizza} pizza with pepporoni and the pay is{cost}")
        else:
            cost+=50
            print(f"you ordered {pizza} pizza with pepporoni and the pay is{cost}")
        
        
else:
  print(f"you ordered {pizza} pizza the pay is{cost}")
extra_cheese=input("do you want extra cheese")
if extra_cheese=="yes":
    cost+=20
    print(f"your pay is {cost}")
else:
    print(f"your pay is {cost}")