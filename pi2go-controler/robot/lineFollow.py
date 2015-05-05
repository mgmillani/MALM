#!/usr/bin/env python
# Simple Line Follower Program example for Pi2Go and Pi2Go-Lite

# Must be run as root - sudo python lineFollow.py

import time
import network
import threading
try:
    import pi2go
    piExists = True
except:
    piExists = False
    print "Error loading pi2go."

speed = None


def pi2goInit():
    pi2go.init()
    vsn = pi2go.version()
    if vsn == 1:
        print "Running on Pi2Go"
    else:
        print "Running on Pi2Go-Lite"

    speed = 75

    pi2go.forward(speed)


piStop = True


def pi2goMove():
    if not piStop:
        if pi2go.irLeftLine() == False:
            print "Left"
            pi2go.spinLeft(speed)
        elif pi2go.irRightLine() == False:
            print "Right"
            pi2go.spinRight(speed)
        else:
            print "Straight"
            pi2go.forward(speed)


def pi2goRun():
    pi2goInit()

    try:
        while True:
            pi2goMove()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print "program end:"

    finally:
        pi2go.cleanup()


# thread to move the program
if piExists:
    threading.Thread(target=pi2goRun)


# -----------------------------------------------------------------------------
# From here on is just TCP controls for the remote controler
# -----------------------------------------------------------------------------

conn = network.TextConnection()
port = 9001


# Create a listenin connection
def connectControl():
    conn.whenHungUp(thenCallFunction=disconnected)
    conn.wait(whenHearCall=heard, port=port)


# Message show in case the connection is lost
def disconnected():
    print "Controler disconected"


# Receives control message and sends to robot
def heard(msg):
    if msg == "walk":  # makes robot run
        print "GO!!!"
        piStop = False
    elif msg == "stop":  # stop the robot from running
        print "STOP!!!"
        piStop = True
    else:  # ignore otherwise
        print "command ignored:" + msg


# sends a ack to see if the receiver is still connected
def sendAck():
    while conn.isConnected():
        phrase = "ACK"
        print "me:" + phrase
        try:
            conn.say(phrase)
        except:
            conn.hangUp()
            connectControl()
        time.sleep(2)


connectControl()
threading.Thread(sendAck).Start()
