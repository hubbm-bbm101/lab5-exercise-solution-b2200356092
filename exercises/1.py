user_choice = int(input("""select the action you want to do:
(1) Sum of odd numbers
(2) Avarage of even numbers\n1-2:"""))


def sum_off_odd_numbers(a):
    total = 0
    for numbers in range(1, a + 1):
        if numbers % 2 == 1:
            total = total + numbers
    print(total)


def avarage_of_even_numbers(b):
    total = 0
    num = 0
    for numberss in range(1, b + 1):
        if numberss % 2 == 0:
            total = total + numberss
            num += 1
    print(total / num)

if user_choice == 1:
    given_number = int(input("please give a number: "))
    sum_off_odd_numbers(given_number)
elif user_choice == 2:
    given_number = int(input("please give a number: "))
    avarage_of_even_numbers(given_number)
else:
    print("please give a correct number")







