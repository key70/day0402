import numpy as np

b =  np.arange(6).reshape(-1,3)
# b =  np.arange(6).reshape(2,-1)
# b =  np.arange(6).reshape(2,3)

print(b)
print(b + 1)
print(b>1)          # BroadCasting   b의 요소만큼 비교하여 True, False를 반환
print(b[b>1])       # BoardCasting의 True요소만 출력
# print(b[0][0])


# a = np.arange(3)
# print(a)
# print(a+1)          #broadCasting
# print(a>1)          #broadCasting
# print( a[a>1])