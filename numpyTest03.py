import numpy as np

#다른 자료형으로의 배열을 생성!
#정수형의 파이썬 배열 ==> 실수형 numpy 배열 생성
# np.array(파이썬배열, dtype="새로운자료형")

# a = [0,1,2,3,4,5]
a = [0,1,2,'3',4,5]
a = [0,1,2,'안녕',4,5]        #불가능
b = np.array(a, dtype='float64')
print(b)