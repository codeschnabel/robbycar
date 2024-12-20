from machine import Pin
from utime import sleep

LED = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        LED.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
LED.off()
print("Finished.")