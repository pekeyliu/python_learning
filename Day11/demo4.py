from demo1 import Person

class Student(Person):
	"""docstring for Student"""
	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self._grade = grade

	@property
	def grade(self):
		return self._grade

	@grade.setter
	def grade(self, grade):
		self._grade = grade

	def study(self, course):
		print('%s 正在学习 %s 课程' % (self.name, course))

class Teacher(Person):
	"""docstring for Teacher"""
	def __init__(self, name, age, title):
		super().__init__(name, age)
		self._title = title

	@property
	def title(self):
		return self._title
	
	@title.setter
	def title(self, title):
		self._title = title

	def teach(self, course):
		print('%s 正在教 %s 课程' % (self.name, course))

def main():
	student = Student('小明', 23, '大一')
	student.study('AI')

	teacher = Teacher('王大志', 57, '副教授')
	teacher.teach('机器学习')

if __name__ == '__main__':
	main()