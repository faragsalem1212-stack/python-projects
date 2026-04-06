import random
import string

# اختيار الكمبيوتر للكلمة
words = ["kitchen", "vast", "modern", "laptop", "mosquito", "program"]
com_choice = random.choice(words)
# طباعة عدد احرف الكلمات للمستخدم
secret = []
for letter in com_choice:
    secret.append("_")
print(secret)
# عدد محاولات المستخدم (هو الي يختارها)
tries = input("How many tries u need: ")
# للتحقق من ان المدخل ارقام
ver = []
for x in string.digits:
    ver.append(x)
while True:
    if tries not in ver:
        print("Invalid input, please choose only numbers...")
        tries = input("How many tries u need: ")
    elif str(tries) in ver and tries == "0":
        print("You can't choose 0, please try again...")
        tries = input("How many tries u need: ")
    else:
        break
int_tries = int(tries)
print(f"Ok, you have {int_tries} tries, GO ON!")
# تخمين الحرف
while "_" in secret:
    if int_tries > 0:
        guess = input("Guess a letter: ").lower()
        # للتحقق من ان الحرف صحيح او لا
        com_word_letters = []
        for x in com_choice:
            com_word_letters.append(x)
        # لدينا الاحرف متقطعة للكلمة المختارة
        # اذا كان التخمين صحيح
        if guess in com_word_letters:
            for position in range(len(com_choice)):
                if com_choice[position] == guess:
                    secret[position] = guess
            print(secret)
            int_tries -= 0
            if "_" not in (secret):
                break
            print(f"You gussed right!, still have {int_tries} tries.")
        else:
            print(secret)
            int_tries -= 1
            print(f"You guessed wrong, you have {int_tries} tries now.")
    elif int_tries == 0 or int_tries < 0:
        print("""
   You Lost!
   =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
   ========='''] """)
        print(f"The word was, {com_choice}")
        quit()
print("***   You Woooon!!!   ***")
quit()
