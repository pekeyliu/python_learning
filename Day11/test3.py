from random import randrange

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
		all_suites = ('♠', '♥', '♣', '♦', '')
		if self._face == 1:
			face_str = 'A'
		elif self._face == 11:
			face_str = 'J'
		elif self._face == 12:
			face_str = 'Q'
		elif self._face == 13:
			face_str = 'K'
		elif self._face == 51:
			face_str = 'JOKER1'
		elif self._face == 52:
			face_str = 'JOKER2'
		else:
			face_str = str(self._face)
		return '%s%s' % (all_suites[self._suite], face_str)

class Poker(object):
	"""一副牌"""
	def __init__(self):
		self._cards = []
		self._current = 0
		for suite in range(5):
			if suite < 4:
				for face in range(1,14):
					card = Card(suite, face)
					self._cards.append(card)
			else:
				joker1_card = Card(suite, 51)
				self._cards.append(joker1_card)
				joker2_card = Card(suite, 52)
				self._cards.append(joker2_card)

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

def dou_dizhu():
	poker = Poker()
	poker.shuffle()

	players = [Player('东邪'), Player('西毒'), Player('南帝')]
	residue_cards = []

	for _ in range(17):
		for player in players:
			player.get(poker.next)

	for _ in range(3):
		residue_cards.append(poker.next)

	for player in players:
		print(player.name + ':', end=' ')
		player.arrange(get_key)
		for card in player._card_on_hand:
			print(card, end=' ')
		print()
	print('底牌：', end='')
	for card in residue_cards:
		print(card, end=' ')
	print()

def main():
	#玩斗地主
	dou_dizhu()  

if __name__ == '__main__':
	main()