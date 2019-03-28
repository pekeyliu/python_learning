from random import randrange
"""
		21点游戏
"""

class Card(object):
	"""一张牌"""
	def __init__(self, suite, face):
		self._suite = suite
		self._face = face

	@property
	def face(self):
		return self._face

	@property
	def suite(self):
		return self._suite

	def __str__(self):
		all_suites = ('♠', '♥', '♣', '♦')
		if self._face == 1:
			face_str = 'A'
		elif self._face == 11:
			face_str = 'J'
		elif self._face == 12:
			face_str = 'Q'
		elif self._face == 13:
			face_str = 'K'
		else:
			face_str = str(self._face)
		return '%s%s' % (all_suites[self._suite], face_str)

class Poker(object):
	"""一副牌"""
	def __init__(self):
		self._cards = []
		self._current = 0
		for suite in range(4):
			for face in range(1,14):
				card = Card(suite, face)
				self._cards.append(card)

	@property
	def cards(self):
		return self._cards
	
	def shuffle(self):
		"""洗牌"""
		self._current = 0
		cards_len = len(self._cards)
		for index in range(cards_len):
			pos = randrange(cards_len)
			self._cards[index], self._cards[pos] = self._cards[pos], self._cards[index]

	@property
	def next(self):
		"""发牌"""
		card = self._cards[self._current]
		self._current += 1
		return card

	@property
	def has_next(self):
		return self._current < len(self._cards)

class Player(object):
	"""docstring for Player"""
	def __init__(self, name):
		self._name = name
		self._card_on_hand = []

	@property
	def name(self):
		return self._name

	@property
	def card_on_hand(self):
		return self._card_on_hand

	def get(self, card):
		"""摸牌"""
		self._card_on_hand.append(card)
									
	def arrange(self, card_key):
		self._card_on_hand.sort(key=card_key)

#排序规则，先根据花色，再根据点数排序
def get_key(card):
	return (card.suite, card.face)

def blackjack():
	poker = Poker()
	poker.shuffle()
	players = [Player('玩家'), Player('电脑')]

	a_is_over = True
	b_is_over = True
	sum_card1 = 0
	sum_card2 = 0

	print('游戏开始，开始发牌')
	for player in players:
		card = poker.next
		player.get(card)
		print('%s的牌为：' % player.name, end=' ')
		print(card)
	sum_card1 = players[0].card_on_hand[0].face
	sum_card2 = players[1].card_on_hand[0].face
	while a_is_over or b_is_over:
		# print('a 的结果 ' + ('未结束' if a_is_over else '结束') + ' b的结果 ' + ('未结束' if b_is_over else '结束'))
		if a_is_over and sum_card1 <= 21:
			choice = input('玩家选择是否继续发票？(Y/N)')
			if choice == 'Y':
				card = poker.next
				players[0].get(card)
				print('%s的牌为：' % players[0].name, end=' ')
				print(card)
				sum_card1 += card.face
				print('玩家总分为：%d' % sum_card1)
			else:
				sum_card1 = sum_card1 if sum_card1 <= 21 else 0
				a_is_over = False
		else:
			sum_card1 = sum_card1 if sum_card1 <= 21 else 0
			a_is_over = False

		if b_is_over and sum_card2 <= 21:
			card2 = poker.next
			players[1].get(card2)
			print('%s的牌为：' % players[1].name, end=' ')
			print(card2)
			sum_card2 += card2.face
			print('电脑总分为：%d' % sum_card2)
			if sum_card2 < 18:
				pass
			elif sum_card2 >= 18 and sum_card2 <= 21:
				b_is_over = False
			else:
				sum_card2 = 0
				b_is_over = False
		else:
			b_is_over = False

	print('玩家获胜，总点数%d,电脑总点数 %d' % (sum_card1, sum_card2))
	if sum_card1 > sum_card2:
		print('玩家获胜')
	elif sum_card1 < sum_card2:
		print('电脑获胜')
	else:
		print('不分胜负，请重新开始')



def main():
	#玩升级游戏
	blackjack()   

if __name__ == '__main__':
	main()