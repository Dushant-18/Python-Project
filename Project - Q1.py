

Category_A = int(input("Enter Unit sold for Category A :"))
Category_B = int(input("Enter Unit sold for Category B :"))

CalculateTotalUnitSold = lambda a, b: a + b
TotalUnitSold = CalculateTotalUnitSold(Category_A, Category_B)
print("Total Unit Sold:", TotalUnitSold)

CalculateDifference = lambda a, b: a - b
Difference = CalculateDifference(Category_A, Category_B)
print("Difference in Units Sold:", Difference)

CalculateRatio = lambda a, b: a / b if b != 0 else "Division by zero error"
Ratio = CalculateRatio(Category_A, Category_B)
print("Ratio of Category A to Category B:", Ratio)