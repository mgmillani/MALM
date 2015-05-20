#!/usr/bin/env python
import time

try:
    import pi2go
    piExists = True
except:
    raise
    piExists = False
    print "Error loading pi2go."
    

speed = None
piStop = True


def pi2goInit():
    print "pi2go Init"
    global piStop
    global speed

    piStop = True
    
    if piExists:
        pi2go.init()
        vsn = pi2go.version()
        if vsn == 1:
            print "Running on Pi2Go"
        else:
            print "Running on Pi2Go-Lite"

        speed = 50

        #pi2go.forward(speed)
    else:  # function place holder in case the program is not running on pi2go
        demo()


def pi2goMove():
    #print "pi2go Move"
    if not piStop:
        if pi2go.irLeftLine() == False:
            #print "Left"
            pi2go.turnForward(0.3*speed, speed)
        elif pi2go.irRightLine() == False:
            #print "Right"
            pi2go.turnForward(speed, 0.3*speed)
        else:
            #print "Straight"
            pi2go.forward(speed)
    else:
        pi2go.forward(0)


def pi2goRun():
    print "pi2go Run"
    pi2goInit()

    try:
        while True:
            pi2goMove()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print "program end:"
	raise
    finally:
        pi2go.cleanup()


def demo():
    while True:
        if piStop:
            print "Robot paused"
        else:
            print "Robot running"
        time.sleep(2)
def main():
    print "Starting standalone"
    pi2goRun()


if __name__ == '__main__':
    main()
