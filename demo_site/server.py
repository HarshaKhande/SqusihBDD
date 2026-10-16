# -*- coding: UTF-8 -*-
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

HERE = Path(__file__).resolve().parent
os.chdir(HERE)
HOST = "127.0.0.1"
PORT = 8000
print("Squish demo site running at http://%s:%s" % (HOST, PORT))
print("Keep this window open while Squish tests are running.")
print("Press Ctrl+C to stop.")
ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler).serve_forever()
