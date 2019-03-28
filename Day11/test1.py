from random import randint, randrange
from abc import ABCMeta, abstractmethod
"""
	主要是通过小游戏，奥特曼和小怪兽的回合制战斗来更好的实现对类、方法、
	简单逻辑的一些处理，更深层次的熟悉这些概念
"""
class Fighter(object, metaclass= ABCMeta):
	"""docstring for Fight"""
	__slots__ = ('_name', '_hp')
	def __init__(self, name, hp):
		self._name = name
		self._hp = hp

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def hp(self):
		return self._hp if self._hp > 0 else 0

	@hp.setter
	def hp(self, hp):
		self._hp

	@property
	def alive(self):
		return self._hp > 0

	def attack(self):
		pass

class Ultraman(Fighter):
	"""docstring for Ultraman"""
	__slots__ = ('_name', '_hp', '_mp')

	def __init__(self, name, hp, mp):
		super().__init__(name, hp)
		self._mp = mp

	@property
	def mp(self):
		return self._mp
	
	@mp.setter
	def mp(self, mp):
		self._mp = mp

	def attack(self, other):
		hp_reduce = randint(15, 25)
		other._hp -= hp_reduce
	
	def hage_attack(self, other):
		if self._mp > 50:
			self._mp -= 50
			huge_harm = other._hp * 3 // 4
			huge_harm = huge_harm if other._hp > 50 else 50
			other._hp -= huge_harm
			return True
		else:
			self.attack(other)

	def magic_attack(self, others):
		if self._mp >= 20:
			self._mp -= 20
			for monster in others:
				if monster.alive:
					monster._hp -= randint(10, 15)
			return True
		else:
			return False
	def resume(self):
		incr_point = randint(1, 10)
		self._mp += incr_point
		return incr_point

	def __str__(self):
		return "~~~~~奥特曼 %s" % self._name + ' 生命值 %s' % str(self._hp) + ' 魔法值 %s' % str(self._mp)

class Monster(Fighter):
	"""docstring for Monster"""
	__slots__ = ('_name', '_hp')

	def attack(self, other):
		if other.alive:
			other._hp -= randint(10, 20)
	def __str__(self):
		return "~~~~~小怪兽 %s" % self._name + ' 生命值 %d' % self._hp

def is_any_alive(monsters):
	for monster in monsters:
		if monster.alive:
			return True
	return False

def select_one_monster(monsters):
	monsters_len = len(monsters)
	while True:
		index = randrange(monsters_len)
		if monsters[index].alive:
			return monsters[index]

def display_info(ultraman, monsters):
	print(ultraman)
	for monster in monsters:
		print(monster)

def main():
	man = Ultraman('pekey', 1000, 120)
	m1 = Monster('aaa', 250)
	m2 = Monster('bbb', 500)
	m3 = Monster('ccc', 750)
	ms = [m1, m2, m3]
	fight_round = 1

	while man.alive and is_any_alive(ms):
		monster = select_one_monster(ms)
		skill = randint(1, 10)
		if skill <= 6:
			print('%s 使用普通攻击攻击了 %s' % (man._name, monster._name))
			man.attack(monster)
			print('%s 的魔法点回复了 %s' % (man._name, man.resume()))
		elif skill <= 9:
			if man.magic_attack(ms):
				print('%s 使用了魔法攻击' % man._name)
			else:
				print('%s 使用了魔法攻击失败' % man._name)
		else:
			if man.hage_attack(monster):
				print('%s 使用了超级必杀技击杀 %s ' % (man._name, monster._name))
			else:
				print('%s 使用普通攻击攻击了 %s' % (man._name, monster._name))
				print('%s 的魔法点回复了 %s' % (man._name, man.resume()))
		if monster.alive:
			print('%s 回击了 %s' % (monster._name, man._name))
			monster.attack(man)
		display_info(man, ms)
		fight_round += 1
	print('====================战斗结束===================')
	if man.alive:
		print('奥特曼胜利...')
	else:
		print('小怪兽胜利...')

if __name__ == '__main__':
	main()
