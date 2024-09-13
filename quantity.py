quantity = int(input("Enter the quantity of items: "))
price = float(input("Enter the price per item: "))

total_cost = quantity*price

formatted_price = "{:.2f}".format(price)
formatted_total_cost = "{:.2f}".format(total_cost)

output = "Total cost: {} items at Rs.{} each = Rs.{}".format(quantity,formatted_price , formatted_total_cost)
print(output)