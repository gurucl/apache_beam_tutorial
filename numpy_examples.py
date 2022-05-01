import numpy as np
import sys
import time

# a = np.array([1,2,3])
# print(a)
#
# b = np.array(([1,2,3],[4,5,6]))
# print(b)

# --------------------------------------------------------------------------------
# s = range(1000)
# print(len(s))
# print(sys.getsizeof(5)*len(s))
#
# ns = np.arange(1000)
# print(len(ns))
# print(ns.size * ns.itemsize)
#
# [print(i) for i in enumerate(r)]

# --------------------------------------------------------------------------------

# size = 100000
# l1 = range(size)
# l2 = range(size)
#
# ar1 = np.arange(size)
# ar2 = np.arange(size)
#
# start = time.time()
# # print(start)
# result = [(x + y) for x,y in zip(l1,l2)]
# # print(result)
# print((time.time()-start)*1000)
#
# start = time.time()
# result1 = ar1 + ar2
# # print(result1)
# print((time.time()-start)*1000)

# --------------------------------------------------------------------------------

# a = np.array(([1,2,3],[4,5,6]))
#
# print(a.ndim)
# print(a.itemsize)
# print(a.dtype)
# print(a.size)
# print(a.shape)

# --------------------------------------------------------------------------------

# a = np.array(([1,2,3,4],[5,6,7,8]))
# print(a)
# print(a.size)
# print(a.shape)
# print(a.ndim)
# print(a.itemsize)
# print(a.reshape(4,2))
# print(a[:1,3])

# --------------------------------------------------------------------------------

a = np.array(([1,2,3,4],[5,6,7,8]))
b = np.array(([1,2,3,4],[5,6,7,8]))
print(a)
print(a)
print(a+b)
print(a*b)



