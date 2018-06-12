# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:2018-06-12-10:38 PM

import socketserver


class TestSocketServer(socketserver.BaseRequestHandler):

    def handle(self):
        print("Server is online...")
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                receive_data = conn.recv(1024)
                print("%s:%s" % (self.client_address[1], receive_data.decode("utf8")))
                # reply
                reply_data = input(">>>")
                conn.sendall(reply_data.encode("utf8"))
            conn.close()


if __name__ == '__main__':
    port = 1226
    server = socketserver.ThreadingTCPServer(('127.0.0.1', port), TestSocketServer)
    server.serve_forever()
