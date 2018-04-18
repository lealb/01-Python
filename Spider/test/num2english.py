# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:4/18/2018-6:17 PM


if __name__ == "__main__":
    t1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
          'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
          'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
          'eighteen', 'nineteen']
    t2 = ['twenty', 'thirty', 'forty', 'fifth', 'sixty',
          'seventy', 'eighty', 'ninety']

    while 1:
        n = input('input a integer:')
        m = int(n)
        print(n)
# %10==0 单独处理20 30 40 等等
        if m < 20:
            print(t1[int(n)])
        elif m < 100:
            s = t2[int(n[0]) - 2]
            print('%s-%s' % (s, t1[int(n[1])]))
        elif m < 1000:
            if n[1] == '1' or n[1] == '0':
                print('%s hundred and %s' % (t1[int(n[0])],
                                             t1[int(n[1:])]))
            else:
                print('%s hundred and %s-%s' % (t1[int(n[0])],
                                                t2[int(n[1]) - 2], t1[int(n[2])]))
