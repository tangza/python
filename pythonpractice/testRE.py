# encoding: UTF-8

import re

# 匹配不是以abc开头的字符串（使用不作为分组的特殊构造）
# pattern = re.compile(r'\b(?!abc).*')
# \b == (?<!\w)(?=\w) 代表单词边界

# 匹配不包含abc的单词
pattern = re.compile(r'\b(?!\w*abc)\w*')

match = pattern.match('dabdcd')

if match:
	print(match.group())