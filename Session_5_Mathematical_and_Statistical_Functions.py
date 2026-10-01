# SESSION 5 - Mathematical and Statistical Functions

# Task 1 - Compare Instagram Likes With a Friend's Likes

# NumPy library ko import kar rahe hain.
import numpy as np

# Mere 7 Instagram posts ke likes store kar rahe hain.
my_likes = np.array([120, 250, 180, 320, 150, 275, 400])

# Friend ke 7 posts ke likes store kar rahe hain.
friend_likes = np.array([100, 230, 200, 300, 160, 250, 380])

# Dono arrays ko add karke combined likes nikal rahe hain.
combined_likes = np.add(my_likes, friend_likes)

# Dono arrays ko subtract karke likes ka difference nikal rahe hain.
difference = np.subtract(my_likes, friend_likes)

# Print the results.
print("Combined Likes:", combined_likes)
print("Difference in Likes:", difference)


# Task 2 - Calculate Final Bill After a 10 Percent Discount

# NumPy library ko import kar rahe hain.
import numpy as np

# Zomato order ke item prices store kar rahe hain.
prices = np.array([250, 180, 320, 150, 400])

# np.multiply() se 10 percent discount apply kar rahe hain.
discounted_prices = np.multiply(prices, 0.90)

# Discounted prices ko add karke final bill nikal rahe hain.
final_bill = np.sum(discounted_prices)

# Print the results.
print("Discounted Prices:", discounted_prices)
print("Final Bill:", final_bill)


# Task 3 - Analyze 30 Days of Step Counts

# NumPy library ko import kar rahe hain.
import numpy as np

# Last 30 days ke step counts store kar rahe hain.
steps = np.array([
    5200, 6100, 7300, 4800, 8000, 6900, 7500, 6200, 7100, 5600,
    6800, 7900, 8200, 6000, 5400, 7600, 8800, 6900, 7200, 6500,
    5900, 8100, 7700, 7000, 6400, 8500, 9000, 7300, 6800, 6100
])

# Fitness ke liye common statistical values calculate kar rahe hain.
print("Mean:", np.mean(steps))
print("Median:", np.median(steps))
print("Standard Deviation:", np.std(steps))
print("Maximum:", np.max(steps))


# Task 4 - Round Movie Ratings in Different Ways

# NumPy library ko import kar rahe hain.
import numpy as np

# 1 se 5 ke beech 10 movie ratings bana rahe hain.
ratings = np.array([4.2, 3.7, 4.8, 2.9, 3.5, 4.1, 3.2, 4.6, 2.7, 4.9])

# Rating ko nearest whole number par round kar rahe hain.
nearest = np.round(ratings)

# Rating ko hamesha neeche ki taraf round kar rahe hain.
rounded_down = np.floor(ratings)

# Rating ko hamesha upar ki taraf round kar rahe hain.
rounded_up = np.ceil(ratings)

# Print the results.
print("Original Ratings:", ratings)
print("Nearest Whole Number:", nearest)
print("Always Rounded Down:", rounded_down)
print("Always Rounded Up:", rounded_up)


# Task 5 - Calculate Skipped Song Percentage and 75th Percentile

# NumPy library ko import kar rahe hain.
import numpy as np

# 1 skipped song ko aur 0 played song ko represent karta hai.
skipped = np.array([0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])

# Skipped songs ka percentage calculate kar rahe hain.
skipped_percentage = np.mean(skipped) * 100

# Skip indicator values ka 75th percentile calculate kar rahe hain.
percentile_75 = np.percentile(skipped, 75)

# Print the results.
print("Percentage of Songs Skipped:", skipped_percentage, "%")
print("75th Percentile of Skip Indicator:", percentile_75)

