# Lists of positive and negative words
positive_words = ["good", "happy", "excellent", "great","nice","very good","very nice"]
negative_words = ["bad", "disappointed", "poor", "terrible"]

# Take customer feedback as input
feedback = input("Enter customer feedback: ").lower()  # Convert to lowercase for easy matching

# Check sentiment
sentiment = "Neutral"
for word in positive_words:
    if word in feedback:
        sentiment = "Positive"
        break

for word in negative_words:
    if word in feedback:
        sentiment = "Negative"
        break

# Print result
print("Customer Feedback Sentiment:", sentiment)
