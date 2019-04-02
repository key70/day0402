import numpy as np

a = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]
arr = np.array(a)
arr2 = arr.flatten()
print(arr2)             #차수와 상관없이 무조건 1차원 만들어 줍니다.



# a = [4,3,1,5,2,2,5,5]
# arr1 = np.array(a)
# r = np.max(arr1)
# idx = np.argmax(arr1)
# print(r)
# print(idx)

#연습)
#점수가 가장 높은 학생의 이름을 출력해 봅니다.
# name = np.array(['차범근','홍길동','강감찬','이순신','유관순','박주호', '문재인'])
# score = np.array([100,80,90,100,70,95,100])
# n = np.argwhere(score==np.amax(score))
# n = n.flatten()
# # n  = n.reshape(1,3)[0]
# print(name[n])



# n = np.argmax(score)        #최고점수인 학생 한명만 뽑아와요
# print(name[n])





# #연습)
# name = ['홍길동','강감찬','이순신','유관순','박주호','김경민', '문재인']
# score = [80,90,100,70,100,95,100]
#
# #성적순으로 이름을 출력해 봅니다.
# arr_name = np.array(name)
# arr_score = np.array(score)
#
# a = np.argsort(arr_score)[::-1]
# #[3,0,1,4,2]
# #[2,4,1,0,3]
# print(a)
# print(arr_name[a])


# a = [4,3,1,5,2]
# # [2,4,1,0,3]
# arr1 = np.array(a)
# #정렬을 하면 몇번째 요소부터 순서대로 오는지 배열을 생성해줘
#
# b = np.argsort(arr1)
# print(b)
# print(arr1[b])
#


# arr1.sort()         #배열의 요소를 정렬 해 줍니다.
# print(arr1)






# a = [1,3,0,3,1]
# b = np.eye(len(a),np.max(a)+1, dtype="int32")[a]
# print(b)


# a = np.eye(5,5, dtype="int32")
# print(a)

# a = np.zeros([5,5], dtype="int32")
# # a[[0,1,2,3,4],[0,1,2,3,4]] = 1
# # a[range(5) ,range(5)] = 1
# print(a)





# a = [1,3,0,3,1]
# # 연습)
# # a배열의 요소만큼의 행의 크기를 갖고 a배열의 요소중에 최대값+1의 열의 크기를 갖는
# # 0으로 채워진 2차원 배열을 만들고
# # 각 행마다 a배열의 요소에 해당하는 열에 1을 채웁니다.
#
# '''
# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 0 1
# 0 1 0 0
# '''
#
# b = np.zeros([len(a),np.max(a)+1], dtype="int32")
# # b[[0,1,2,3,4],[1,3,0,3,1]] = 1
# # b[[0,1,2,3,4],a] = 1
# b[[range(5)],a] = 1
# print(b)


# # 연습)
# # 0으로 채워진 5*5 배열을 만들고 대각선을 1로 만드세요
# '''
# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1
# '''
# a = np.zeros([5,5],dtype="int32")
# a[[0,1,2,3,4],[0,1,2,3,4]] = 1
# print(a)





# 연습)
# 테두리가 1로 채워지고 속은 0으로 채워진 5*5배열을 만들어 봅니다.
# indexArray를 이용해 봅니다.
# a = np.ones([5,5], dtype="int32")
# a[1:-1 , 1:-1] = 0
# print(a)


# a = np.zeros([5,5], dtype="int32")
# print(a)
#
# a[:,[0,-1]] = 1
# a[[0,-1], :] = 1
# print(a)




# a = np.arange(12).reshape(-1,4)
# print(a)
# #        행 행 열 열
# print(a[[1, 0],[0,1]])         #index Array
# a[[1,0],[0,1]] = 100
# print(a)

# #       행 열
# # print(a[0, 1])       #0번째 행의 1번째 열
# # print(a[0])         #0번째 행
# print(a[[0,1]])       #0번째행, 1번째행
# print(a[[1,0]])       #0번째행, 1번째행           index Array

# print(a>5)
# print(a[a>5])           #bool Array

