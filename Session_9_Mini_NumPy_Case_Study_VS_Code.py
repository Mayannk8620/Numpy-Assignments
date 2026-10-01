# SESSION 9 - Mini NumPy Case Study
# TASK 1 - Create a Prices Array


# NumPy library ko import kar rahe hain.
import numpy as np

# Diye gaye product prices ka NumPy array bana rahe hain.
prices = np.array([299, 499, 799, 0, 1599, -1, 899])

# Prices array ko print kar rahe hain.
print("Original Prices:", prices)

# Array ka data type check karke print kar rahe hain.
print("Data Type:", prices.dtype)



# TASK 2 - Clean Invalid Prices Using Boolean Indexing


# NumPy library ko import kar rahe hain.
import numpy as np

# Original prices ka array bana rahe hain.
prices = np.array([299, 499, 799, 0, 1599, -1, 899])

# Boolean indexing se sirf positive prices select kar rahe hain.
positive_prices = prices[prices > 0]

# Positive prices ka average calculate kar rahe hain.
average_price = np.mean(positive_prices)

# 0 aur negative values ko average positive price se replace kar rahe hain.
cleaned_prices = np.where(prices <= 0, average_price, prices)

# Original prices ko print kar rahe hain.
print("Original Prices:", prices)

# Positive prices ka average print kar rahe hain.
print("Average Positive Price:", average_price)

# Cleaned prices ko print kar rahe hain.
print("Cleaned Prices:", cleaned_prices)



# TASK 3 - Calculate Total Bill for Each Item


# NumPy library ko import kar rahe hain.
import numpy as np

# Product prices ka array bana rahe hain.
prices = np.array([299, 499, 799, 0, 1599, -1, 899])

# Sirf positive prices ko select kar rahe hain.
positive_prices = prices[prices > 0]

# Positive prices ka average calculate kar rahe hain.
average_price = np.mean(positive_prices)

# Invalid prices ko average price se replace kar rahe hain.
cleaned_prices = np.where(prices <= 0, average_price, prices)

# Har item ki quantity ka array bana rahe hain.
quantities = np.array([2, 1, 3, 4, 2, 1, 5])

# Price aur quantity ko multiply karke har item ka total bill nikal rahe hain.
item_bills = cleaned_prices * quantities

# Cleaned prices ko print kar rahe hain.
print("Cleaned Prices:", cleaned_prices)

# Quantities ko print kar rahe hain.
print("Quantities:", quantities)

# Har item ka total bill print kar rahe hain.
print("Total Bill for Each Item:", item_bills)



# TASK 4 - Generate a Price Summary Report


# NumPy library ko import kar rahe hain.
import numpy as np

# Original prices ka array bana rahe hain.
prices = np.array([299, 499, 799, 0, 1599, -1, 899])

# Sirf positive prices ko select kar rahe hain.
positive_prices = prices[prices > 0]

# Positive prices ka average calculate kar rahe hain.
average_price = np.mean(positive_prices)

# Invalid prices ko average price se replace karke cleaned array bana rahe hain.
cleaned_prices = np.where(prices <= 0, average_price, prices)

# Har item ki quantity store kar rahe hain.
quantities = np.array([2, 1, 3, 4, 2, 1, 5])

# Har item ka bill calculate kar rahe hain.
item_bills = cleaned_prices * quantities

# Cleaned prices mein minimum value find kar rahe hain.
minimum_price = np.min(cleaned_prices)

# Cleaned prices mein maximum value find kar rahe hain.
maximum_price = np.max(cleaned_prices)

# Cleaned prices ka average calculate kar rahe hain.
average_cleaned_price = np.mean(cleaned_prices)

# Cleaned prices ka total calculate kar rahe hain.
total_prices = np.sum(cleaned_prices)

# Sabhi items ka combined bill calculate kar rahe hain.
total_bill = np.sum(item_bills)

# Summary report ka heading print kar rahe hain.
print("----- Price Summary Report -----")

# Minimum price print kar rahe hain.
print("Minimum Price:", minimum_price)

# Maximum price print kar rahe hain.
print("Maximum Price:", maximum_price)

# Average price print kar rahe hain.
print("Average Price:", average_cleaned_price)

# Sabhi cleaned prices ka total print kar rahe hain.
print("Total of All Prices:", total_prices)

# Sabhi items ka combined total bill print kar rahe hain.
print("Total Bill for All Items:", total_bill)


# TASK 5 - Find Unique Price Values


# NumPy library ko import kar rahe hain.
import numpy as np

# Original prices ka array bana rahe hain.
prices = np.array([299, 499, 799, 0, 1599, -1, 899])

# Sirf positive prices ko select kar rahe hain.
positive_prices = prices[prices > 0]

# Positive prices ka average calculate kar rahe hain.
average_price = np.mean(positive_prices)

# Invalid prices ko average price se replace kar rahe hain.
cleaned_prices = np.where(prices <= 0, average_price, prices)

# np.unique() ka use karke duplicate values ko remove kar rahe hain.
unique_prices = np.unique(cleaned_prices)

# Cleaned prices print kar rahe hain.
print("Cleaned Prices:", cleaned_prices)

# Unique price values print kar rahe hain.
print("Unique Price Values:", unique_prices)

# Unique price values ki total counting print kar rahe hain.
print("Number of Unique Prices:", len(unique_prices))
