#범위의 값을 모두 더하는 것
array = [3,5,1,2,4]
summary = 0
for x in array:
    summary += x
print(summary)

# i안의 범위와 j안의 범위를 곱한 값
array = [3,5,1,2,4]
for i in array:
    for j in array:
        temp = i * j
        print(temp)


import time
start_time = time.time()


end_time = time.time()
print("time:" , end_time - start_time)


a = 0.3+0.6
print(round(a,4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)
    

a= [1,2,3,4,5,6,7,8,9]
print(a)
print(a[3])
n= 10
a= [0] * n
print(a)


a= [1,2,3,4,5,6,7,8,9]
print(a[7])
print(a[-1])
print(a[-3])
a[3] = 7
print(a)


a= [1,2,3,4,5,6,7,8,9]
print(a[3])
print(a[1 : 4])



array = [i for i in range(10)]
print(array)


array = [i for i in range(20) if i % 2 == 1]
print(array)
array = [i * i for i in range(1, 10)]
print(array)
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)


n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

summary = 0
for i in range(1, 10):
    summary += i
print(summary)

for _ in range(5):
    print("hello world")


a=[1, 4, 3]
print(a)
a.append(2)
print(a)
a.sort()
print(a)
a.sort(reverse = True)
print(a)


a=[4,3,2,1]
a.reverse()
print(a)
a.insert(2,3)
print(a)
print(a.count(3))
a.remove(1)
print(a)

a=[1,2,3,4,5,5,5]
remove_set = {3,5}
result = [i for i in a if i not in remove_set]
print(result)


data = 'Hello world'
print(data)
data = "Don't you know \"Python\"?"
print(data)

a= "Hello"
b= "World"
print(a+ " " + b)
a="string"
print(a*3)
a="ABCDEF"
print(a[2:4])

a=(1,2,3,4,5,6,7,8,9,)
print(a[3])
print(a[1:4])


data = dict()
data['사과'] = 'Apple'
data['바나나'] ='Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")


data = dict()
data['사과'] = 'Apple'
data['바나나'] ='Banana'
data['코코넛'] = 'Coconut'

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])


data = set([1,1,2,3,4,4,5])
print(data)
data = {1,1,2,3,4,4,5}
print(data)


a=set([1,2,3,4,5])
b=set([3,4,5,6,7])
print(a | b)
print(a & b)
print(a - b)


data = set([1,2,3])
print(data)

data.add(4)
print(data)
data.update([5,6])
print(data)
data.remove(3)
print(data)


n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)

n,m,k = map(int,input().split())
pirnt(n,m,k)


import sys

data = sys.stdin.readline().rstrip()
print(data)


a = 1
b = 2
print(a,b)
print(7, end=" ")
print(8, end=" ")

answer = 7
print("정답은 "+str(answer)+"입니다")


x = 15

if x >= 10:
    print("x >=10")
if x >= 0:
    print("x >=0")
if x >= 30:
    print("x >=30")


score = 85

if score >=90:
    print("A학점")
elif score >=80:
    print("B학점")
elif score >=70:
    print("C학점")
else:
    print("F학점")


i = 1
result = 0
while i <= 9:
    result += i
    i += 1

print(result)


array = [9,8,7,6,5]

for x in array:
    print(x)


result = 0

for i in range(1, 10):
    result += i

print(result)

result = 0
for i in range(1, 31):
    result += i
print(result)

result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(result)

i = 1

while True:
    print("현재 i의 값:", i)
    if i == 5:
        break
    i += 1

scores= [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i+1 , "번 학생은 합격입니다.")

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i+1 ," 번 학생은 합격입니다.")


#구구단

for i in range(2,10):
    for j in range(1,10):
        print( i, "X", j, "=" , i*j)
    print()
    
for i in range(1,10):
    for j in range(1,10):
        print( i, "X", j, "=", i*j)
    print()








































































































