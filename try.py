import random
import numpy as np


arr1 = np.random.normal(1, 1, 10)
arr2 = np.random.normal(1,1, (10,20))
print(arr1, arr2)

arr1inds = arr1.argsort()
sorted_arr1 = arr1[arr1inds[::-1]]
sorted_arr2 = arr2[arr1inds[::-1]]
print(sorted_arr1,sorted_arr2)