#dictionary to store product information
product_info = {
    "product_name": "Wireless Mouse",
    "SKU": "WM-12345",
    "price": 25.99,
    "category": "Electronics"
}

# Function to fetch product details
def product_details(product):
    print("Product Name:", product["product_name"])
    print("Product SKU:", product["SKU"])

# Query by customer service representative
product_details(product_info)