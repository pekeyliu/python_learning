import math
"""
输入M和N计算C(M,N)


m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fm // fn // fmn)
"""

"""
	获取最大公约数和最小公倍数
"""
def gcd(x,y):
	(x,y) = (y,x) if x > y else (x,y)
	for i in range(x,0,-1):
		if x % i == 0 and y % i == 0:
			return i

def lcm(x,y):
	return x * y // gcd(x,y)

print("获取28和56的最小公倍数=====")
print(lcm(28,56))

print("判断是否为回文数（1）========")

def recycl(n):
	if n < 10:
		print('是回文')
		return True
	else:
		m = list(str(n))
		m_len = len(m)
		if m_len % 2 == 0:
			mid = m_len // 2
			tmp = mid
			for x in range(0,mid):
				if m[x] == m[2*tmp-1+x]:
					pass
					#print('是回文')
				else:
					print('不是回文')
					return False
				tmp -= 1
			return True
		else:
			mid = m_len // 2
			tmp = mid

			for x in range(0,mid):
				if m[x] == m[2*tmp+x]:
					pass
				else:
					print('不是回文')
					return False
				tmp -= 1
			return True	
print(recycl(1432))

"""
	正着的数等于倒着数的数
"""
print("判断是否为回文数（2）========")
def is_palindrome(num):
	temp = num
	total = 0
	while temp > 0:
		total = total * 10 + temp % 10
		temp //= 10
	return total == num
print(is_palindrome(1432))

print("判断是否为素数")
def is_primes(num):
	mid = int(math.sqrt(num))
	for x in range(2,mid +1):
		if num % x == 0:
			return False
	return True  if num != 1 else False
print(is_primes(25))

if __name__ == '__main__':
	num = int(input('请输入正整数: '))
	if is_palindrome(num) and is_primes(num):
		print('%d是回文素数' % num)