## 在屏幕上显示跑马灯文字
import os
import time
import random

""" 
    跑马灯设计
def main():
    content = '北京欢迎你为你开天劈地...'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
"""

def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code
print("生成指定长度的验证码")
print(generate_code(5))


def get_mx2(n):
    k1,k2 = (n[0],n[1]) if n[0] > n[1] else (n[1],n[0])
    for i in range(2,len(n)):
        if n[i] > k1:
            k2 = k1
            k1 = n[i]
        elif n[i] > k2:
            k2 = n[i]
    return k1,k2

print("获取数组中的前两个最大的值")
print(get_mx2([i*2 for i in range(1,9)]))
        
##计算指定的年月日是这一年的第几天

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def which_day(year,month,day):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1 ):
        total += days_of_month[index]
    return total + day
print("计算指定的年月日是这一年的第几天")
print(which_day(2020,10,17))

## 打印杨辉三角

def Pascal_Triangle(row):
    yh = [[]] * row
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()
print("打印杨辉三角")
print(Pascal_Triangle(7))