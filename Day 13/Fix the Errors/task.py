try:
    age = int(input("How old are you?"))
    if age > 18:
        print(f"You can drive at age {age}.")
    else:
        print("You have to wait till you're above 18 to drive!")
except TypeError:
    print("You cant mix integers and strings in a comparison")
