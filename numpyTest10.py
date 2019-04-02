import numpy as np


#bool array
#index array


a = np.arange(12).reshape(-1, 4)
print(a)




# # print(a[:][1])   #모든행의 1열을 뽑아 오는 것이 아닙니다. 모든 행을 뽑아 와서 그중에 1행만 뽑아와요.
# print(a[:,1])      #모든행의 1열만 뽑아 와요.
#
# print(a[0,0])
# print(a[0:1,0])



# 연습)
# for문을 이용하여 행과 열을 바꿔서 출력해 봅니다.
'''
0 4 8
1 5 9
2 6 10
3 7 11
'''

# print(a[:,0])
# print(a[:,1])
# print(a[:,2])
# print(a[:,3])

# for i in range(4):
#     print(a[:,i])
#
# b = a.transpose()       #행,열를 바꿔 새로운 배열을 생성합니다.
# print(b)



# 연습)
# 테두리가 1로 채워지고 속은 0으로 채워지는 5*5배열을 만들어 봅니다.
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1


# a = np.ones([5,5],dtype="int32")
# a[1:4,1:4] = 0
# print(a)
#



# print(a[::])
# print(a[::-1])


#연습
#행도 거꾸로 열도 거꾸로 출력 해 봅니다.
# print(a[::-1][::-1])
# print(a[::-1,::-1])                 #fancy Indexing


# print(a)
# print(a[:])             #모든행을 보여주세요
# print(a[:][1])          #모든행의 1열을 보여 주세요
# print(a[:][1:3])        #모든행의 1열부터 3-1열까지 보여주세요



# print(a[0])
# print(a[1:])
# print(a[0][0])              # 맨첫번째행의 첫번째 열
# print(a[-1][-1])            # 마지막행의 마지막 열
# print(a[1][2])                # [행][열]
# print(a[1])                   #[행]
# print(a[1:3])                #[1:3]     1행부터 3-1행까지
#


# b = np.zeros_like(a)
# print(b)
#
# c = np.ones_like(a)
# print(c)
#
# d = np.full_like(a, 100)
# print(d)


# print(np.cumsum(a))
# print(np.cumsum(a,axis=0))
# print(np.cumsum(a,axis=1))


# print(np.sum(a))
# print(np.sum(a, axis=0))
# print(np.sum(a, axis=1))






# 배열을 0으로 채워주세요             zeros
# 배열을 1로 채워주세요              ones
# 0,1 이외의 다른값으로 채워주세요   full

# a = np.zeros(10, dtype=np.int32)
# b = np.ones(10, dtype=np.int32)
# c = np.full(10,3)
#
# print(a)
# print(b)
# print(c)


# a = np.zeros([3,4],dtype=np.int32)
# b = np.ones([3,4],dtype=np.int32)
# c = np.full([3,4],100)
# print(a)
# print(b)
# print(c)












