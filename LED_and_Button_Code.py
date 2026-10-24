from gpiozero import LED, Button
from gpiozero.pins.mock import MockFactory
from time import sleep

# Set the pin factory to MockFactory for testing purposes
# This allows you to test the code without actual hardware
pin_factory = MockFactory()

# Create LED and Button objects
Power_LED = LED(2, pin_factory=pin_factory)
posible_LED_one = LED(3, pin_factory=pin_factory)
posible_LED_two = LED(4, pin_factory=pin_factory)
Up_Arrow = Button(17, pin_factory=pin_factory)
Down_Arrow = Button(27, pin_factory=pin_factory)
Left_Arrow = Button(22, pin_factory=pin_factory)
Right_Arrow = Button(23, pin_factory=pin_factory)
Confirm_Button = Button(24, pin_factory=pin_factory)
back_button = Button(25, pin_factory=pin_factory)

buttons = [Up_Arrow, Down_Arrow, Left_Arrow, Right_Arrow, Confirm_Button, back_button]

def button_pressed(button):

    if button == Up_Arrow:
        print("Up Arrow pressed")
        Up_Arrow_pressed()
    elif button == Down_Arrow:
        print("Down Arrow pressed")
        Down_Arrow_pressed()
    elif button == Left_Arrow:
        print("Left Arrow pressed")
        Left_Arrow_pressed()
    elif button == Right_Arrow:
        print("Right Arrow pressed")
        Right_Arrow_pressed()
    elif button == Confirm_Button:
        print("Confirm Button pressed")
        Confirm_Button_pressed()
    elif button == back_button:
        print("Back Button pressed")
        back_button_pressed()

def Up_Arrow_pressed():
    print("Up Arrow pressed")
    # Up Arrow button pressed

def Down_Arrow_pressed():
    print("Down Arrow pressed")
    # Down Arrow button pressed

def Left_Arrow_pressed():
    print("Left Arrow pressed")
    # Left Arrow button pressed

def Right_Arrow_pressed():
    print("Right Arrow pressed")
    # Right Arrow button pressed

def Confirm_Button_pressed():
    print("Confirm Button pressed")
    # Confirm Button pressed

def back_button_pressed():
    print("Back Button pressed")
    # Back Button pressed