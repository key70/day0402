import numpy as np




a = [1,2,3,4,5]
b = [1.0, 2.0, 3.0, 4.0, 5.0]
c = ['a','b','c','d','e', 'hello', '우리나라 대한민국', '이순신 우리나라 대한민국 우리나라 대한민국 우리나라 대한민국']
d = ['hello', 'java', 'python', 'oracle', 'mongo']
e = ['김경민', '오상훈', '이성기', '김도희', '정연미']


arr1 = np.array(a)
arr2 = np.array(b)
arr3 = np.array(c)
arr4 = np.array(d)
arr5 = np.array(e)


print(arr1.shape)   # (5,)      1차원이면서 데이터의 수가 5개
print(arr1.ndim)    # 1         1차원
print(arr1.dtype)   # int32     요소하나를 위한 자료형이 int32





print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
print(arr5.dtype)

