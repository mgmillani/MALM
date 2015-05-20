#!/usr/bin/env python
# Must be run as root - sudo python controlLineFollow.py

import time
import network
import threading
import normalLineFollow as lf
import random

# thread to move the program
t= threading.Thread(target=lf.pi2goRun)
t.daemon = True
t.start()

# -----------------------------------------------------------------------------
# From here on is just TCP controls for the remote controler
# -----------------------------------------------------------------------------

walkMsg = "walk;"
stopMsg = "stop;"
ack = "ACK"
conn = network.TextConnection()
port = 9001
chanceToWalk = 0.2

# Create a listenin connection
def connectControl():
    conn.whenHungUp(thenCallFunction=disconnected)
    conn.wait(whenHearCall=heard, port=port)


# Message show in case the connection is lost
def disconnected():
    print "Controler disconected"


# Receives control message and sends to robot
def heard(msg):
    if msg == walkMsg:  # makes robot run
        if random.random() < chanceToWalk:
            print "GO!!!"
            lf.piStop = False
    elif msg == stopMsg:  # stop the robot from running
        print "STOP!!!"
        lf.piStop = True
    else:  # ignore otherwise
        print "command ignored:" + msg


# sends a ack to see if the receiver is still connected
def sendAck():
    while True:
        phrase = ack
        try:
            conn.say(phrase)
        except:
            conn.hangUp()
            connectControl()
        time.sleep(2)


def main():
    print "Starting pi2goControler"
    connectControl()
    threading.Thread(target=sendAck).start()


if __name__ == '__main__':
    main()
