for a in range(1,6):
          for b in range(1,6):
              for c in range(1,6):
                for d in range(1, 6):
                    if (a != b) and (b != c) and (c != d) and (a != d) and (a != c) and (d != b):

                          print(str(a)+str(b)+str(c)+str(d))


#!/usr/bin/env python
# -*- coding:utf-8 -*-
#导入random和string模块
# import random, string
# def GenPassword(length):
#     随机出数字的个数
    # numOfNum = random.randint(1,length-1)
    # numOfLetter = length - numOfNum
    # 选中numOfNum个数字
    # slcNum = [random.choice(string.digits) for i in range(numOfNum)]
    # 选中numOfLetter个字母
    # slcLetter = [random.choice(string.ascii_letters) for i in range(numOfLetter)]
    # 打乱这个组合
    # slcChar = slcNum + slcLetter
    # random.shuffle(slcChar)
    # 生成密码
    # genPwd = ''.join([i for i in slcChar])
    # return genPwd
# if __name__ == '__main__':
#     print (GenPassword(6))
