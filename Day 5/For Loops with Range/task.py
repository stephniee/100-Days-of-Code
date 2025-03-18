# second_num = 0
# for number in range(1,101):
#     print(number)
#     second_num += number
# print("second number: " + str(second_num))

for number in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
