# encoding: utf-8
"""
@author: Yaoyang
@contact: YooLight99@163.com
@time: 2020-07-30 9:34
@file: Myname.py
@desc: 
"""
#动态规划法

#原问题：Redraiment是走梅花桩的高手。Redraiment总是起点不限
# 从前到后，往高的桩子走，但走的步数最多，不知道为什么？
# 你能替Redraiment研究他最多走的步数吗？
def GetResult(l):
    n = len(l)  # 传入list的长度
    dp = [1] * n  # dp[i]表示以第i个桩为结尾，最多走多少步，初始是1步（默认这个桩是跟它之前相比最矮的）
    res = 0  # 整个问题的结果
    for i in range(n):  # i表示第几个桩
        for j in range(i):  # j表示i前面的桩
            if l[i] > l[j]:  # 如果第i个桩前面有比它矮的（比如是j），
                # 且以第j个桩为结尾走的步数是最多的，
                # 步数就是dp[j]+1，加的这个1表示从第j个走1步到第i个桩；另一种就是dp[i],默认等于1，但是
                # 遍历j的过程可能会更新这个值，因此取上述两个结果中最大的那个值，表示第i个桩为结尾，
                # 最多走多少步
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])  # 到第i个桩时最多走几步
    return res


while True:
    try:
        n = int(input())  # 几个点
        str_input = input().split()
        l = [int(v) for v in str_input]  # 输入的数组成的集合
        # l=[2,5,1,5,4,5]
        # print(l)
        ans = GetResult(l)
        print(ans)
    except:
        break
