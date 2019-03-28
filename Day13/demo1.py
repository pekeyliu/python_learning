import time
def main():
	file = None
	try:
		# file = open('aaa.txt', 'r', encoding='utf-8')
		# print(file.read())
		"""with 可自动释放资源，不需要进行close操作"""
		# with open('aaa.txt', 'r', encoding='utf-8') as f:
		# 	print(f.read())

		#通过for-in 方式进行读取
		# with open('aaa.txt', mode='r', encoding='utf-8') as f:
		# 	for line in f:
		# 		print(line, end=' ')
		# 		time.sleep(1)
		# print()

		with open('./doc/aaa.txt', 'r', encoding='utf-8') as f:
			line = f.readlines()
		print(line)

	except FileNotFoundError as e:
		print('无法打开文件')
	except LookupError:
		print('未知编码')
	except UnicodeDecodeError:
		print("读取文件时解码错误!")
	

if __name__ == '__main__':
	main()