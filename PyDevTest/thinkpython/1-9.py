'''
1.9 연습문제
'''
# 1. print 문에서 괄호 하나를 없애거나 두 괄호를 모두 없애면 어떻게 될까?
# 에러가 난다.
from math import pi

def abc():
    print('abc 입니다')
     


try:
    
    print('fff', 3/0)
except Exception as ex: # 에러 종류
    print('에러가 발생 했습니다', ex) # e

# 2. 문자열을 출력하려고 할 때 따옴표 하나를 없애거나 둘 다 없애면 어떻게 될까?
# 에러가 난다.
print('123')

#3. - 기호를 사용해서 -2 같은 음수를 만들 수 있다. 숫자 앞에 + 기호를 넣으면 어떻게 될까? 2++2는 어떻게 될까?
# 2++2 = 2 + (+2) 처럼 된다.
# 2+-2 = 2+(-2) 가 된다.
print( 2++2)
print(2+-2)

# 4. 수학 표기에서는 02처럼 앞자리를 0으로 채워도 괜찮다. 파이썬에서 이렇게 하면 어떻게 될까?
# 오류가 발생한다.
# print(02)

# 5. 두 값 사이에 연산자가 없다면 어떻게 될까?
# 에러가 발생된다.
# print( 2 2 )

# 6. 42분 42초는 모두 몇 초인가?
# 2562초
m = 42
s = 42
ts = 42 * 60 + s
print('전체초 : ',ts)

# 7. 10킬로미터는 몇 마일인가? 힌트: 1마일은 1.61킬로미터
# 6.2 마일
km = 10
mile = 1.61
w = km / mile
print(w)

# 8. 10킬로미터 경주를 42분 42초로 뛰었다면 평균 속도는 얼마인가?(마일당 시간을 분과 초로 표기) 
# 시간당 마일로 표기했을 때 평균 속도는 얼마인가?
a= 10 / 1.61
b = 2562 / 6.21
print(a)
print(b * 60)

import math as a
print( a.pi ** a.pi )
