# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-13-09:09 PM
import threading
import time

# lock = threading.Lock()
# lock = threading.Lock()
lock = threading.RLock()


class DeadLock(threading.Thread):
    def lock_a(self):
        lock.acquire()
        print(self.name, "gotlock", time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name, "gotlock", time.ctime())
        lock.release()
        lock.release()

    def lock_b(self):
        lock.acquire()
        print(self.name, "gotlock", time.ctime())
        time.sleep(2)
        lock.acquire()
        print(self.name, "gotlock", time.ctime())
        lock.release()
        lock.release()

    def run(self):
        self.lock_a()
        self.lock_b()


# 应用
class Account(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = threading.RLock()

    def withdraw(self, amount):
        """
        提现
        :param amount: 金额
        :return:
        """
        with self.lock:
            self.balance -= amount

    def deposit(self, amount):
        """
        存款
        :param amount:
        :return:
        """
        with self.lock:
            self.balance += amount

    def draw_cash(self, amount):  # lock.acquire中嵌套lock.acquire的场景
        """

        :param amount:
        :return:
        """
        with self.lock:
            interest = 0.05
            count = amount + amount * interest

            self.withdraw(count)


def transfer(from_account, to_account, amount):
    # 锁不可以加在这里 因为其他的其它线程执行的其它方法在不加锁的情况下数据同样是不安全的
    from_account.withdraw(amount)
    to_account.deposit(amount)


if __name__ == "__main__":
    """
    解决死锁和递归锁，只需要创建一把递归锁即可
    RLock 实现一个锁+计数器
    """
    # threads = []
    # for i in range(3):
    #     threads.append(DeadLock())
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    alex = Account('alex', 1000)
    yuan = Account('yuan', 1000)

    t1 = threading.Thread(target=transfer, args=(alex, yuan, 100))
    t1.start()

    t2 = threading.Thread(target=transfer, args=(yuan, alex, 200))
    t2.start()

    t1.join()
    t2.join()

    print('alex >>>', alex.balance)
    print('yuan >>>', yuan.balance)
