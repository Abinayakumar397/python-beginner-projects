import os
print("*******welcome to silent auction program*******")
def greatest_bid(bid_details):
  max=0
  winner=""
  for i in bid_details:  #{'jenny':90000,'shyam':98766,'abi':100000} 
     if max < bid_details[i] :
       max=bid_details[i]
       winner=i
  print(f"The winner is {winner} with a bid of {max}")
  

any_bidders=True

bidders_data={}


while any_bidders:
   name=input("what is your name?:")
   bid_amount=int(input("what is your bid?:"))
   bidders_data[name]=bid_amount
   bidders=input("Are they any bidders? Type 'yes' or 'no'")
   if bidders=="no":
    greatest_bid(bidders_data)
    any_bidders=False
   else:
    os.system("cls")
    any_bidders=True
