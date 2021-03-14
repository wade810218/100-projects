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

profit = {
    "money": 0
}


def report():
    """Print resource report."""
    for ingredient in resources:
        unit = 'ml'
        if ingredient == "coffee":
            unit = 'g'
        print(f"{ingredient}: {resources[ingredient]}{unit}")
    print(f"money: ${profit['money']}")


def check_resources(coffee):
    """Return True when order can be made, False if ingredients are insufficient"""
    for item in coffee['ingredients']:        
        if coffee['ingredients'][item] > resources[item]:        
            print(f"Sorry there is not enough {item}.")
            return False           
    return True


def process_coins():
    """Return the total calculated from coin inserted"""
    def count_coins(quarter, dime, nickle, penny):
        total = quarter * 0.25 + dime * 0.10 + nickle * 0.05 + penny * 0.01
        return total

    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes =  int(input("how many dimes?: "))
    nickles =  int(input("how many nickles?: "))
    pennies =  int(input("how many pennies?: "))
    
    return count_coins(quarters, dimes, nickles, pennies)



def check_transaction(coffee, payment):  
    """Return True when the payment is accepted, or False if money is insufficient."""
    if payment >= coffee['cost']:        
        profit['money'] += coffee['cost']
        if payment > coffee['cost']:
            change = round(payment - coffee['cost'] , 2)
            print(f"Here is {change} dollars in change.")
      
        return True

    print("Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(coffee):
    """Deduct the required ingredients from the resources."""
    for item in coffee['ingredients']:        
        resources[item] -= coffee['ingredients'][item]

    

def operate(choice):   
    if choice == "report":
        report()
    elif choice in MENU.keys():    
        drink = MENU[choice]            
        if check_resources(drink):
            print(f"{choice} is ${drink['cost']}") 
            if check_transaction(drink , process_coins()):
                make_coffee(drink)
                print(f"Here is your {choice} ☕. Enjoy!")
    elif choice == "off":
        global turn_on
        turn_on = False       
      

turn_on = True

while turn_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    operate(order)





    
