import numpy as np

a = np.arange(12).reshape(-1,4)
print(a)

#a배열과 동일한 shape의 배열을 생성하고 0으로 채워주세요
b = np.zeros_like(a)
c = np.zeros(a.shape, dtype="int32")
print(b)
print(c)

# print(np.max(a))
# print(np.max(a,axis=0))
# print(np.max(a,axis=1))

# print(np.sum(a))
# print(np.sum(a, axis=0))
# print(np.sum(a, axis=1))



# a = np.zeros([3,4], dtype="int32")
# print(a)


# a = np.zeros(3, dtype="int32")
# print(a)
#
# b = np.ones(10)
# print(b)


