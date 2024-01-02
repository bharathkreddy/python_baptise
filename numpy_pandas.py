# %%
import math
import numpy as np

a = np.zeros(5)
print(a, a.dtype)

a = np.zeros(5, dtype=int)
print(a, a.dtype)

a = np.zeros((3,4), dtype=np.uint8)
print(a, a.dtype)

a = np.ones((2,3), dtype=np.float32)
print(a, a.dtype)

a = np.full((3,4), 42, dtype=np.uint8)
print(a, a.dtype)

a = np.eye(5, dtype=np.uint16)
print(a, a.dtype)

# if the numbers do not fit into dytype then we get weird results
a = np.arange(2, 11, 2, dtype=np.uint8)
print(a, a.dtype)

# if we specify dtype as int, then floats would get truncated
a = np.linspace(2, 9, num=6, dtype=np.float16)
print(a, a.dtype)

x_coords = np.linspace(-2 * math.pi, 2 * math.pi, 50)
print(x_coords)

# This is random module INSIDE numpy and not random module
np.random.seed(42)

print(np.random.random(5))
print(np.random.random((2,3)))
print(np.random.rand(4,2))
print(np.random.randint(1, 10, 5))

# Simulate 2 dies, 10 throws each
print(np.random.randint(1, 7, (10,2)))


# %%
# RESHAPING ARRAYS
arr = np.arange(12)
print(arr , arr.shape)

# reshaping and reading elements
m1 = arr.reshape(3,4)
print(m1 , m1.shape, m1[1][2])

# Changing arr modifies m1, as slots point to same objectect, and are just arranged in a diff way
arr[0] = 100
print(arr , arr.shape)
print(m1 , m1.shape)

# copying breaks the link
m3 = arr.reshape(6,2).copy()
arr[0] = 999
print(arr, m3)

# %%
# STACKING ARRAYS
a1 = np.arange(1, 6)
print(a1)
a2 = np.arange(1, 11).reshape(2,5)
print(a2)

# pass the arrays to be stacked as a tupple or list
s1 = np.vstack((a1, a2))
print(s1)

# numpy will adjust dtypes when stacking diff types
a1 = np.arange(1, 6)
a2 = np.random.random(10).reshape(2,5).round(2)
s1 = np.vstack((a1, a2))
print(s1)
print(s1.dtype)

a1 = np.arange(0, 6).reshape(3,2)
a2 = np.random.random(15).reshape(3,5).round(2)
s1 = np.hstack((a1, a2))
print(s1)
print(s1.dtype)

# Stacking does not reference original objects. It copies and creates a new object
a1[0][1] = 99
print(a1)
print(s1)

# %%
# SLICING AND INDEXING
a = np.arange(1, 10).reshape(3,3)

# We want to slice it in two axes
print(a[1:,1:3])

# Slicing also support steps.
a = np.arange(1, 26).reshape(5,5)
print(a[:5:2, ::2])

# NOTE: Slices are linked to original Array, even if reshaped, unless STACKED.
a = np.arange(1, 10)
# when a scalar is provided, it is broadcasted into shape and size needed
a[::2] = 99
print(a)
# %%
# FANCY INDEXING
# What if we want to pick rows 1,2 and 4 ?
a = np.arange(1,11)
index_array = np.array([1,2,4])
print(a, '\n', a[index_array])

# %%
# Shape of index_array determines shape of output
a = np.arange(1, 26).reshape(5,5)
index_array_1 = np.array([1,2,4])
index_array_2 = np.array([0,3])

print(a)
print('Array\n\n')

print(a[1, index_array_1])
print('index & fancy\n\n')

print(a[index_array_1, 2])
print('fancy & index\n\n')

print(a[1:3, index_array_1])
print('slice & fancy\n\n')

print(a[:, np.array([0,3])])
print('Isolate columns\n\n')

print(a[np.array([1,4]), :])
print('isolate rows\n\n')

print(a)
print('Array\n\n')

print(a[np.array([0,2]), np.array([1, 3])])
print('fancy & fancy\n')
print('Think of this as a a zip of 2 index arrays - giving elements at positions : (0, 1) & (2, 3)\n\n')

print(a[np.array([0,2]), np.array([1])])
# %%
# MASKING 

arr = np.array([10, -10, 20, -20, 30, -30])
print(arr)
mask = arr > 0
print(mask)
print(arr[mask])
print(arr[arr < 0])
print(arr[abs(arr)> 15])

# How to add logic (and:&, or:|, negation:~)
print('\n\n')
arr = np.arange(-10, 11)
print(arr)
print(arr[(arr > 0) & (arr %2 == 0)])
print('\n\n')


# %%

# Masking 2-D Arrays
# mask allways returns 1-D array as there might be diff elements from each dimention matching mask
arr = np.array([
    [1, 2],
    [3, 4]
], dtype=np.uint8)

print(arr)
print('\n\n')
print(arr != 3)
print('\n\n')
print(arr[arr != 3])


# %%
import csv
with open('python-fundamentals-main/31 - Matplotlib/05 - Charting with mplfinance/AAPL_data.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list(reader)


print(header)
print(data)

arr = np.array(data)
print(arr)
# String d-type
print(arr.dtype)

ohlc = np.array(arr[:,1:5]).astype(np.float64)

# print first 15 rows
print(header[1:5])
print(ohlc[:15,:])

# i want to find dates on which APPL closed higher than opening
# Step1: create a mask
mask = ohlc[:,3] > ohlc[:,0]

# Step2: Apply mask on Dates
dates = np.array(arr[:,0])

# Step3: Hstack these two.
s = np.hstack((dates[mask].reshape(651,1), ohlc[mask]))
print(s)
# %%
# numpy has many universal functions which are vectorised.
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(np.add(a, b))

# Broadcast
print(np.add(a, 10))
print(b / 10)

print(b **2)

# %%

# PERFORMANCE
from time import perf_counter

l = list(range(1, 10_000_000))

print('Calculating Pef of calc. inverse of each element in a list')
start = perf_counter()
new_list = []
for el in l:
    new_list.append(1 / el)
end = perf_counter()
print(f'Loop time: {end - start}')

start = perf_counter()
new_list = [ 1 / el for el in l]
end = perf_counter()
print(f'Comprehension time: {end - start}')

np_list = np.array(l)
start = perf_counter()
new_arr = 1 / np_list
end = perf_counter()
print(f'Numpy time: {end - start}')

# %%

# PANDAS
