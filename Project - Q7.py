# Function to calculate area
def calculate_area(length, width):
    return length * width

# function
def main():
    length1, width1 = 20, 15
    length2, width2 = 30, 10
    length3, width3 = 25, 12

    print(f"The area of section 1 is {calculate_area(length1, width1)} square meters.")
    print(f"The area of section 2 is {calculate_area(length2, width2)} square meters.")
    print(f"The area of section 3 is {calculate_area(length3, width3)} square meters.")

# Run the program
main()