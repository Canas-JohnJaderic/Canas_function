menu = {
    "Coffe": 59,
    "Machiatto": 59,
    "Coke Float": 79,
    "Fries": 79,
    "Fish and Chips": 99,
    "Fried Chicken": 149,
    "Hamburg Steak": 149,
    "Vegan Salad": 199,
    "Wagyu Beef": 299 
}

#display of ietms
print("Welcome to Drinking and Driving\nThese are our available Items:")
for item, price in menu.items():
    print(f"{item}: Pesos {price:.2f}")

total = 0

#order process
order = ""
while order not in menu:
    order = input("------------------------------------------------------------------------------------------------------------\nPlease enter the item you'd like to order: ").strip()
    total += menu[order]
    print(f"You have selected {order}, which costs Pesos {menu[order]:.2f}.")
    # want order again?
    ordgain = input("---------------------\nWould you like to order another Item? Yes or No\n---------------------\nEnter Here: ")
    if ordgain == "no" or "No":
        break
    elif ordgain != "yes" or "Yes":
        print("Invalid input. Please enter 'Yes' or 'No' only.")

#Gcash payment real
while True:
    try:
        pay = float(input(f"------------------------------------------------------------------------------------------------------------\nYour total is Pesos {total:.2f}. Please enter your payment: Pesos "))
        if pay < total:
            print("Insufficient payment. Please enter a valid amount.")
        else:
            change = pay - total
            print(f"Thank you for your payment! Your change is Pesos {change:.2f}")
            break
    #if enter is not valid        
    except ValueError:
        print("Invalid input. Please enter a valid amount for payment.")
