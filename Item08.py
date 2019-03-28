from random import sample,randint,randrange
"""
	双色球选号
	enumerate() 函数可返回list的下标和值
	红色球为1-34中选取
	sample()实现从列表中选择不重复的n个元素。
"""
def display(balls):
	"""
		列表输出双色球号
	"""
	for x, y in enumerate(balls):
		if x == len(balls) - 1:
			print('|', end='')
		print('%02d' % y ,end=' ')
	print()

def random_select():
	"""
		随机产生一组号码
	"""
	red_balls = [x for x in range(1,34)]
	select_balls = []

	#for _ in range(6):
    #    index = randrange(len(red_balls))
    #    selected_balls.append(red_balls[index])
    #    del red_balls[index]

	select_balls = sample(red_balls,6)
	select_balls.sort()
	select_balls.append(randint(1,16))
	return select_balls

def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


# if __name__ == '__main__':
#     main()

"""
约瑟夫环问题


《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。

 说明：解决此类问题，可以考虑全是True的数组，尽量不要删减改变数组的大小，
 否则会导致数组的下标改变，统计更加麻烦
"""
def main():
    persons = [True] * 30
    # counter 死亡人数 index循环下标 number 报数
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()

"""
	井字棋游戏
"""
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


# if __name__ == '__main__':
#     main()
    
