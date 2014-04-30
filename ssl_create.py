#!usr/bin/env python
import os

from config import CERT_NAME

os.system("openssl genrsa -des3 -passout pass:x -out server.pass.key 2048")
os.system("openssl rsa -passin pass:x -in server.pass.key -out {0}.key".format(CERT_NAME))
os.system("rm server.pass.key")
os.system("openssl req -new -key {0}.key -out {0}.csr".format(CERT_NAME))
os.system("openssl x509 -req -days 365 -in {0}.csr -signkey {0}.key -out {0}.crt".format(CERT_NAME))