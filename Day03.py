import math

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if a + b > c and b + c > a and a + c > b:
	print('周长：%f' % (a + b + c))
	p = (a + b + c) / 2
	area = math.sqrt(p * (p -a) * (p - b) * (p -c))
	print('面积：%f' % area)
else:
	print('不构成三角函数')