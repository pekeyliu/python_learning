from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
	"""docstring for Pet"""			
	def __init__(self, nikename):
		self._nikename = nikename

	@abstractmethod
	def make_voice(self):
		pass

class Dog(Pet):
	"""docstring for Dog"""
		
	def make_voice(self):
		print('%s is wangwang' % self._nikename)

class Cat(Pet):
	"""docstring for Cat"""
	def make_voice(self):
		print('%s is miaomiao' % self._nikename)

def main():
	dog = Dog("二哈")
	dog.make_voice()
	cat = Cat('喵星人')
	cat.make_voice()

if __name__ == '__main__':
	main()
		