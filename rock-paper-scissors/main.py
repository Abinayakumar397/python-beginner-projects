import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""


print("   welcome!!let's play rock paper scissors!!!  ")
user_choice=int(input("it's ur turn! enter your choice(0=rock,1=paper,2=scissor):"))
computer_choice=random.randint(0,2)

if (user_choice==0 and computer_choice==0) or (user_choice==1 and computer_choice==1) or (user_choice==2 and computer_choice==2):
    print("the match is draw")
elif user_choice==0 and computer_choice==1:
    print(rock)
    print(paper)
    print("computer wins!!")
elif user_choice==0 and computer_choice==2:
     print(rock)
     print(scissor)
     print("you win!!")
elif user_choice==1 and computer_choice==0:
     print(paper)
     print(rock)
     print("you win!!")
elif user_choice==1 and computer_choice==2:
    print(paper)
    print(scissor)
    print("computer wins!!")
elif user_choice==2 and computer_choice==0:
    print(scissor)
    print(rock)
    print("computer wins!!")
else:
    print(scissor)
    print(paper)
    print("you win!!")
