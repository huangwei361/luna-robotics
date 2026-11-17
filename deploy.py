#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Luna Robotics 官网本地部署脚本
用法:
    python deploy.py              # 启动本地服务器（默认 8080 端口）
    python deploy.py --port 9000  # 指定端口
    python deploy.py --no-browser # 不自动打开浏览器
"""
import http.server
import socketserver
import os
import sys
import threading
import webbrowser

PORT = 8080
OPEN_BROWSER = True

args = sys.argv[1:]
if '--port' in args:
    try:
        PORT = int(args[args.index('--port') + 1])
    except (IndexError, ValueError):
        print('端口参数无效，使用默认 8080')
if '--no-browser' in args:
    OPEN_BROWSER = False

ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stdout.write('[%s] %s\n' % (self.log_date_time_string(), fmt % args))
        sys.stdout.flush()


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == '__main__':
    with ThreadedServer(('127.0.0.1', PORT), Handler) as httpd:
        url = 'http://127.0.0.1:%d/index.html' % PORT
        btc_url = 'http://127.0.0.1:%d/btc-training/index.html' % PORT
        print('=' * 58)
        print('  Luna Robotics 官网已启动')
        print('=' * 58)
        print('  主站首页 : %s' % url)
        print('  BTC 专题 : %s' % btc_url)
        print('=' * 58)
        print('  按 Ctrl+C 停止服务')
        sys.stdout.flush()
        if OPEN_BROWSER:
            threading.Timer(0.8, lambda: webbrowser.open(url)).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\n服务已停止')
