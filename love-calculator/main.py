name1=input("what is your name?")
name2=input("what is his/her name?")
combine_string=name1+name2
lower_case_str=combine_string.lower()
print(lower_case_str)
t=lower_case_str.count('t')
r=lower_case_str.count('r')
u=lower_case_str.count('u')
e=lower_case_str.count('e')
true=t+r+u+e
print(true)
l=lower_case_str.count('l')
o=lower_case_str.count('o')
v=lower_case_str.count('v')
e=lower_case_str.count('e')
love=l+o+v+e
print(love)

print(f"your love percentage is {true}{love}%")