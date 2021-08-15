'''
#replace
a = 'Hello World' 
a= a.replace('World','Python')
print(a)
#translate
table = str.maketrans('aeiou','12345')
print('apple'.translate(table))

#split
print('apple pear grape pineapple orange'.split())
#join
print(' '.join(['apple', 'pear', 'grape', 'pineapple','orange']))
#upper
print('python'.upper())
#lower
print('PYTHON'.lower())
#lstrip , r , s
print('    Python    '.strip())
print('    Python    '.lstrip())
print('    Python    '.rstrip())
print(', python'.lstrip(',. '))
print('python , '.rstrip(',. '))
print(' ., python ,. '.strip(',. '))

#ljust,rjust(공간을 할당하고 글자를 채운 다음 남은 문자는 공백)
print('python'.ljust(10))
print('python'.rjust(10))

#center (공간을 균등하게 해서 홀수면 왼쪽이 하나더 많음)
print('python'.center(10))

#메서드 체이닝
print('python'.rjust(10).upper())

#zfill -> 0 으로 채우기
print('35'.zfill(4)) #0035
print('3.5'.zfill(6))
print('hello'.zfill(10))

#find , rfind -> 처음으로 찾는 문자열의 인덱스를 반환 없으면 -1
print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))
print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))
'''

#index , rindex
print('apple pineapple'.index('pl'))
print('apple pineapple'.rindex('pl'))