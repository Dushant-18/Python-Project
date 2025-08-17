# Sample Input
products = [
    {"product_name": "Product A", "stock": 50},
    {"product_name": "Product B", "stock": 150},
    {"product_name": "Product C", "stock": 30},
    {"product_name": "Product D", "stock": 75},
    {"product_name": "Product E", "stock": 20}
]

threshold = 40

# Find products that need replenishment
reorder_list = []

for product in products:
    if product["stock"] < threshold:
        reorder_list.append(product["product_name"])

# Print Output
print("Products that need replenishment:")
for item in reorder_list:
    print(item)
