import numpy as np

a = ['160.7','180.5','145.8','175.5','170.7','165.8']


# 연습)
# 파이썬 배열을 numpy 배열로 만든 후
# 170이상 데이터 뽑아 새로운 numpy배열을 만들어 봅니다.
arr1 = np.array(a, dtype='float64')
arr2 = arr1[arr1>170]
print(arr2)