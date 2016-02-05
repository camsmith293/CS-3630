from myro import *

def sensorTest():
    while True:
        print(getObstacle("left"), getObstacle("right"), getObstacle("middle"))

init("COM3")
setForwardness(1)
sensorTest()