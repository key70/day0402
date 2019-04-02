import numpy as np

name = ['박자바','김파이','홍프링','이프로','정서버',"정프로"]
score = [80,90,100,70,95,100]

# 성적순으로 정렬하기
n = np.argsort(score)[::-1]
print(np.array(name)[n])

# 최고 점수 학생 리스트 : 최고값 중복으로 되는 경우 사용하는 방법
s = np.array(score)
a = np.argwhere(s==np.max(s))
names = (np.array(name)[a]).reshape(1,-1)[0]
# names = (np.array(name)[a]).flatten().tolist()
print(names)