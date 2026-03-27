print("Welcome to the rock, paper, sicssors game!")
rock = "🤜"
paper = "✋"
scissors = "✌️"
# طلب التعليمات أم لا
ent = input(
    "Please if u need any help u can write (Help) or press enter to continue:\n"
).lower()
if ent == "help":
    print("""
     *********** RULES ***********
     1) You choose and the computer chooses
     2) Rock smashes Scissors -> Rock wins
     3) Scissors cut Paper -> Scissors win
     4) Paper covers Rock -> Paper wins
     """)

# حصر الاختيارات وطباعة اختيار المسخدم
choice = input("choose one of rock, paper, sicssors to start playing:\n").lower()
if choice not in (["rock", "paper", "scissors"]):
    print("invaild input, try the game again")
    exit()
else:
    if choice == "rock":
        print(f"You choose {rock}")
    elif choice == "paper":
        print(f"You choose {paper}")
    else:
        print(f"You choose {scissors}")
# طباعة جواب الحاسوب
import random

com_choice = random.choice(["rock", "paper", "scissors"])
if com_choice == "rock":
    print(f"the computer choose {rock}")
elif com_choice == "paper":
    print(f"the computer choose {paper}")
else:
    print(f"the computer choose {scissors}")

# الخوارزميات
if com_choice == choice:
    print("Its a tie!")
elif (
    (choice == "rock" and com_choice == "scissors")
    or (choice == "paper" and com_choice == "rock")
    or (choice == "scissors" and com_choice == "paper")
):
    print(f"You Won!, {choice} beats {com_choice}")
else:
    print(f"You Lost!, {com_choice} beats {choice}")
