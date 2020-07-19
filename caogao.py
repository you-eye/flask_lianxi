import datetime
import os
import random
import re

import requests

li = '1234'.split(' ')

str1 = 'dljfdl'

li1 = [1, 2, 1]
li2 = [3, 4, 5]
dic = {'a': 1, 'b': 2, 'c': 3}
dic['d'] = dic.get('d', 0) + 1
import re

# str2 = 'dlkfjdlkfjfdklfj1234fddfds'
# print(re.findall(r'.*j(.*?)f', str2))
# from hashlib import md5, sha1, sha256
#
# print(md5(str2.encode('utf-8')).hexdigest())  # 32
# print(sha1(str2.encode('utf-8')).hexdigest())  # 40
# print(sha256(str2.encode('utf-8')).hexdigest())  # 64

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

}
url = 'https://hz.zu.anjuke.com/fangyuan/'
res = requests.get(url, headers=headers)
print(res.text)
print('1111111111111111111')
print('1111111111111111111')

