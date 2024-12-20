from machine import Pin, PWM, ADC
from motor import Motor, motor_forward
import time


joystick = ADC(26) # Pin 26 = ADC0

# Joystick constants
JOYSTICK_MIN = 0
JOYSTICK_CENTER = 65535 / 2 
JOYSTICK_MAX = 65535

# Read initial joystick value
initialValue = joystick.read_u16()
print (initialValue)

motor = Motor(Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT))

while True:
    jostickValue = joystick.read_u16()
    print(str(initialValue) + " " + str(jostickValue))
    motor_forward(motor, jostickValue)
    time.sleep(0.1)

#offset = initialValue - 0.5

def control_motor(value):
    global initialValue
    # Swap axis direction if joystick is mounted in reverse position
    invertedValue = (value - 1) * -1

    if value > initialValue:
        higherRange = joystickMax - initialValue
        percentageInHigherRange = (value - initialValue) * 100 / higherRange
        fixedValue = percentageInHigherRange * joystickMax / 100
        fixedRoundedValue = round(fixedValue * 100) / 100

        # motor1_IN1.value(0)  # Motor direction forward
        # motor1_IN2.value(1)  # Motor direction reverse
        # pwm_motor.duty(512)  # Set motor speed (adjust PWM value as needed)
    else:
        lowerRange = initialValue
        percentageInLowerRange = value * 100 / lowerRange
        fixedValue = percentageInLowerRange * joystickMiddle / 100
        fixedRoundedValue = round(fixedValue * 100) / 100

    print("ADC0: ", fixedRoundedValue)
    time.sleep(0.1)
