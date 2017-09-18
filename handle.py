#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-09-12 11:58:28

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

template = '''
{id}:
  host: {ip}
  user: root
  passwd: password
  minion_opts:
    - id: {id}
'''


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        response = self.rfile.read(int(self.headers['content-length']))
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.data_parse(response)
        self.do_insert(self.data)
        result = ('data: %s, send OK\n' % response).encode('ascii')
        self.wfile.write(result)

    def do_insert(self, data):
        with open(r'/etc/salt/roster', 'a') as f:
            f.write(data + '\n')

    def data_parse(self, data):
        data = json.loads(data.decode('utf-8'))
        self.data = template.format(id=data['id'], ip=data['ip'])
        return self.data


def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
