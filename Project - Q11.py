# Customer spending amounts
customer_spendings = [200, 800, 1500, 3000, 450, 1200]

print("Customer Spending Categories:")

# Loop through each customer's spending
for i, spending in enumerate(customer_spendings, start=1):
    if spending < 500:
        category = "Low"
    elif 500 <= spending < 1500:
        category = "Medium"
    else:
        category = "High"
    
    # Print categorized result
    print(f"Customer {i}: Spending = ${spending} -> Category: {category}")
