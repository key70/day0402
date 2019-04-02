import numpy as np

# 결론
# 차원이 다른 것 끼리 연산이 가능하려면
# 열의 수가 중요하며
# 두개의 배열의 열의 수를 동일하게 하거나
# 열의 수를 하나짜리로 만들어
# 연산을 수행한 후
# 원하는 차원으로 다시 만든다.



# 연습)
# 5개의 배열을 서로 덧셈을 실행해 봅니다.
a = np.arange(3)  #[0 1 2]
b = np.arange(6)  #[0 1 2 3 4 5]
c = np.arange(3).reshape(-1,3)  #[[0,1,2]]
d = np.arange(6).reshape(-1,3)  #[[0 1 2][3 4 5]]
e = np.arange(3).reshape(3,-1)  #[[0] [1] [2]]

print(d+e)     #불가능

# print(c+e)      #broadCasting
# print(c+d)          #broadCasting, vectorOperation


# print(b+e) #[[0,1,2,3,4,5],[1,2,3,4,5,6],[2,3,4,5,6,7]]

# print(b+d)  #오류
# print(b+c)  #오류
# print(a+e)  #[[0 1 2][1 2 3][2 3 4]]            VectorOperation, VectorOperation
# print(a+b)    # 오류
# print(a+c)      # vector operation  [[0 2 4]]
# print(a+d)
# [[0 2 4][3 5 7]]    broadCasting, vector operation
# a는 일차원배열이고
# b은 이차원배열 끼리 연산을 수행하였더니
# a배열의 b배열의 행만큼 연산을 수행====> broad Casting
# a밸의 요소 하나하나가 b배열의 각 행의 열과 대응하여 연산 ===> vector operation



# print(a)
# print(b)
# print(c)
# print(d)
# print(e)







# c = a + b             #ValueError: operands could not be broadcast together with shapes (3,) (6,)
# print(c)

# b = np.arange(3)
#
# c = a + b               #vector operation
# print(a)
# print(b)
# print(c)

