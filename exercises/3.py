import random
number=int(random.randint(1,25))
a = int(input("please give a number between 1 and 25: "))
def guess(guessnumbers):
    if guessnumbers > number:
        print("decrease your number")
        new_number = int(input("please give a new number: "))
        guess(new_number)
    elif guessnumbers < number:
        print("increase your number")
        new_number1 = int(input("please give a new number: "))
        guess(new_number1)
    else:
        print("Congratulations, you know the number.")
guess(a)
