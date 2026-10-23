import time

from gpiozero import servo
from gpiozero.pins.mock import MockFactory

# Set the pin factory to MockFactory for testing purposes
# This allows you to test the code without actual hardware

pin_factory = MockFactory()

# Create a servo object on GPIO pin 17
my_servo = servo.Servo(17, pin_factory=pin_factory)

#if music played move servo back and forth
def move_servo():
    # Move the servo to the minimum position
    my_servo.min()
    print("Servo moved to minimum position")
    
    # Wait for a moment
    time.sleep(1)

    my_servo.mid()
    print("Servo moved to center position")
    
    # Move the servo to the maximum position
    my_servo.max()
    print("Servo moved to maximum position")
    
    # Wait for a moment
    time.sleep(1)
    
    my_servo.mid()
    print("Servo moved to center position")