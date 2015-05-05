#!/usr/bin/python

import network
import sys

conn = None
port = 9001


def heard(phrase):
    # print "them:" + phrase
    pass


def serverConnect():
    conn.call(sys.argv[1], whenHearCall=heard, port=port)


def chat():
    print "Input a command: < stop or walk >"
    while conn.isConnected():
        phrase = raw_input()
        print "Send:" + phrase
        try:
            conn.say(phrase)
        except:
            conn.hangUp()
            serverConnect()
            conn.say(phrase)


def init():
    serverConnect()


def walk():
    conn.say("walk")


def stop():
    conn.say("stop")


def main():
    print "Remote control program."
    while True:
        conn = network.TextConnection()
        serverConnect()
        chat()
        conn.hangUp()


if __name__ == '__main__':
    main()
