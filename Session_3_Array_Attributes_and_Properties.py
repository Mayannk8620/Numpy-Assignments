# SESSION 3 - Array Attributes and Properties

# Task 1 - Display NumPy Array Properties

# NumPy library ko import kar rahe hain.
import numpy as np

# Instagram posts ke likes ka array bana rahe hain.
likes = np.array([120, 250, 180, 320, 150, 275, 400])

# NumPy array ki important properties print kar rahe hain.
print("ndim:", likes.ndim)
print("shape:", likes.shape)
print("size:", likes.size)
print("dtype:", likes.dtype)
print("itemsize:", likes.itemsize)
print("nbytes:", likes.nbytes)


# Task 2 - Reshape Daily Step Counts

# NumPy library ko import kar rahe hain.
import numpy as np

# 5 din ke morning aur evening steps ko array mein store kar rahe hain.
daily_steps = np.array([
    [1200, 1800],
    [1500, 2200],
    [1300, 2000],
    [1700, 2500],
    [1600, 2300]
])

# 2D array ko 1D array mein convert kar rahe hain.
one_d_steps = daily_steps.reshape(10)

# Array ko wapas 5 rows aur 2 columns mein convert kar rahe hain.
five_by_two = one_d_steps.reshape(5, 2)

# Arrays aur unki shapes ko display kar rahe hain.
print("1D Array:", one_d_steps)
print("1D Shape:", one_d_steps.shape)
print("\n5 x 2 Array:")
print(five_by_two)
print("5 x 2 Shape:", five_by_two.shape)


# Task 3 - Reshape Food Item Prices

# NumPy library ko import kar rahe hain.
import numpy as np

# 12 food items ke prices ka array bana rahe hain.
prices = np.array([120, 250, 180, 300, 150, 220, 90, 175, 280, 130, 200, 160])

# Same data ko 3 rows aur 4 columns mein reshape kar rahe hain.
shape_3x4 = prices.reshape(3, 4)

# Same data ko 4 rows aur 3 columns mein reshape kar rahe hain.
shape_4x3 = prices.reshape(4, 3)

# Array ko ek 1D array mein flatten kar rahe hain.
flat_prices = prices.flatten()

# Print all versions.
print("Original Array:")
print(prices)
print("\n3 x 4 Array:")
print(shape_3x4)
print("\n4 x 3 Array:")
print(shape_4x3)
print("\nFlattened Array:")
print(flat_prices)


# Task 4 - Transpose a Spotify Playlist Array

# NumPy library ko import kar rahe hain.
import numpy as np

# Rows playlists ko aur columns song categories ko represent karte hain.
playlist = np.array([
    [40, 30, 20],
    [25, 35, 15],
    [30, 20, 40]
])

# transpose() se rows aur columns ko swap kar rahe hain.
transposed_playlist = playlist.T

# Display both arrays.
print("Original Playlist Array:")
print(playlist)

print("\nTransposed Playlist Array:")
print(transposed_playlist)


# Task 5 - Reshape and Flatten Product Ratings

# NumPy library ko import kar rahe hain.
import numpy as np

# 15 Flipkart product ratings ko array mein store kar rahe hain.
ratings = np.array([4.2, 3.8, 4.5, 4.0, 3.5, 4.7, 4.1, 3.9, 4.8, 4.3, 3.7, 4.6, 4.0, 3.6, 4.9])

# Ratings ko 3 rows aur 5 columns mein reshape kar rahe hain.
rating_table = ratings.reshape(3, 5)

# flatten() array ko wapas ek single 1D array mein convert karta hai.
flattened_ratings = rating_table.flatten()

# Jab humein saare values ek continuous list mein chahiye hoti hain tab flatten() useful hai.
# reshape() elements ki sankhya badle bina array ka shape change karta hai.
print("3 x 5 Ratings:")
print(rating_table)

print("\nFlattened Ratings:")
print(flattened_ratings)

