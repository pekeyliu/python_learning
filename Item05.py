import random
"""
	水仙花数，个位数的立方 + 十位数的立方 + 百位数的立方 = 本身
"""
print("1000以内的水仙花数为:")
for x in range(100,1000):
	a = x // 100
	b = x % 100 //10
	c = x % 10
	#print("a=%d,b=%d,c=%d" % (a,b,c))
	if x == (a**3 + b**3 + c**3):
		print(x, end = "\t")
print()
"""
	求算完全数，如果一个数恰好等于它的因子之和，则称该数为“完全数”
"""
print("10000 以内的完全数：")
for i in range(1,1000):
	k = 0
	for j in range(1,i):
		if (i % j) == 0:
			k += j
	if i == k:
		print(i,end="\t")

"""
	我国古代数学家张丘建在《算经》一书中提出的数学问题：
	鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
"""
print()
x,y,z = 0,0,0
for x in range(0,21):
	for y in range(0,34):
		z = 100 - x - y
		k = x + y + z
		m = 15*x + 9*y + z
		if m == 300 and k == 100:
			print("鸡翁=%d,鸡母=%d,鸡雏=%d" % (x,y,z))

"""
	斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）
	以兔子繁殖为例子而引入，故又称为“兔子数列”，
	指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
	在数学上，斐波纳契数列以如下被以递推的方法定义：
	F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）在现代物理、准晶体结构、化学等领域，
	斐波纳契数列都有直接的应用，为此，美国数学会从1963年起出版了以《斐波纳契数列季刊》
	为名的一份数学杂志，用于专门刊载这方面的研究成果。
"""
print("for 循环方式===========================")
result = 1
start_result = 1
end_result = 1
for x in range(1,30):
	if x == 1:
		end_result = 1
	elif x == 2:
		end_result = 1
	else:
		end_result =  start_result + result
		result = start_result
		start_result = end_result
		
	print(end_result,end = " ")

print("def 递归方式===========================")
def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return fibonacci(n-1) +fibonacci(n-2)
print(fibonacci(29),end = " ")

"""
	craps赌博游戏
	规则：玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；如果点数和为2、3或12，
	则玩家输庄家胜。若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的
	点数和则玩家胜；若掷出的点数和为7则庄家胜。
"""
print()
print()

print("==================================")

def get_number():
	a = random.randint(1,6)
	b = random.randint(1,6)
	print("a = %d and b = %d" % (a,b))
	return a + b
gamer_cnt = 0
master_cnt = 0
for x in range(1,1001):
	fisrt = get_number()
	is_win = True
	print("first score %d" % fisrt)
	if fisrt == 7 or fisrt == 11:
		print("the gamer is win!!! score = %d" % fisrt)
		is_win = False
		gamer_cnt += 1
	if fisrt == 2 or fisrt == 3 or fisrt == 12:
		print("the master is win ..... score = %d" % fisrt)
		is_win = False
		master_cnt += 1
	score = 0
	if is_win:
		for i in range(1,100):
			score = get_number()
			print("total score：%d" % score)
			if score == fisrt:
				print("the gamer is win!!! score = %d" % score)
				gamer_cnt += 1
				break
			elif score == 7:
				print("the master is win ..... score = %d" % score)
				master_cnt += 1
				break
			elif score > 12:
				print("this time game over!")
				break
print("执行10000次的结果为，玩家赢了%d次，庄家赢了%d次" % (gamer_cnt,master_cnt))
