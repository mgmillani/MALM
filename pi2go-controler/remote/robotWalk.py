#!/usr/bin/python

import remoteControl
import sys

address = '127.0.0.1'
port = 9001

if len(sys.argv) == 2:
    address = sys.argv[1]

if len(sys.argv) == 3:
    address = sys.argv[1]
    port = sys.argv[2]


remoteControl.init(address, port)
remoteControl.walk()
remoteControl.close()
