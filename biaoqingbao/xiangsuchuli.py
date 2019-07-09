# @Author : wangxz
# -*- coding: utf-8 -*-

import re
data = 'http://www.interoem.com/messageinfo.asp?id=3'
ret = re.sub(r'com/(.*)',"com", data)
print(ret)