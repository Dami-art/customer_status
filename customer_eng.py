# Program: Customer status and discount
# Author: Damjana
# Language: English

while True:
    customer_name = input("Enter customer's full name: ")
    if " " not in customer_name:
        print("Name not entered correctly, please enter first and last name: ")
        continue
    else:
        full_name = customer_name.split()
        first_name = full_name[0]
        last_name = full_name[1]
        break

num_purchases = int(input("Enter number of purchases in the last year: "))

if num_purchases > 0:
    total_spent = 0
    purchases_above_10k = 0
    for x in range(1, num_purchases + 1):
        purchase_value = float(input(f"Enter amount for purchase {x} in dinars: "))
        total_spent += purchase_value
        if purchase_value > 10000:
            purchases_above_10k += 1

    print(f"Dear {first_name}, you have spent {total_spent:.2f} dinars in total, "
          f"with {purchases_above_10k} purchases above 10,000 dinars.")

def status(total_spent, num_purchases):
    if total_spent > 100000 and num_purchases > 10:
        return "VIP"
    else:
        return "STANDARD"

customer_status = status(total_spent, num_purchases)
print(f"Customer {first_name} {last_name} has {customer_status} status.")

price = float(input(f"Dear {first_name}, enter the price of the item you want to buy: "))

def calculate_discount(price, customer_status):
    if customer_status == "VIP":
        discount = 10
    else:
        discount = 5
    discounted_price = price - (price * discount / 100)
    return discounted_price

new_price = calculate_discount(price, customer_status)
print(f"The price of the item with discount is: {new_price:.2f} dinars.")