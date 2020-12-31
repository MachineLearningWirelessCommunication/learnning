import re

s = "A B C D"
pattern1 = '\w+\s+\w+'
pattern2 = '(\w+)\s+\w+'
pattern3 = '(\w+)\s+(\w+)'
p1 = re.compile(pattern1)
print(p1.findall(s))
p2 = re.compile(pattern2)
print(p2.findall(s))
p3 = re.compile(pattern3)
print(p3.findall(s))
