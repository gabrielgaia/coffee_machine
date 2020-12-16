from data import MENU
from data import resources


def coffee(client_order: str):
    def check_resources() -> bool:
        water_order = MENU[client_order]['ingredients']['water']
        coffee_order = MENU[client_order]['ingredients']['coffee']

        if client_order != 'espresso':
            milk_order = MENU[client_order]['ingredients']['milk']
            if milk_order > resources['milk']:
                print("I'm sorry, but there's not enough milk.")
                return False
            else:
                resources['milk'] -= milk_order

        if water_order > resources['water']:
            print("I'm sorry, but there's not enough water.")
            return False
        elif coffee_order > resources['coffee']:
            print("I'm sorry, but there's not enough coffee.")
            return False
        else:
            resources['water'] -= water_order
            resources['coffee'] -= coffee_order
            return True

    client_order = client_order.lower()
    if client_order == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
    elif client_order == 'espresso' or client_order == 'latte' or client_order == 'cappuccino':
        if check_resources():
            price = MENU[client_order]['cost']
            print(f'It costs ${price}.')
            print('Please insert coins.')
            quarters = int(input('How many quarters? '))
            dimes = int(input('How many dimes? '))
            nickels = int(input('How many nickels? '))
            pennies = int(input('How many pennies? '))
            total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
            if total >= price:
                change = total - price
                if change > 0:
                    print(f'Here is ${round(change, 2)} in change.')
                print(f'Here is your {client_order} ☕\nEnjoy!')
            else:
                print("There's not enough money. Money refunded.")
    else:
        print("Sorry, I'm afraid we don't have that.")


should_continue = True
while should_continue:
    order = input('What would you like? (espresso/latte/cappuccino): ')
    coffee(order)
    if order.lower() != 'report':
        sequence = input('Would like to make another order? ')
        if sequence.lower() == 'no' or sequence.lower() == 'n':
            print('Bye!')
            should_continue = False
