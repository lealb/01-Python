# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-11-09:56 AM
import socket
import subprocess


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


def test_cmd(command):
    a = subprocess.Popen(command, shell=True)
    print(a)


if __name__ == "__main__":
    # test1(1226)
    test_cmd('dir')
