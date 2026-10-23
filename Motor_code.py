from gpiozero import servo
from gpiozero.pins.mock import MockFactory

# Set the pin factory to MockFactory for testing purposes
# This allows you to test the code without actual hardware

pin_factory = MockFactory()

