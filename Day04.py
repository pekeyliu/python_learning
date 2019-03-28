"""
	求100以内偶数之和，range（2,100,2）以2为步长递增
"""
import random,math
print("求100以内偶数之和，range（2,100,2）以2为步长递增")
sum = 0
for i in range(2,100,2):
	sum += i
print(sum)
"""
100以内猜数字大小
answer = random.randint(1,100)
conter = 0
while True:
	conter += 1
	number = int(input("请输入100以内的值："))
	if number > answer:
		print("猜大了")
	elif number < answer:
		print("猜小了")
	else:
		print("猜对了")
		break
print(" You totle getess %d times" % conter)
if conter > 7:
	print("you have not enough IQ")
"""

"""
	输出乘法口诀表

print("输出乘法口诀表")
for i in range(1,10):
	for j in range(1,i+1):	
		print(str(i * j)  ,end = "\t")
	print()
print()
for i in range(1,10):
	print((i-1)*"\t",end="")
	for j in range(i,10):
		print(str(i * j)  ,end = "\t")
	print()
"""
"""
	判断一个数是否为素数
num = int(input("please input a number:"))
end = int(math.sqrt(num))
is_prim = True
for x in range(2,end + 1):
	if num % x == 0:
		is_prim = False
		break
if is_prim and num != 1:
	print("The number is primes!")
else:
	print("The number is not primes.")
"""

"""
输入两个正整数计算最大公约数和最小公倍数

x = int(input('x = '))
y = int(input('y = '))
if x > y:
	(x, y) = (y, x)
for factor in range(x, 0, -1):
	if x % factor == 0 and y % factor == 0:
		print('%d和%d的最大公约数是%d' % (x, y, factor))
		print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
		break
"""

"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""
for x in range(1,6):
	print('*'*x)

count = 1
for i in range(5,0,-1):
	print(((i-1)*' ') + ((count)*'*'))
	count += 1

count = 1
for i in range(5,0,-1):
	print(((i-1)*' ') + ((count*2-1)*'*'))
	count += 1

row = 5
for i in range(row):
	

    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print((2 * i + 1))
    print()

for _ in range(1,10):
	print('*',end='')
