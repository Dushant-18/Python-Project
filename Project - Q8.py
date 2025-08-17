def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Main program
def analyze_feedback():
    feedback = input("Enter customer feedback: ")
    print("\nCustomer Feedback Analysis:")
    print("Original Feedback:", feedback)
    print("Number of Vowels:", count_vowels(feedback))
    print("Reversed Feedback:", feedback[::-1])

# Run the program
analyze_feedback()