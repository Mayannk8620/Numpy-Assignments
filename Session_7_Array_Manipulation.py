# SESSION 7 - Array Manipulation

# Task 1 - Concatenate Zomato and Swiggy Ratings

# NumPy library ko import kar rahe hain.
import numpy as np

# 5 Zomato restaurants ki ratings ka array bana rahe hain.
zomato_ratings = np.array([4.2, 4.5, 3.8, 4.1, 4.6])

# 5 Swiggy restaurants ki ratings ka array bana rahe hain.
swiggy_ratings = np.array([4.0, 4.3, 3.9, 4.4, 4.7])

# Dono arrays ko ek array mein combine kar rahe hain.
all_ratings = np.concatenate((zomato_ratings, swiggy_ratings))

# Print the combined ratings.
print("Combined Restaurant Ratings:", all_ratings)


# Task 2 - Stack Weekly Instagram Likes Vertically

# NumPy library ko import kar rahe hain.
import numpy as np

# 3 Instagram posts ke weekly likes store kar rahe hain.
post_1 = np.array([120, 150, 180, 200, 220, 240, 260])
post_2 = np.array([100, 130, 160, 190, 210, 230, 250])
post_3 = np.array([140, 170, 200, 230, 250, 270, 300])

# Arrays ko vertically stack kar rahe hain, jisse har row ek post ko represent karegi.
weekly_likes = np.vstack((post_1, post_2, post_3))

# Print the stacked array.
print("Weekly Likes:")
print(weekly_likes)


# Task 3 - Split Product IDs Into Five Parts

# NumPy library ko import kar rahe hain.
import numpy as np

# 12 product IDs ka array bana rahe hain.
product_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112])

# Array ko 5 almost equal parts mein divide kar rahe hain.
parts = np.array_split(product_ids, 5)

# Har part aur uski shape display kar rahe hain.
for number, part in enumerate(parts, start=1):
    print("Part", number, ":", part)
    print("Shape:", part.shape)


# Task 4 - Add and Delete a User in a WhatsApp Group

# NumPy library ko import kar rahe hain.
import numpy as np

# Har row ek user ko aur har column ek din ko represent karta hai.
messages = np.array([
    [10, 12, 8, 15, 9, 11, 14],
    [5, 7, 6, 8, 10, 9, 12],
    [20, 18, 22, 19, 25, 21, 24]
])

# New user ke weekly messages ko ek new row ke roop mein add kar rahe hain.
new_user = np.array([[8, 10, 9, 12, 11, 13, 15]])
messages_with_new_user = np.vstack((messages, new_user))

# Updated array se second user ki row delete kar rahe hain.
messages_after_delete = np.delete(messages_with_new_user, 1, axis=0)

# Print the arrays.
print("After Adding New User:")
print(messages_with_new_user)

print("\nAfter Deleting Second User:")
print(messages_after_delete)


# Task 5 - Demonstrate View and Copy

# NumPy library ko import kar rahe hain.
import numpy as np

# YouTube video views ka array bana rahe hain.
views = np.array([1000, 2000, 3000, 4000])

# view() original array ke same data ko share karta hai.
views_view = views.view()

# copy() data ki independent copy banata hai.
views_copy = views.copy()

# Dono arrays ke first element ko modify kar rahe hain.
views_view[0] = 9999
views_copy[0] = 5555

# View mein change karne se original array bhi change hota hai.
print("Original Array after View Modification:", views)

# Copy mein change karne se original array change nahi hota.
print("Copied Array:", views_copy)

