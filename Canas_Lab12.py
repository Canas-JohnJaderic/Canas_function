menu = {
    "Coffee": 59,
    "Macchiato": 59,
    "Coke Float": 79,
    "Fries": 79,
    "Fish and Chips": 99,
    "Fried Chicken": 149,
    "Hamburg Steak": 149,
    "Vegan Salad": 199,
    "Wagyu Beef": 299
}

#display of ietms
def menushow():
    print("Welcome to Drinking and Driving\nThese are our available Items:")
    for item, price in menu.items():
        print(f"{item}: Pesos {price:.2f}")

#you order here
def ordnow():
    total = 0
    while True:
        order = input("------------------------------------------------------------------------------------------------------------\nPlease enter the item you'd like to order: ").strip()
        if order in menu:
            #adds price from all or just one order
            total += menu[order]
            print(f"You have selected {order}, which costs Pesos {menu[order]:.2f}.")
        else:
            print("Item is not on the menu. Please choose another item")
            continue
        
        if input("Would you like to order another item? (Yes/No): ").strip().lower() != "yes":
            break

    return total

#Paypament style
def gcash(total):
    while True:
        try:
            #input to pay
            pay = float(input(f"------------------------------------------------------------------------------------------------------------\nYour total is Pesos {total:.2f}. Please enter your payment: Pesos "))
            if pay < total:
                print("Insufficient payment. Please enter a valid amount.")
            else:
                print(f"Thank you for your payment! Your change is Pesos {pay - total:.2f}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid amount for payment.")

#combination of the definided functions
def final():
    menushow()
    total = ordnow()
    gcash(total)

#print all the thingies
final()
