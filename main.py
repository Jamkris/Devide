#=======================승현================================
'''
import numpy as np

result = []
#입력
#list1 = list(map(int,input().split(' ')))
list1 = [2, -5, -1, 4]  #나뉠 값
#list2 = list(map(int,input().split(' ')))
list2 = [1, -3]  #나눌 값
result = []  # 몫

#자리수 맞추기
for i in range(len(list1) - len(list2)):
  list2.append(0)

#넘파이 변환
arr1 = np.array(list1)
arr2 = np.array(list2)

#자리수 맞추고 빼줌
first = list1[0]  #몫 x제곱부분
list3 = list(arr1 - (list1[0] * arr2))  # result
arr3 = np.array(list3)

#자리수 맞추기
list2.pop()  # 뒷부분 삭제
list3.pop(0)  # 앞부분 0 삭제

#첫번째 뺄셈
second = list1[0]  #몫 x부분
arr3 = list(arr3 - (list1[0] * arr2))  # result

#넘파이 변화
arr3 = np.array(list3)
arr2 = np.array(list2)

arr4 = list(arr3 - (list2[0] * arr2))  #나머지

print(f'몫 : {first} {second})
print(f'나머지 : {arr4}')

'''
#=======================규민================================
import numpy as np

list1 = list(map(int, input().split(' ')))  # 나뉠 수
list2 = list(map(int, input().split(' ')))  # 나눌 수
# list1 = [2, -5, -1, 4]  #나뉠 값
# list2 = [1, -3]  #나눌 값
list3 = []  # 값
반복 = len(list1) - len(list2)
# 자리수 맞추기
for _ in range(반복):
	list2.append(0)
print("list2:", end="")
print(list2, end="\n\n")
# arr은 append 등의 함수를 먹지 않음
arr1 = np.array(list1)
arr2 = np.array(list2)

for i in range(반복):
	list3.append(arr1[i])
	list1 = arr1 - (arr2 * arr1[i])  # x^2빼기
	list2.pop()
	list2.insert(0, 0)

	arr1 = np.array(list1)
	arr2 = np.array(list2)
	print("list1:", end="")
	print(list1)
	print("list2:", end="")
	print(list2, end="\n\n")

list1 = arr1 - (arr2 * arr1[반복])  # x^2빼기
print("list1:", end="")
print(list1)
print("list2:", end="")
print(list2, end="\n\n")

print("몫:", list3)
print("나머지:", list1[-1])
#=======================챗 GPT================================
'''
import numpy as np

list1 = list(map(int, input().split(" ")))
list2 = list(map(int, input().split(" ")))
# 분자 다항식의 계수를 정의합니다. (x^3 + 2x^2 - 5x + 6)
numerator = np.array(list1)

# 분모 다항식의 계수를 정의합니다. (x - 1)
denominator = np.array(list2)

# np.polydiv() 함수를 사용하여 다항식을 나눕니다.
quotient, remainder = np.polydiv(numerator, denominator)

# 결과를 출력합니다.
print("나눗셈의 몫:", quotient)
print("나눗셈의 나머지:", remainder)'''
