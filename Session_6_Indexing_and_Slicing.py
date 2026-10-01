# SESSION 6 - Indexing and Slicing

# Task 1 - Access First and Last Product Prices

# NumPy library ko import kar rahe hain.
import numpy as np

# Product prices ka array bana rahe hain.
prices = np.array([199, 299, 399, 499, 599])

# Basic indexing se first element access kar rahe hain.
first_price = prices[0]

# Negative indexing se last element access kar rahe hain.
last_price = prices[-1]

# Print both prices.
print("First Price:", first_price)
print("Last Price:", last_price)


# Task 2 - Slice Cricket Scores for Matches 2 to 4

# NumPy library ko import kar rahe hain.
import numpy as np

# Rows players ko aur columns 5 matches ko represent karte hain.
scores = np.array([
    [45, 60, 55, 70, 65],
    [30, 50, 48, 62, 58],
    [80, 75, 90, 85, 88]
])

# Index 1 se 3 tak columns slice karke matches 2 se 4 nikal rahe hain.
selected_scores = scores[:, 1:4]

# Print the selected scores.
print("Scores for Matches 2 to 4:")
print(selected_scores)


# Task 3 - Access the Last Three Ratings

# NumPy library ko import kar rahe hain.
import numpy as np

# Create an array of ratings.
ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5])

# Negative indexing aur slicing se last 3 ratings nikal rahe hain.
last_three = ratings[-3:]

# Result ko print kar rahe hain.
print("Last Three Ratings:", last_three)


# Task 4 - Select Every Third Natural Number

# NumPy library ko import kar rahe hain.
import numpy as np

# Pehle 20 natural numbers ka array bana rahe hain.
numbers = np.arange(1, 21)

# Second element se start karke har third value select kar rahe hain.
selected_numbers = numbers[1::3]

# Result ko print kar rahe hain.
print("Every Third Number Starting from the Second Element:", selected_numbers)


# Task 5 - Filter Flipkart Prices Above 500

# NumPy library ko import kar rahe hain.
import numpy as np

# Product prices ka array bana rahe hain.
prices = np.array([250, 650, 450, 800, 1200, 350, 700])

# Boolean indexing se sirf 500 se greater prices select kar rahe hain.
high_prices = prices[prices > 500]

# Print the filtered prices.
print("Prices Above 500:", high_prices)


# Task 6 - Find IPL Scores Above 200 Using where()

# NumPy library ko import kar rahe hain.
import numpy as np

# IPL team scores ko array mein store kar rahe hain.
scores = np.array([210, 180, 195, 220, 205, 175])

# np.where() un indexes ko return karta hai jahan condition True hoti hai.
indexes = np.where(scores > 200)

# Print the indexes.
print("Indexes of Scores Above 200:", indexes[0])

