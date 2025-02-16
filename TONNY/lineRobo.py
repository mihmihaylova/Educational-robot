from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep
robot = KitronikPicoRobotBuggy()

def green():
    robot.setLED(0, robot.GREEN)
    robot.setLED(1, robot.GREEN)
    robot.setLED(2, robot.GREEN)
    robot.setLED(3, robot.GREEN)
    robot.show()
    
def red():
    robot.setLED(0, robot.RED)
    robot.setLED(1, robot.RED)
    robot.setLED(2, robot.RED)
    robot.setLED(3, robot.RED)
    robot.show()
    
def lightTurnOff():
    robot.setLED(0, robot.BLACK)
    robot.setLED(1, robot.BLACK)
    robot.setLED(2, robot.BLACK)
    robot.setLED(3, robot.BLACK)
    robot.show()
    
def buzzer():
    robot.beepHorn()
        

def headLights():
    robot.setLED(0, (50, 50, 50)) 
    robot.setLED(1, (50, 50, 50)) 
    robot.setLED(2, (50, 0, 0))   
    robot.setLED(3, (50, 0, 0))  
    robot.show()

def forward(speed):
    robot.motorOn("l", "f", speed) 
    robot.motorOn("r", "f", speed) 
    
def turnLeft(speed):
    robot.motorOn("l", "r", speed)
    robot.motorOn("r", "f", speed) 
    
def turnRight(speed):
    robot.motorOn("l", "f", speed) 
    robot.motorOn("r", "r", speed)

def stop():
    robot.motorOff("l")
    robot.motorOff("r")

headLights()


def next_mark():
    while True:
        leftSensor  = robot.getRawLFValue("l")
        rightSensor = robot.getRawLFValue("r")
        centerSensor = robot.getRawLFValue("c")
        print(leftSensor , " " , centerSensor ," " , rightSensor)
        if(centerSensor < 20000):
            if(leftSensor < (rightSensor)): # turn right
                turnRight(0.5)
            elif (rightSensor <  (leftSensor)): # turn left
                turnLeft(0.5)
        elif(centerSensor > 30000 and rightSensor > 30000 and leftSensor > 30000):
            stop()
            forward(0.5)
            sleep(0.05)
            stop()
            lightTurnOff()
            break
            
        else:
            forward(0.5)
        sleep(0.05)


