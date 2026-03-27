import random
print("Welcome to the Coin Toss Game!")
print("""
Please choose one of the following options:
1. play with random.randint
2. play with random.random 
please enter (1 or 2):""")
choise = int(input())
if choise == 1:
  result = random.randint(0,1)
  if result == 0:
    result = "heads"
  else:
    result = "tails"
elif choise == 2:
  result = random.random()
  if result < 0.5:
    result = "heads"
  else:
    result = "tails"
else:
  print("Invalid input")
  exit()

your_choise = input("Enter heads or tails: ").lower()
if your_choise == result:
  print("You Win!")
elif your_choise != result and ( your_choise == "heads" or your_choise == "tails" ):
  print("You Lost!")
else:
  print("Invalid Input!")
  exit()

print(f"The computer choise is {result} ")
