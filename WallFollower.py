from myro import *

def main():

    seenObstacle = False

    print("Starting loop")
    while(not seenObstacle or (getObstacle("middle") or getObstacle("left") or getObstacle("right"))):
        if getObstacle("middle"):
            seenObstacle = True
            if getObstacle("left"):
                print("Turning right")
                turnRight(1, 0.5)
            elif getObstacle("right"):
                print("Turning left")
                turnLeft(1, 0.5)
        else:
            forward(1, 0.8)

init("COM3")
main()