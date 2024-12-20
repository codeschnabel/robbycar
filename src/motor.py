from machine import Pin, PWM
import time

# ENA = Pin(0, Pin.OUT)  # GP0 - PWM Pin für Geschwindigkeit (ENA)
# IN1 = Pin(1, Pin.OUT)  # GP1 - Richtungspin 1 (IN1)
# IN2 = Pin(2, Pin.OUT)  # GP2 - Richtungspin 2 (IN2)

# # Erstelle ein PWM-Objekt für den ENA-Pin (PWM für Geschwindigkeit)
# IN1.value(1)
# IN2.value(0)

# pwm = PWM(ENA)
# pwm.freq(15000)
# pwm.duty_u16(65000)

# time.sleep(5)

# pwm.duty_u16(0)
# IN1.value(0)
# IN2.value(0)

class Motor:

    ena_pin: Pin
    in1_pin: Pin
    in2_pin: Pin

    __pwm_frequency = 15000

    def __init__(self, ena_pin: Pin, in1_pin: Pin, in2_pin: Pin):
        self.ena_pin = ena_pin
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin


def motor_forward(motor: Motor, speed: int):
    motor.in1_pin.value(1)
    motor.in2_pin.value(0)
    pwm = PWM(motor.ena_pin)
    pwm.freq(motor.__pwm_frequency)
    pwm.duty_u16(speed)

def motor_backward(motor: Motor, speed: int):
    motor.in1_pin.value(0)
    motor.in2_pin.value(1)
    pwm = PWM(motor.ena_pin)
    pwm.freq(motor.__pwm_frequency)
    pwm.duty_u16(speed)

def motor_stop(motor: Motor):
    pwm = PWM(motor.ena_pin)
    pwm.duty_u16(0)
    motor.in1_pin.value(0)
    motor.in2_pin.value(0)