import re

def main():
	str1 = r'^[0-9a-zA-Z_]{6,20}$' #6-20的字母数字下划线组成
	str2 = r'^[1-9]\d{4,11}$'  # 12的数字，且第一位数字不能为0
	# 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
	str3 = r'(?<=\D)1[34578]\d{9}(?=\D)' 