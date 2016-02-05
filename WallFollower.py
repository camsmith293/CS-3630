from myro import *

def scriptedLab1():

    seenObstacle = False

    while(not seenObstacle):
        print("looping")
        forward(1, 0.8)
        if (getObstacle("left") or getObstacle("right") or getObstacle("middle")):
            seenObstacle = True
        print(seenObstacle)

    turnLeft(1, 0.65)

    obstacles = lookAround()
    while(obstacles[1]):
        forward(1, 2.5)
        obstacles = lookAround()

def lookAround():
    seenLeftObstacle = False
    seenRightObstacle = False

    turnLeft(1, 0.5)
    seenLeftObstacle = getObstacle("middle")

    turnRight(1, 1)
    seenRightObstacle = getObstacle("middle")

    turnLeft(1, 0.5)

    return (seenLeftObstacle, seenRightObstacle)


init("COM3")
scriptedLab1()