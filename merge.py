# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
import numpy as np
def mergemm(a,b):
    print(a[0], b[0])
    x = []
    if a[0] < b[0]:
        x = np.append(a,b)
    elif a[0] >= b[0]:
        x = np.append(b,a)
    return x
    
