import random
print("welcome to the password generator!")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['@','!','#','$','%','^','&','*','(',')','~','?']

l_count=int(input("how many letters would you like in password?"))
s_count=int(input("how many symbols would you like in password?"))
n_count=int(input("how many numbers would you like in password?"))
i=1
l1=""
while i<=l_count:
    l2=random.choice(letters)
    l1+=l2
    i+=1


j=1
while j<=s_count:
    l2=random.choice(symbols)
    l1+=l2
    j+=1


z=1
while z<=n_count:
    l2=random.choice(numbers)
    l1+=str(l2)
    z+=1

l3=[]
for i in l1:
    l3.append(i)
random.shuffle(l3)

password=""
for i in l3:
    password+=i
print( "password created ",password)