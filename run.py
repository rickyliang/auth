#!/usr/bin/env python

from app import app
from config import CTX

app.run(host='127.0.0.1', port=4444, ssl_context=CTX, debug=True)