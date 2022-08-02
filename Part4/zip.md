# 📚 zip 함수
+ 2개 이상의 반복가능한 자료형(iterable 리스트이나 튜플 자료형)을 원소끼리 묶어주는 함수(packing) 
```python
mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)
```

>(1, 40)<br>
(2, 50)<br>
(3, 60)<br>

### 🔗 여러 개의 iterable을 동시 순회
```python
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]

answer = []
for number1, number2, number3 in zip(list1, list2, list3):
   print(number1 + number2 + number3)
```

### 🔗 Key 리스트와 Value 리스트로 딕셔너리 생성하기
+ 파이썬의 zip 함수와 dict 생성자를 이용하면 코드 단 한 줄로, 두 리스트를 합쳐 딕셔너리로 만들 수 있음
```python
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```

### 🔗 Unpacking(*)
+ 두 개로 묶었던 리스트들은 별표(*)와 zip() 함수를 이용하면 해체 가능
> zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만듭니다.<br>
튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.

```python
#인자 해체하기
pairs = [('a', 1), ('b', 2), ('c', 3)]
tuple1, tuple2= zip(*pairs)
print(tuple1, tuple2)
```

> ('a', 'b', 'c') (1, 2, 3)
