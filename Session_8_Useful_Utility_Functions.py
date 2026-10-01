# SESSION 8 - Useful Utility Functions

# Task 1 - Find Unique IPL Team Names

# NumPy library ko import kar rahe hain.
import numpy as np

# Kuch duplicate IPL team names ka array bana rahe hain.
teams = np.array(["CSK", "MI", "RCB", "MI", "KKR", "CSK", "GT", "RCB"])

# np.unique() duplicate values ko remove karke unique values return karta hai.
unique_teams = np.unique(teams)

# Result ko print kar rahe hain.
print("Unique IPL Teams:", unique_teams)


# Task 2 - Count Missing Zomato Ratings

# NumPy library ko import kar rahe hain.
import numpy as np

# Kuch missing ratings ko NaN ke roop mein store kar rahe hain.
ratings = np.array([4.2, 4.5, np.nan, 3.8, np.nan, 4.1, 5.0])

# np.isnan() missing NaN values ke liye True return karta hai.
missing_values = np.isnan(ratings)

# True values ki total counting kar rahe hain.
missing_count = np.sum(missing_values)

# Result ko print kar rahe hain.
print("Missing Ratings:", missing_count)


# Task 3 - Limit Product Prices Using clip()

# NumPy library ko import kar rahe hain.
import numpy as np

# Product prices ka array bana rahe hain.
prices = np.array([80, 150, 450, 900, 1200, 1500])

# Sabhi prices ko 100 se 1000 ke range mein limit kar rahe hain.
limited_prices = np.clip(prices, 100, 1000)

# Result ko print kar rahe hain.
print("Original Prices:", prices)
print("Clipped Prices:", limited_prices)


# Task 4 - Handle NaN and Infinity Values

# NumPy library ko import kar rahe hain.
import numpy as np

# Normal values, NaN aur infinity wala array bana rahe hain.
views = np.array([1200, np.nan, 3500, np.inf, 2800])

# Array mein maximum finite value find kar rahe hain.
finite_values = views[np.isfinite(views)]
maximum_value = np.max(finite_values)

# NaN values ko 0 se replace kar rahe hain.
views_cleaned = np.nan_to_num(views, nan=0, posinf=maximum_value, neginf=0)

# Print the cleaned array.
print("Original Views:", views)
print("Cleaned Views:", views_cleaned)


# Task 5 - Find Indices of Even Numbers Using where()

# NumPy library ko import kar rahe hain.
import numpy as np

# Example numbers ka array bana rahe hain.
numbers = np.array([11, 24, 37, 42, 55, 68, 71, 80])

# Even numbers ke liye Boolean condition bana rahe hain.
even_condition = numbers % 2 == 0

# np.where() un indexes ko return karta hai jahan condition True hoti hai.
even_indexes = np.where(even_condition)

# Even numbers ke indexes aur corresponding values print kar rahe hain.
print("Indexes of Even Numbers:", even_indexes[0])
print("Even Numbers:", numbers[even_indexes])

