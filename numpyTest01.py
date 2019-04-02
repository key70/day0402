import numpy as np

a = [0,1,2,3,4,5]
arr = np.array(a)
print(arr)


arr2 = arr.reshape(2,3)
print(arr2)


print(arr.shape)
print(arr2.shape)


print(arr.ndim)
print(arr2.ndim)


print(arr.dtype)
print(arr2.dtype)





# b = np.arange(5)
#
#
# c = np.array(a)
# print(c)
# print(type(c))



# print(a)
# print(b)
#
# print(type(a))
# print(type(b))