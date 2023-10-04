# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

# course = 'Python for Beginners'
# print(course.replace('Beginners', 'Absolute Beginners'))
# print('Python' in course)

# print(10 ** 3)
# x = 10
# x -= 3
# print(x)


# y = -2.9
# print(abs(y))
# print(round(y))

# import math
# print(math.floor(2.9))
# print(math.ceil(13.4))

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
#
# else:
#     print("What a lovely day")
# print("Enjoy your day")

# price = 1000000
# good_credit = False
# bad_credit = True
#
# if good_credit:
#     price  = 0.9 * price
#     print(f"The price is ${price}")
# elif bad_credit:
#     price = 0.8 * price
#     print(f"The price is ${price}")


# has_good_credit = True
# has_criminal_record = True
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# temperature = 32
#
# if temperature != 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day!")

# name = "Klaudia"
#
# if len(name) < 3:
#     print("Name must be at least 3 characters!")
# elif len(name) > 50:
#     print("Name can be a maximum 50 characters!")
# else:
#     print("Name looks good!")

# weight = input("Weight: ")
# weight = float(weight)
#
# unit = input("(L)bs or (K)g: ")
# unit = unit.lower()
#
# if unit == 'l':
#     weight = weight * 0.45
#     print(f'You are {weight} kilograms')
#
# elif unit == 'k':
#     weight = weight * 2.20
#     print(f'You are {weight} pounds')
#
# else:
#     print(f'Enter the correct unit')

# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print('done')

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
    else:
        print("You failed!")
print("Game over!")