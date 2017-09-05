# -*- coding: utf-8 -*-
# Description: 关于外部数据
# 2017/6/22:1:48
import csv


def dealcsvDatabyStr(source, target):
    with open(source) as rf:
        reader = csv.reader(rf)
        with open(target, 'w') as wf:
            writer = csv.writer(wf)
            writer.writerow(next(reader))
            for row in reader:
                if row[0] < '2017-08-15':
                    continue
                if int(row[6]) >= 2737580000:
                    writer.writerow(row)


def testbreak():
    for i in range(1, 10):
        if i < 3:
            continue
        if i % 3 == 0:
            print(i)


if __name__ == "__main__":
    filname = "file/GSPC.csv"
    dealcsvDatabyStr(filname, "file/result.csv")
    #testbreak()
