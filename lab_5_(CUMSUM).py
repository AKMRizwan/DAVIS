#  print("**********    CUMSUM FUNCTION     ****************")

import numpy as np
def cumsum(arr):
    result = np.zeros_like(arr, dtype=float)  
    result[0] = arr[0]  
    for i in range(1, len(arr)):
        result[i] = result[i - 1] + arr[i]
    return result


arr3 = np.array([10, 20, 90, 25, 6, 2])
print("Original array:", arr3)
print("Cumulative sum:", cumsum(arr3))
