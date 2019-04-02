import numpy as np

name = ['차범근','홍길동','강감찬','이순신','유관순','박주호','문재인']
score = [100,80,90,100,70,95,100]

name = np.array(name)
score = np.array(score)

tmpidx = np.argwhere(score==np.amax(score))
print(tmpidx.flatten())
idx = tmpidx.flatten()

print(name[idx])


# name = ['홍길동','강감찬','이순신','유관순','박주호','김경민', '문재인']
# score = [80,90,100,70,100,95,100]
#
# name = np.array(name)
# score = np.array(score)
# s = score.argsort()[::-1]
#
# print(name[s])
# print(score[s])
#
# print(score.argmax())

# a = [4,3,1,5,2]
# arr1 = np.array(a)
# print(arr1)
#
# arr2 = arr1.argsort()
# print(arr2)
#
# print(arr1[arr2])

# arr1.sort()
# print(arr1)

# a = np.zeros([5,5], dtype=np.int)
# print(a)
#
# a = np.eye(5,5, dtype=np.int)
# print(a)
#
# a = [1,3,0,3,1]
# b = np.eye(5,4, dtype=np.int)[a]
# print(b)

# a[range(5),range(5)]=1
# print(a)

# a = [1,3,0,3,1]
#
# arr1 = np.zeros([len(a),np.max(a)+1], dtype=np.int)
# arr1[[range(len(a))],a]=1
# print(arr1)
#
# print(type(range(5)))

# a = np.arange(12).reshape(-1,4)
# print(a)
# print("="*20)
#
# print(a[[1,0],[0,1]])   #Index Array
#
# a[[1,0],[0,1]] = 100
# print(a)
#
# a = np.ones([5,5], dtype=np.int)
# b = np.zeros([5,5], dtype=np.int)
#
# a[1:-1,1:-1] = 0
# print(a)
#
# b[:,[0,-1]]=1
# print(b)
# b[[0,-1],:]=1
# print(b)

# a = np.zeros([5,5], dtype=np.int)
# print(a)
#
# a[[0,1,2,3,4],[0,1,2,3,4]]=1
# print(a)

# print(a[0,1])
# print("="*20)
# print(a[0])
# print("="*20)
# print(a[[0,1]])
# print("="*20)
# print(a[[1,0]])
# print("="*20)
# print(a>5)
# print(a[a>5])