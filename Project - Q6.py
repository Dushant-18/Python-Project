# Sample input
products_sold = ["laptop", "mouse", "keyboard", "monitor", "printer"]

print("---For Loop ----")
for product in products_sold:
    print(product.upper())

print("----- while Loop ----")
i = 0
while i < len(products_sold):
    print(products_sold[i].upper())
    i += 1