#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-09-15 10:58:46

import socket
from selectors import DefaultSelector, EVENT_READ

selector = DefaultSelector()


class Chat:
    def __init__(self, host, port, max_clients):
        self.clients = []
        self.host = host
        self.port = port
        self.stoped = False
        self.max_clients = max_clients

    def run(self):
        self.sock = socket.socket()
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.max_clients)
        self.sock.setblocking(False)
        selector.register(self.sock, EVENT_READ, self.accept)

    def accept(self, key, mask):
        print('accept')
        conn, addr = self.sock.accept()
        self.clients.append(addr)
        conn.setblocking(False)
        selector.register(conn, EVENT_READ, self.handle)

    def handle(self, key, mask):
        selector.unregister(key.fd)
        print('send')
        conn = key.fileobj
        print(conn.getpeername())
        try:
            data = conn.recv(4096)
        except BlockingIOError:
            pass
        if data:
            for client in self.clients:
                if client != conn.getpeername():
                    self.sock.sendto(data, client)


def loop(self):
    while not self.stoped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)

    def stop(self):
        self.stoped = True


if __name__ == '__main__':
    chat = Chat('localhost', 8000, 10)
    chat.run()
    loop()
