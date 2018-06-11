# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-11-09:52 AM
import socket


def test1(port, ip="127.0.0.1"):
    """
    记住server与client的区别，server通过绑定ip，通过conn交互
    client通过socket连接交互
    :param port:
    :param ip:
    :return:
    """
    sk = socket.socket()
    address = (ip, port)
    sk.bind(address)
    print("Server online ,Waiting connect……")
    sk.listen(3)  # waiting connect numbers
    count = 0
    while True:
        conn, addr = sk.accept()
        print("SK ACCEPT:%s" % str(conn))
        while count < 3:
            try:
                data = conn.recv(1024)  # data is not null

                if not data:
                    break
                else:
                    print("%s:%s" % (addr[1], str(data, "utf8")))
                    # 回信
                    cin = input(">>>>>")
                    # 1.ConnectionResetError 如果没有发送消息直接force disconnect,在recv()除捕获
                    # 如果先发送信息，后捕获，位置于send()方法
                    # 2.在Linux 环境下，默认强制断开为发送空消息，不会跑出异常
                    conn.send(bytes(cin, "utf8"))
                    count = count + 1
            except ConnectionResetError as error:
                print("Client force disconnect:", error)
                break
        conn.close()
    sk.close()


if __name__ == "__main__":
    test1(1226)
