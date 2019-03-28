def main():
	try:
		with open('./icon/aa.jpg', 'rb') as fs:
			data = fs.read()
			print(type(data))
		with open('./icon/cc.jpg', 'wb') as fs2:
			fs2.write(data)
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass

if __name__ == '__main__':
	main()