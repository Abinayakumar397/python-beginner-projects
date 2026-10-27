import random
play_again=True
while play_again:
 print("********Welcome to the number guessing game*********")
 print("I'm thinking of a number between 1 and 100.")
 number=random.randint(1,100)
 print("Choose a difficulty:\n1.Easy (10 attempts)\n2.Hard (5 attempts)")
 choice=int(input("Enter your choice:"))
 attempts_for_easy=10
 attempts_for_hard=5

 if choice==1:
  attempts+=1
  print(f"you have {attempts_for_easy}remaining.")
  while attempts_for_easy!=0:
  
   guess=int(input("Make a guess:"))
   if guess>number:
     print("Too high!")
     attempts_for_easy-=1
     print(f"you have {attempts_for_easy}remaining.")
     attempts+=1
   elif guess<number:
     print("Too low!")
     attempts_for_easy-=1
     print(f"you have {attempts_for_easy}remaining.")
     attempts+=1
   else:
     print(f"Congratulations!\nYou guessed the correct number: {number}")
     print(f"You took {attempts} attempts.")
     attempts_for_easy=0
  
  again=input("Do you want to play again? (y/n):")
  if again=='y':
    play_again=True
  else:
    play_again=False

 else:
   attempts=0
   print(f"you have {attempts_for_hard}remaining.")
   while attempts_for_hard!=0:
    
    
    guess=int(input("Make a guess:"))
    if guess>number:
     print("Too high!")
     attempts_for_hard-=1
     print(f"you have {attempts_for_hard}remaining.")
     attempts+=1
    elif guess<number:
     print("Too low!")
     attempts_for_hard-=1
     print(f"you have {attempts_for_hard}remaining.")
     attempts+=1
    elif guess==number:
     print(f"Congratulations!\nYou guessed the correct number: {number}")
     print(f"You took {attempts} attempts.")
     attempts_for_hard=0
    
 
   again=input("Do you want to play again? (y/n):")
   if again=='y':
    play_again=True
   else:
    play_again=False

  