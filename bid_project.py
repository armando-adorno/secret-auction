import art
import os

print(art.logo)

bider_name = [input("Name: ")] # Ask for Name Input
bid_price = [int(input("Price: "))] # Ask for Bid Price

bid_log = { # Add Name and Bid into a dictionary as the key and value.
           
           "name": bider_name,
           "price": bid_price
}

more_bids = input("Anyone else want to bid? Type 'Yes' or 'No' ").lower()

if(more_bids == "yes"):
    bids = True
elif(more_bids == "no"):
    bids = False
    
while(bids == True):
  
    # TODO Need To Clear the Terminal for each Bider Input
    os.system('cls')
    
    bider_name.append(input("Name: "))
    bid_price.append(int(input("Price: ")))
  
    more_bids = input("Anyone else want to bid? Type 'Yes' or 'No' ").lower()
    
    if(more_bids == "yes"):
      bids = True
    else:
      bids = False
      break
    
# TODO Find the Highest Bid & Declares The Bider as the Winner
 
max_price = max(bid_price) # Stores the Maximum Price Made

#* Line 41 - 42 is for practice with dict variables.
bider_max = bid_log["price"][bid_price.index(max_price)]
bider_name = bid_log["name"][bid_price.index(max_price)]

print(f"The winner is {bider_name} with a price of ${bider_max}")