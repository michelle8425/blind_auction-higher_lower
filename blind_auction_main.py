#from replit import clear

from art import logo

print(logo)

bids = {}
bidy = True

def max_bid(bidding_record):
  highest_amt = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_amt:
      highest_amt = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_amt}")


while bidy is not False:
  name = input("What is your name? ")
  bid = int(input("How much would you like to bid? $ "))
  bids[name] = bid
  again= input ("Do we have another bidder? ")
  if again == "yes":
    clear()
  elif again == "no":
    bidy = False
    print(bids)
    max_bid(bids)