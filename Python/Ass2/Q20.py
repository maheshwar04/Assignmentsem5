# Define the discount percentage
discount_percentage = 0.60

# Define a list of original prices
original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

# Print the table header
print("Original Price  Discount  New Price")
print("----------------------------------")

# Generate and print the table
for price in original_prices:
    discount = price * discount_percentage
    new_price = price - discount
    print(f"${price:.2f}        ${discount:.2f}    ${new_price:.2f}")

#op
#Original Price  Discount  New Price
#----------------------------------
#$4.95        $2.97    $1.98
#$9.95        $5.97    $3.98
#$14.95        $8.97    $5.98
#$19.95        $11.97    $7.98
#$24.95        $14.97    $9.98
