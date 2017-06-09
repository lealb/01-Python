# -*- coding: utf-8 -*-
# Description: Python 编程快捷上手 第三章
# 2017/6/7:11:38


def collatz(number):
    if (number % 2):
        print(3 * number + 1)
        return 3 * number + 1
    else:
        print(number // 2)
        return number // 2


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Please enter a number: "))
            collatz(number)
            # break
        except ValueError:
            print("Oops!That was no valid number.Try again")

