# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-11-09:56 AM
import socket


def test1(port, ip="127.0.0.1"):
    sk = socket.socket()
    address = (ip, port)
    try:
        sk.connect(address)
        print("SK:%s" % sk)
        count = 0
        while count < 5:
            cin = input(">>>>>")
            if cin.casefold() == "exit":
                break
            else:
                sk.send(bytes(cin, "utf8"))
                data = sk.recv(1024)
                print("%s:%s" % (str(address[1]), str(data, "utf8")))
            count = count + 1
        sk.close()
    except ConnectionAbortedError as error:
        print("Server is offline", error)
        return 0


def test_cmd(port, ip="127.0.0.1"):
    """
    subprocess.PIPE把输出放进管道PIPE
    :param command:
    :return:
    """
    # 1.创建对象
    sk = socket.socket()
    # 2.连接服务端指定的ip地址和端口
    address = (ip, port)
    sk.connect(address)
    while True:
        command = input(">>>>")
        if command.casefold() == "exit":
            break
        # 3.发送命令
        sk.send(bytes(command, "utf8"))
        # 4.获取返回结果并打印
        # 解决结果大于1024的接收问题，先接收数据的长度，然后累加
        receive_length = int(str(sk.recv(1024), "utf8"))
        print("Length:", receive_length)
        receive_data = bytes()
        while len(receive_data) != receive_length:
            print(len(receive_data))
            receive_data += sk.recv(1024)
            print(len(receive_data))
        print("Execute %s Result is:%s" % (command, str(receive_data, "utf8")))
    sk.close()


if __name__ == "__main__":
    # test1(1226)
    test_cmd(1226)
