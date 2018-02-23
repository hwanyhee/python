#-*- coding: utf-8 -*-
f = open('test.txt', 'w',encoding='utf8')
name = input('이름을 입력하세요?\n')

f.write(name)
f.close()

f = open('test.txt', 'r',encoding='utf8')
name=f.readlines()
print(name)
f.close()