'''
@Author: your name
@Date: 2020-04-14 10:54:20
@LastEditTime: 2020-07-29 13:43:08
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \py work\My python\Test.py
'''

a , neg , pos = input().split() , [] , []
for i in a:
    neg.append(int(i)) if int(i) < 0 else pos.append(int(i))
print( len(neg) )
print( sum(pos) / len(pos) )