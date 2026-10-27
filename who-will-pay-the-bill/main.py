import random
l1=input("enter everybody's name seperated by comma:").split(',')
print(l1)
length=len(l1)
who_pay=random.randint(0,length-1)
print(f"{l1[who_pay]} will pay the bill")
