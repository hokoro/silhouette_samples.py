# -*- coding: utf-8 -*-
"""천영성 - 세_번째_과제.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_PZL9mF05B79hj7WDriAhvmJdu_cW2hd

## **00 과제 제출 예시**
아래와 같이 출력 결과와 동일한 출력을 해주시면 됩니다.
"""

# 출력 결과 : 광주 인공지능사관학교
print("광주 인공지능사관학교")

"""## **01 별 찍기(1)**
첫째 줄에 별 1개, 둘째 줄에 별 2개, ..., 열번째 줄에는 별 10개를 출력해 보세요.
"""

# 출력 결과
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

for i in range(1,11):
  for j in range(i):
    print('*',end ='')
  print('\n')

"""## **02 별 찍기(2)**
"숫자를 입력하세요"라는 입력창을 만든 후

출력 결과(1)과 출력 결과(2)를 보고 규칙을 유추하여 별을 출력해 보세요.

(입력창에 들어가는 숫자의 범위는 1부터 100까지 입니다.)
"""

#  출력 결과(1)
#  숫자를 입력하세요 3
#  1
#  *
#  2
#  *
#  **
#  3
#  *
#  **
#  ***

#  출력 결과(2)
#  숫자를 입력하세요 5
#  1
#  *
#  2
#  *
#  **
#  3
#  *
#  **
#  ***
#  4
#  *
#  **
#  ***
#  ****
#  5
#  *
#  **
#  ***
#  ****
#  *****

number = int(input('숫자를 입력하세요'))
for i in range(1,number+1):
  print(i,end = '')
  for j in range(0,i+1):
    for k in range(j):
      print('*',end = '')
    print('\n')

"""## **03 별 찍기(3)**
숫자 N(1 ≤ N ≤ 100)을 입력 받아 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 출력해 보세요.
"""

# 출력 예시

# N : 7
# *******
# ******
# *****
# ****
# ***
# **
# *

N = int(input('N :'))
for i in range(N,0,-1):
  for j in range(i):
    print('*',end = '')
  print('\n')

"""## **04 소수판별**
동쪽 끝 바다 너머 숫자들이 모여 사는 자연수 나라가 있다.

어느 날 자연수 나라에 반역자 무리가 있다는 소문이 퍼졌다.

반역자 무리의 특징은 1과 자기 자신으로만 나누어 떨어지는 수인 '소수'라는 것!

**자연수 나라의 영웅이 되어 '소수'를 찾아내자!**

변수 number_check에 "소수인가?!"라는 입력창을 만들어

입력된 숫자가 소수라면 "윽.. 분하구나..", 소수가 아니라면 "충성!!"을 출력해주세요.

~~(코드가 돌아가는데 걸리는 시간이나 성능 차이는 고려하지 않습니다.)~~

**소수 : 1과 자기 자신으로만 나누어 떨어지는 수로 2, 3, 5, 7 등이 있습니다.**
"""

# 출력 예시 (1)

# 소수인가?! 6
# No

# 출력 예시 (2)

# 소수인가?! 7
# Yes

# 아래의 함수 prime_number의 pass를 지운 후 코드를 작성해 주세요.
# 주어진 init()함수 직접 수정 불가

def prime_number(number):
  for i in range(2,number):
    if number % i == 0:
      return 'NO'
  
  return 'Yes'

def init():
  number_check = int(input('소수인가?!'))
  answer = prime_number(number_check)

  print(answer)

init()

"""## **05 함수(1)**
사칙연산인 더하기, 빼기, 곱하기, 나누기를 add, sub, mul, div라고 가정한다. 아래의 함수 calculate의 pass를 지우고 코드를 작성한 후 주어진 입력 값을 차례로 입력했을 때 출력 결과와 같은 출력을 해주세요.

(만약, 오타를 입력하면 '잘못 입력하셨습니다. 다시 입력해 주세요.'를 출력한 후 다시 시작하는 코드를 작성해 주세요.)

1) 첫 번째 입력 값 : ddd 1 2

2) 두 번째 입력 값 : mul 4 4



"""

# calculate()함수의 pass를 지운 후 코드를 작성해 주세요.
# 주어진 변수(oper, num1, num2) 및 init()함수, calculate()함수 직접 변경 불가
# 출력 결과 : 계산 할 사칙연산, 첫 번째 숫자, 두 번째 숫자를 입력해 주세요.(공백을 기준으로 분리)ddd 1 2
#           잘못 입력하셨습니다. 다시 입력해 주세요.
#           계산 할 사칙연산, 첫 번째 숫자, 두 번째 숫자를 입력해 주세요.(공백을 기준으로 분리)mul 4 4
#           16

def calculate(oper, num1, num2):
    if oper not in ('add','sub','mul','div'):
      print('잘못 입력하셨습니다.다시 입력해주세요')
      init()
    else:
      if oper in 'add':
        print(num1+num2)
      if oper in 'sub':
        print(num1-num2)
      if oper in 'mul':
        print(num1*num2)
      if oper in 'div':
        print(num1/num2)

def init():
  oper, num1, num2 = input('계산 할 사칙연산, 첫 번째 숫자, 두 번째 숫자를 입력해 주세요.(공백을 기준으로 분리)').split()
  calculate(oper, int(num1), int(num2))

init()

"""## **06 함수(2)**
아래 introduce_myself 함수 안의 pass를 지우시고 

성별이 '남자'일 경우엔 '안녕하세요 저는 정우입니다. 나이는 31이고 남자입니다. 잘 부탁드립니다!'를 출력하고, '여자'일 경우엔 '안녕하세요 저는 희선입니다. 나이는 26이고 여자입니다. 만나서 반가워요!'를 출력하는 코드를 작성하신 후 출력 결과와 동일한 출력을 해주세요. (함수에 전달되는 인자를 사용해주세요.)
"""

# introduce_myself()함수의 pass를 지운 후 코드를 작성해 주세요.
# 주어진 변수(jungwoo, heesun), init()함수, introduce_myself()함수 및 print문 직접 수정 불가
# 출력 결과 : 안녕하세요 저는 정우입니다. 나이는 31이고 남자 입니다. 잘 부탁드립니다!
#           안녕하세요 저는 희선입니다. 나이는 26이고 여자 입니다. 만나서 반가워요!

def introduce_myself(name, age, sex):
  if sex in '남자':
    return('안녕하세요 저는 '+name+'입니다.'+'나이는 '+str(age)+'이고 '+sex+'입니다. 잘부탁드립니다!')
  else:
    return('안녕하세요 저는 '+name+'입니다.나이는 '+str(age)+'이고 '+sex+'입니다. 잘부탁드립니다!')



def init():
  jungwoo = introduce_myself('정우', 31, '남자')
  heesun = introduce_myself('희선', 26, '여자')
  print(jungwoo)
  print(heesun)

init()

"""## **07 함수(3)**
아래의 medal_bag에는 광주 인공지능사관학교 학생들이 대회에 참여해 얻은 메달의 종류들이 뒤죽박죽 담겨있다. 이것을 메달 별로 몇 개가 있는지 카운트해주는 count_individual 함수와 메달 별로 카운트된 것을 딕셔너리로 만들어 주는 make_dictionary 함수가 있다. pass를 지운 후 출력 결과와 동일하게 출력하는 코드를 작성해 주시고 출력 결과와 동일한 출력을 해주세요.
"""

# 주어진 count_individual()함수, make_dictionary(), init()함수 직접 수정 불가
# 출력 결과 : {'Gold': 6, 'Silver': 4, 'Bronze': 3}

def count_individual(medal_bag):
  return medal_bag.count('Gold'),medal_bag.count('Silver'),medal_bag.count('Bronze')

def make_dictionary(gold_count, silver_count, bronze_count):
  return {'Gold':gold_count,'Silver':silver_count,'Bronze':bronze_count}

def init():
  medal_bag = ['Bronze', 'Gold', 'Gold', 'Gold', 'Silver', 'Gold', 'Gold', 'Gold', 'Silver', 'Silver', 'Silver', 'Bronze', 'Bronze']

  gold_count, silver_count, bronze_count = count_individual(medal_bag)
  medal_dict = make_dictionary(gold_count, silver_count, bronze_count)

  print(medal_dict)

init()

