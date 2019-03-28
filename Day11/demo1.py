class Person(object):

	__slots__ = ('_name', '_age', '_gender')

	"""docstring for ClassName"""
	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name
	
	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, age):
		self._age = age

	def play(self):
		if self._age <= 16:
			print("%s 正在下飞行棋" % self._name)
		else:
			print("%s 正在斗地主" % self._name)

def main():
	p = Person('pekey',25)
	p.play()
	p.age = 14
	p.play()
	p._gender = '男'
	print(p._gender)


if __name__ == '__main__':
	main()

