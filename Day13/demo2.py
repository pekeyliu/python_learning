from math import sqrt

def is_primes(number):
	assert number > 0
	for x in range(2, int(sqrt(number)) + 1):
		if number % x == 0:
			return False
	return True if number != 1 else False

def main():
	filenames = ('./doc/a.txt', './doc/b.txt', './doc/c.txt')
	fs_list = []
	try:
		for filename in filenames:
			fs_list.append(open(filename, 'w', encoding='utf-8'))
		for number in range(1,10000):
			if is_primes(number):
				if number < 100:
					fs_list[0].write(str(number) + '\n')
				elif number < 1000:
					fs_list[1].write(str(number) + '\n')
				else:
					fs_list[2].write(str(number) + '\n')
	except Exception as e:
		raise
	else:
		pass
	finally:
		for fs in fs_list:
			fs.close()

if __name__ == '__main__':
	main()