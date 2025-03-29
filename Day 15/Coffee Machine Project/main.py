MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

shop_open = True

def print_report():
    for key in resources:
        if key == 'water' or key == 'milk':
            print(f"{key.title()}: {resources[key]}ml")
        elif key == 'coffee':
            print(f"{key.title()}: {resources[key]}g")
        else:
            print(f"{key.title()}: ${resources[key]}")

def deduct_ingredients(ingredient,resource):
    for item, amount in ingredient.items():
        if item in resource:
            resource[item] -= amount
    return resource

def can_make_drink(drink_name, resource, menu):
    """Check if there are enough resources to make the drink."""
    ingredients = menu[drink_name]["ingredients"]

    for item, amount in ingredients.items():
        if resource.get(item, 0) < amount:
            print(f"No dice, not enough {item}.")
            return False  # Not enough resources

    return True  # Sufficient resources

def minus_resource(drink,resource,reference):
    if drink == 'espresso':
        espresso_ingredients = reference[drink]["ingredients"]
        deduct_ingredients(espresso_ingredients,resource)
        print(f"Here is your {drink} ☕️. Enjoy!")
    elif drink == 'latte':
        latte_ingredients = reference[drink]["ingredients"]
        deduct_ingredients(latte_ingredients, resource)
        print(f"Here is your {drink} ☕️. Enjoy!")
    elif drink == 'cappuccino':
        cappuccino_ingredients = reference[drink]["ingredients"]
        deduct_ingredients(cappuccino_ingredients, resource)
        print(f"Here is your {drink} ☕️. Enjoy!")

def get_paid(drink,reference,resource):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    coin_purse = []
    for coin in coins:
        while True:  # Keep prompting until valid input is given
            try:
                amount = int(input(f"How many {coin}? "))
                if amount < 0:
                    raise ValueError("Amount cannot be negative.")  # Custom exception for negative values
                coin_purse.append(amount * coins[coin])
                break  # Exit loop if input is valid
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number.")

    total = sum(coin_purse)
    if total >= reference[drink]["cost"]:
        print(f"Thank you for paying ${total}.")
        cost = reference[drink]["cost"]
        print(f"Here is ${total-cost:.1f} in change.")
        resource.update({"money":cost})
        return True
    else:
        print("Sorry that's not enough money. Money refunded...")
        return False

while shop_open:
    try:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_input in MENU:
            print(f"User Drink: is {user_input}")
            if can_make_drink(user_input,resources,MENU):
                get_paid(drink=user_input,resource=resources,reference=MENU)
                minus_resource(user_input,resources,MENU)
            else:
                print(f"We're out of stock for {user_input} try our other drinks!")
        elif user_input == "report":
            print_report()
        elif user_input == "off":
            print("Bye bye")
            shop_open = False
        else:
            print("Wrong input, try again babes <3")
    except KeyError:
        print("Not found")
    # except:
    #     print("Emergency call tech support")

