import random
import os
score=0
correct=True
logo = """
  ╔════════════════════╗
  ║  HIGHER  OR LOWER  ║
  ╚════════════════════╝
  """
vs = """
  ╔═══╗
  ║VS!║
  ╚═══╝
  """
db=[
    "Narenda modi,a pm",
   "Nasa,a space agency",
   "T-series,a music label",
    "virat kholi,a cricketer"
      
 ]
while correct:
  
  print(logo)
  
  compare_1=random.choice(db)
  
  compare_2=random.choice(db)

  while compare_1==compare_2:  #to avoid duplicates
     compare_2=random.choice(db)
  print(compare_1)
  print(vs)
  print(compare_2)
  choice=input("Who has more followers? Type '1' or '2':")
  index1=db.index(compare_1)
 
  index2=db.index(compare_2)
  if index1>index2 and choice=='1':
   
     score+=1
     print(f"you are right.your score is {score}")
  elif index2>index1 and choice=='2':
     
     score+=1
     print(f"you are right.your score is {score}")
  else:
     os.system('cls')
     print(logo)
     print(f"your are wrong...your final score is {score}")
     correct=False