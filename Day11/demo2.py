from math import sqrt

class Triangle(object):
	"""docstring for Triangle"""
	def __init__(self, a, b, c):
		self._a = a
		self._b = b
		self._c = c

	@staticmethod
	def is_valid(a, b, c):
		return a + b > c and b + c > a and a + c > b

	def perimeter(self):
		return (self._a + self._b + self._c) * 2

	def area(self):
		half = self.perimeter() / 2
		return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def main():
	if Triangle.is_valid(3, 4, 5):
		t = Triangle(3, 4, 5)
		print("三角形的周长为：%d" % t.perimeter())
		print('三角形的面积为: %f' % t.area())
	else:
		print("不构成三角形")

if __name__ == '__main__':
	main()