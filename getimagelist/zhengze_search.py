#encoding=gbk
import re

search = re.search(r'fishC', 'i love fishC.com')
print(search)
#  d  ƥ������
#  . �κ��ַ�
print(re.search(r'.', '2a1afawf'))
# ƥ��ip��ַ


print(re.search(r'[aeiou]', 'I love '))
print(re.search(r'[a-z]', ' I s'))
print(re.search(r'ab{3}c', 'abbbbc'))
print(re.search(r'ab{2,10}c', 'abbbbbc'))
print(re.search(r'[0-25]', '6'))  # ���� 0 .1 .2 .5
#ƥ������  0 - 255
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '188'))
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-4]', '254'))

#ip��ַ
print(re.search(r'([01]\d\d|2[0-4]\d25[0-5])'))