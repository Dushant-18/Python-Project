# Take product prices from the user
product_prices_input = input("Enter product prices separated by spaces: ")
product_prices = [int(price) for price in product_prices_input.split()]

# Take premium product price from the user
premium_product_price = int(input("Enter premium product price: "))

# Find highest and lowest prices
highest_price = max(product_prices)
lowest_price = min(product_prices)

# Extract mid-range products (excluding highest & lowest)
mid_range_products = [price for price in product_prices if price != highest_price and price != lowest_price]

# Add the premium product price to the list
updated_product_list = product_prices.copy()
updated_product_list.append(premium_product_price)

# Output
print("Highest Price:", highest_price)
print("Lowest Price:", lowest_price)
print("Mid-Range Products:", mid_range_products)
print("Updated Product List with Premium Price:", updated_product_list)
