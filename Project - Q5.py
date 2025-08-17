# Predefined threshold
threshold = 20

# Take stock level as input
stock_level = int(input("Enter stock level: "))

# Check stock level
if stock_level < threshold:
    print("Reorder Now")
else:
    print("Stock is sufficient")