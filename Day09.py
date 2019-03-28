from time import sleep
import math
class Clock(object):
	"""docstring for Clock"""
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def run(self):
		"""走字"""
		self.second += 1
		if self.second == 60:
			self.second = 0
			self.minute += 1
		if self.minute == 60:
			self.minute = 0
			self.hour += 1
		if self.hour == 24:
				self.hour = 0

	def __str__(self):
		return "%02d:%02d:%02d" % (self.hour,self.minute,self.second)

# def main():
# 	clock = Clock(23, 59, 58)
# 	while True:
# 		print(clock)
# 		sleep(1)
# 		clock.run()

# if __name__ == '__main__':
# 	main()


"""定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法"""
class point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def move(self, x, y):
		self.x = x
		self.y = y
	def move_to(self, x, y):
		self.x += x
		self.y += y
	def get_distance(self, other):
		X = self.x - other.x
		Y = self.y - other.y
		return math.sqrt(X**2 + Y**2)

	def __str__(self):
		return "(%d,%d)" % (self.x, self.y)

def main():
	a = point(3, 5)
	b = point(-4, -8)
	print("two point distance is %f" % a.get_distance(b))

if __name__ == '__main__':
	main()
