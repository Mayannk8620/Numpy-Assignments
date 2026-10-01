# SESSION 4 - Array Operations

# Task 1 - Calculate Average Instagram Engagement

# NumPy library ko import kar rahe hain.
import numpy as np

# 7 Instagram posts ke likes aur comments store kar rahe hain.
likes = np.array([120, 250, 180, 320, 150, 275, 400])
comments = np.array([10, 25, 15, 30, 12, 20, 35])

# Har post ke likes aur comments ko element-wise add karke engagement nikal rahe hain.
engagement = likes + comments

# Sabhi posts ka average engagement calculate kar rahe hain.
average_engagement = np.mean(engagement)

# Result ko print kar rahe hain.
print("Engagement per Post:", engagement)
print("Average Engagement:", average_engagement)


# Task 2 - Calculate Final Food Prices After Discount

# NumPy library ko import kar rahe hain.
import numpy as np

# 5 food items ke prices store kar rahe hain.
prices = np.array([250, 180, 320, 150, 400])

# Har item ka corresponding discount rupees mein store kar rahe hain.
discounts = np.array([20, 15, 30, 10, 50])

# Har price se corresponding discount ko element-wise subtract kar rahe hain.
final_prices = prices - discounts

# Print the final prices.
print("Final Prices:", final_prices)


# Task 3 - Find IPL Matches With Scores Above 180

# NumPy library ko import kar rahe hain.
import numpy as np

# 5 IPL matches ke scores store kar rahe hain.
scores = np.array([165, 195, 178, 210, 185])

# Har score ko 180 se compare kar rahe hain.
high_scores = scores > 180

# Boolean array ko print kar rahe hain.
print("Scores:", scores)
print("Scores Above 180:", high_scores)


# Task 4 - Find Transactions Paid by App or PhonePe

# NumPy library ko import kar rahe hain.
import numpy as np

# 1 ka matlab transaction app se paid hua hai.
paid_by_app = np.array([1, 0, 1, 0, 0, 1])

# 1 ka matlab transaction PhonePe se paid hua hai.
paid_by_phonepe = np.array([0, 1, 0, 0, 1, 0])

# logical_or tab True deta hai jab dono mein se koi ek condition True ho.
paid_by_either = np.logical_or(paid_by_app == 1, paid_by_phonepe == 1)

# Result ko print kar rahe hain.
print("Paid by App or PhonePe:", paid_by_either)


# Task 5 - Add a Step Bonus Using Broadcasting

# NumPy library ko import kar rahe hain.
import numpy as np

# 7 din ke walking steps store kar rahe hain.
steps = np.array([4500, 6200, 7100, 5300, 8000, 6900, 7500])

# Broadcasting ka use karke har din 500 steps ka bonus add kar rahe hain.
updated_steps = steps + 500

# Week ke total steps calculate kar rahe hain.
weekly_total = np.sum(updated_steps)

# Print the results.
print("Updated Daily Steps:", updated_steps)
print("Total Weekly Steps:", weekly_total)

