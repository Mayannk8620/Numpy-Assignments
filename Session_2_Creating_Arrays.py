# SESSION 2 - Creating Arrays

# Task 1 - Create an Array of Zomato Order Ratings

# NumPy library ko import kar rahe hain.
import numpy as np

# Last 5 Zomato order ratings ko array mein store kar rahe hain.
ratings = np.array([4, 5, 3, 4, 5])

# Ratings array ko print kar rahe hain.
print("Zomato Order Ratings:", ratings)


# Task 2 - Generate Even Numbers Using arange()

# NumPy library ko import kar rahe hain.
import numpy as np

# 10 se 30 tak even numbers generate kar rahe hain.
# Stop value include nahi hoti, isliye 30 tak lane ke liye stop value 32 rakhi hai.
even_numbers = np.arange(10, 32, 2)

# Result ko print kar rahe hain.
print("Even Numbers from 10 to 30:", even_numbers)


# Task 3 - Generate Equally Spaced Values Using linspace()

# NumPy library ko import kar rahe hain.
import numpy as np

# 0 aur 1 ke beech 8 equally spaced values bana rahe hain.
volume_levels = np.linspace(0, 1, 8)

# Print the values.
print("Volume Levels:", volume_levels)


# Task 4 - Simulate an Add to Cart Counter

# NumPy library ko import kar rahe hain.
import numpy as np

# Cart count ko represent karne ke liye 10 zeros ka array bana rahe hain.
cart = np.zeros(10, dtype=int)

# 3rd aur 7th item ko 1 se update kar rahe hain.
# Python mein indexing 0 se start hoti hai, isliye positions 2 aur 6 hain.
cart[2] = 1
cart[6] = 1

# Print the updated cart.
print("Updated Cart Counter:", cart)


# Task 5 - Generate Random OTP Codes

# NumPy library ko import kar rahe hain.
import numpy as np

# Random result ko same rakhne ke liye seed set kar rahe hain.
np.random.seed(42)

# 1000 se 9999 ke beech 6 random four-digit OTP codes bana rahe hain.
otp_codes = np.random.randint(1000, 10000, size=6)

# Print the OTP codes.
print("Random OTP Codes:", otp_codes)

