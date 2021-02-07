# -*- coding: utf-8 -*-
"""109.11.15 模組.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w2Q6mK2OKxYEXXCfHX35-ovOjU6se0mW
"""

#匯入模組import
#匯入模組中指定的函式from...import
#別名的使用as

#擲骰子遊戲
import random

while True:
  inkey = input('按任意鍵再按[Enter]鍵擲骰子，直接按[Enter]鍵結束:')
  if len(inkey) > 0:
    num = random.randint(1, 6)
    print('你擲的骰子為:' +str(num))
  else:
    print('遊戲結束!')
    break

#大樂透中獎號碼
import random

list1 = random.sample(range(1, 50), 7)
special = list1.pop()
list1.sort()
print('本期大樂透中獎號碼為:', end=',')
for i in range(6):
  if i ==5: print(str(list1[i]))
  else: print(str(list1[i]), end=',')
print('本期大樂透特別號為:'+ str(special))

#時間模組time
import time
print(time.time()) #1605341080.289486

import time
print(time.localtime())
print(time.localtime(time.time()))

#ctime() , 傳回值為[字串]
import time as t
print(t.ctime())
print(t.ctime(t.time()))

#列印時間凾式所有資訊
import time as t

week = ['一', '二', '三', '四', '五', '六', '日']
dst = ['無日光節約時間', '有日光節約時間']
time1 = t.localtime()
show = '現在時刻:中華民國' + str(int(time1.tm_year)-1911) +'年'
show += str(time1.tm_mon) + '月' + str(time1.tm_mday) + '日'
show += str(time1.tm_hour) + '時' + str(time1.tm_min) + '分'
show += str(time1.tm_sec) + '秒 星期' + week[time1.tm_wday] + '\n'
show += '今天是今年的第' + str(time1.tm_yday) + '天，此地' + dst[time1.tm_isdst]
                         
print(show)

