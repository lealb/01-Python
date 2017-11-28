# -*- coding: utf-8 -*-
# Description: 企业利润提成
# 2017/9/5 15:34


# 常规方法 if 不支持switch
def testWay1(money):
    bonus = 0
    if money <= 100000:
        bonus = money * 0.1
    elif 100000 < money <= 200000:
        bonus = 10000 + (money - 100000) * 0.075
    elif 200000 < money <= 400000:
        bonus = 10000 + 7500 + (money - 400000) * 0.05
    elif 400000 < money <= 600000:
        bonus = 10000 + 7500 + 10000 + (money - 600000) * 0.03
    elif 600000 < money <= 1000000:
        bonus = 10000 + 7500 + 10000 + 6000 + (money - 600000) * 0.015
    elif money > 1000000:
        bonus = 10000 + 7500 + 10000 + 6000 + 6000 + (money-1000000) * 0.01
    return bonus


# list
def testWay2(money):
    profit = [1000000, 600000, 400000, 200000, 100000, 0]
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    bonus = 0
    for i in range(0, 6):
        if money > profit[i]:
            bonus += (money - profit[i]) * rate[i]
            money = profit[i]
    return bonus


# 嵌套列表
def testWay3(profit):
    bonus = 0
    profit /= 10000
    bonusRateList = [[100, 0.010], [60, 0.015], [40, 0.030], [20, 0.050], [10, 0.075], [0, 0.100]]

    for i in range(0, len(bonusRateList)):
        if (profit > bonusRateList[i][0]):
            bonus += ((profit - bonusRateList[i][0]) * bonusRateList[i][1])
            profit = bonusRateList[i][0]
    return bonus * 10000


if __name__ == '__main__':
    money = int(input('Please input profit value:'))
    bonus = testWay1(money)
    print(bonus)
