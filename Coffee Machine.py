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
}

# penny - 0.01
# nickel - 0.05
# dime - 0.10
# quarter - 0.25

money = 0

espresso_price = (MENU.get('espresso')).get('cost')
latte_price = (MENU.get('latte')).get('cost')
cappuccino_price = (MENU.get('cappuccino')).get('cost')


#print report how much resources left
def report_resources():

    print(f"Water: {resources.get('water')}ml\nMilk: {resources.get('milk')}ml\nCoffee: {resources.get('coffee')}gr\nMoney: {money}$")


#check sufficient resources
def check_resources():
    if choice.lower() == "espresso":
        print(f"The price is: ${espresso_price}")
        if resources.get('water') >= 50:  
            if resources.get('coffee') >= 18: 
                return True
            else:
                print("Not enough coffee")
                return False
        else:
            print("Not enough water")
            return False
    elif choice.lower() == "latte":
        print(f"The price is: ${latte_price}")
        if resources.get('water') >= 200:  
            if resources.get('coffee') >= 24:  
                if resources.get('milk') >= 150:  
                    return True
                else:
                    print("Not enough milk")
                    return False
            else:
                print("Not enough coffee")
                return False
        else:
            print("Not enough water")
            return False
    elif choice.lower() == "cappuccino":
        print(f"The price is: ${cappuccino_price}")
        if resources.get('water') >= 250: 
            if resources.get('coffee') >= 24:  
                if resources.get('milk') >= 100:  
                    return True
                else:
                    print("Not enough milk")
                    return False
            else:
                print("Not enough coffee")
                return False
        else:
            print("Not enough water")
            return False


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        report_resources()
        continue
    elif choice == "no":
        print("Bye bye")
        break
    elif choice not in MENU and choice != "report":
        print("Invalid choice. Please select espresso, latte, cappuccino.")
        continue

    else:

        get_choice_price = ((MENU.get(choice)).get('cost'))
        consumed_water = MENU.get(choice, {}).get('ingredients', {}).get('water', 0)
        consumed_milk = MENU.get(choice, {}).get('ingredients', {}).get('milk', 0)
        consumed_coffee = MENU.get(choice, {}).get('ingredients', {}).get('coffee', 0)
        if not check_resources():
            # If resources are insufficient, do not proceed further
            continue
    
        else:

            print("Please insert coins. ")
            pennies = int(input("How many pennies? "))
            nickels = int(input("How many nickels? "))
            dimes = int(input("How many dimes? "))
            quarters = int(input("How many quarters? "))

            inserted_money = (pennies*0.01) + (nickels*0.05) + (dimes*0.1) + (quarters*0.25)
            print(f"Total amount inserted is: ${inserted_money}")
            change = round((inserted_money - get_choice_price),2)
            if change < 0:
                print("Not enough money inserted")
            else:
                print(f"Your change is: ${change}")
                print(f"Here is your {choice}. Enjoy!")
                money+= round(inserted_money - change,2)
                resources['water'] -= consumed_water
                resources['coffee'] -= consumed_coffee
                if 'milk' in resources:  # Only update milk if it exists
                    resources['milk'] -= consumed_milk

        
            
            buy_more=input("Do you want to buy some more? y/n: ")
            if buy_more =="y":
                True
            else:
                break
