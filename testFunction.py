import wiringpi
import time

LED1 = 26
LED2 = 24
LED3 = 22

CAM_LED = 31
LASER = 29
BT_LED = 36

SERVO = 18

#constantS for readability
OUTPUT = 1
PWM = 2
TIME_PER_PWM_TICK = 0.1

def initializePins():
    wiringpi.wiringPiSetupGpio()

    wiringpi.pinMode(LED1, OUTPUT)
    wiringpi.pinMode(LED2, OUTPUT)
    wiringpi.pinMode(LED3, OUTPUT)

    wiringpi.pinMode(CAM_LED, OUTPUT)
    wiringpi.pinMode(LASER, OUTPUT)
    wiringpi.pinMode(BT_LED, OUTPUT)

    wiringpi.pinMode(18, PWM)

def on(pinNum):
    wiringpi.digitalWrite(pinNum, 1)

def off(pinNum):
    wiringpi.digitalWrite(pinNum, 0)

def setPwm(duty):
    wiringpi.pwmWrite(18, duty)

def setAngle(angle):
    if(angle > 179):
        angle = 179
    elif(angle < 0):
        angle = 0

    setPwm(angle) #figure out how to do this?????
