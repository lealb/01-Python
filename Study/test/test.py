# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:4/19/2018-8:49 PM

def test_gress():
    print("Begin Game".center(20, "*"))
    num = input("Get number:")
    try:
        num = int(num)
    except Exception as error:
        print("Error:", error)
        num = 0
    if num == 8:
        print("Success")
    # elif num > 8:
    #     print("Big")
    # else:
    #     print("Small")
    else:
        if num > 8:
            print("Big")
        else:
            print("Small")


if __name__ == "__main__":
    # print("中国".encode("gbk"))
    # print("\u5218\u51ef")
    test_gress()
