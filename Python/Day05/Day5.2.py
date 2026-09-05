def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(50, 3)
print(total)

total = calculate_total(100, 5)
print(total)

total = calculate_total(25, 10)
print(total)

def calculate_total(price, quantity):
    return price*quantity

def apply_discount(total, discount):
    return total - discount

total = calculate_total(500, 60)
final_price = apply_discount(total, 50)

print(final_price)



def calculate_total():

    price = 50
    quantity =4

    calculate_total = price * quantity
    return calculate_total

calculated_total = calculate_total()
print(calculated_total)