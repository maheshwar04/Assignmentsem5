# Define the discount percentage
discount_percentage = 0.60

# Print the table header
print("Original Price  Discount  New Price")
print("----------------------------------")

# Define original prices individually
price1 = 4.95
price2 = 9.95
price3 = 14.95
price4 = 19.95
price5 = 24.95

# Calculate and print the table for each price
discount1 = price1 * discount_percentage
new_price1 = price1 - discount1
print(f"${price1:.2f}        ${discount1:.2f}    ${new_price1:.2f}")

discount2 = price2 * discount_percentage
new_price2 = price2 - discount2
print(f"${price2:.2f}        ${discount2:.2f}    ${new_price2:.2f}")

discount3 = price3 * discount_percentage
new_price3 = price3 - discount3
print(f"${price3:.2f}        ${discount3:.2f}    ${new_price3:.2f}")

discount4 = price4 * discount_percentage
new_price4 = price4 - discount4
print(f"${price4:.2f}        ${discount4:.2f}    ${new_price4:.2f}")

discount5 = price5 * discount_percentage
new_price5 = price5 - discount5
print(f"${price5:.2f}        ${discount5:.2f}    ${new_price5:.2f}")

#op
#Original Price  Discount  New Price
#----------------------------------
#$4.95        $2.97    $1.98
#$9.95        $5.97    $3.98
#$14.95        $8.97    $5.98
#$19.95        $11.97    $7.98
#$24.95        $14.97    $9.98
