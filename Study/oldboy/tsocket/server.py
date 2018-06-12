# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-11-09:52 AM
import socket
import subprocess


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


def test_cmd(port, ip="127.0.0.1"):
    # 1.实例化套接字对象
    sk = socket.socket()
    # 2.指定连接的ip地址和端口
    address = (ip, port)
    # 3 服务器绑定
    sk.bind(address)
    # 4 设置连接等待数
    sk.listen(3)
    # waiting connect,get accept
    print("%s is online,waiting connect" % address[1])
    # 5.准备监听，获取连接信息
    conn, addr = sk.accept()
    print("%s Connected successfully" % addr[1])
    # 6.准备接收客户端命令，执行返回结果
    while True:
        command = conn.recv(1024)
        if not command:
            break
        result = subprocess.Popen(str(command, "utf8"), shell=True, stdout=subprocess.PIPE)
        result_data = result.stdout.read()
        result_length = bytes(str(len(result_data)), "utf8")
        # sendall会把数据直接全部发送到客户端，客户端将所有的数据都放到缓冲区,
        # 每次recv多少字节取决于recv内的参数，理论不应该超过8k
        conn.sendall(result_length)
        conn.sendall(result_data)
    conn.close()
    sk.close()


if __name__ == "__main__":
    test_cmd(1226)
