# SESSION 1 - Introduction to NumPy

# Task 1 - Create a Python List and NumPy Array

# NumPy library ko import kar rahe hain.
import numpy as np

# 1 se 1000 tak numbers ki Python list bana rahe hain.
python_list = list(range(1, 1001))

# 1 se 1000 tak numbers ka NumPy array bana rahe hain.
numpy_array = np.array(range(1, 1001))

# Dono data structures ko display kar rahe hain.
print("Python List:")
print(python_list)

print("\nNumPy Array:")
print(numpy_array)


# Task 2 - Compare Memory Usage of List and NumPy Array

# Memory calculate karne ke liye NumPy aur sys ko import kar rahe hain.
import numpy as np
import sys

# 1000 integers ki ek list aur ek NumPy array bana rahe hain.
python_list = list(range(1, 1001))
numpy_array = np.array(range(1, 1001))

# sys.getsizeof() Python list object ka memory size bytes mein deta hai.
list_memory = sys.getsizeof(python_list)

# nbytes NumPy array ke actual data ka memory usage batata hai.
array_memory = numpy_array.nbytes

# Memory usage ko bytes mein print kar rahe hain.
print("Python List Memory:", list_memory, "bytes")
print("NumPy Array Memory:", array_memory, "bytes")


# Task 3 - Compare List and NumPy Array Execution Time

# NumPy aur time module ko import kar rahe hain.
import numpy as np
import time

# Dono examples ke liye 10,000 integers bana rahe hain.
python_list = list(range(1, 10001))
numpy_array = np.array(range(1, 10001))

# Python list ke har element mein 5 add karne ke liye function bana rahe hain.
def add_five_list(data):
    return [value + 5 for value in data]

# NumPy array ke har element mein 5 add karne ke liye function bana rahe hain.
def add_five_array(data):
    return data + 5

# Python list ko execute hone mein kitna time laga, woh measure kar rahe hain.
start_time = time.perf_counter()
list_result = add_five_list(python_list)
list_time = time.perf_counter() - start_time

# NumPy array ko execute hone mein kitna time laga, woh measure kar rahe hain.
start_time = time.perf_counter()
array_result = add_five_array(numpy_array)
array_time = time.perf_counter() - start_time

# Dono methods ka execution time print kar rahe hain.
print("Python List Time:", list_time, "seconds")
print("NumPy Array Time:", array_time, "seconds")


# Task 4 - Compare Loop and Vectorized Operations

# NumPy library ko import kar rahe hain.
import numpy as np

# Restaurant ratings ka NumPy array bana rahe hain.
ratings = np.array([4, 5, 3, 4, 5])

# Loop method mein har rating ko 2 se multiply kar rahe hain.
loop_result = []
for rating in ratings:
    loop_result.append(rating * 2)

# Vectorized method mein poore array ko ek saath 2 se multiply kar rahe hain.
vectorized_result = ratings * 2

# Dono results ko display kar rahe hain.
print("Loop Result:", loop_result)
print("Vectorized Result:", vectorized_result)

# Vectorization se har element ke liye alag Python loop likhne ki zarurat nahi hoti.

