# product prices
product_price = [150, 85, 300, 120, 45, 200]

# Predefined discount threshold
discount_threshold = 100

# Filter products below threshold
eligible_products = [price for price in product_price if price < discount_threshold]

# Print results
print("Products eligible for the discount campaign:", eligible_products)
