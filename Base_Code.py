"""from picamera2 import Picamera2, Preview
import numpy as np"""
from time import sleep, time
from gpiozero import LED, Button
from gpiozero.pins.mock import MockFactory
from gpiozero import Servo
"""import RPi.GPIO as GPIO
from pn532 import *
from pn532test.pn532.spi import PN532_SPI"""

pin_factory = MockFactory()

# Initialize LED's and buttons and speaker for user interaction
# Create LED and Button objects
Power_LED = LED(2, pin_factory=pin_factory)
posible_LED_one = LED(3, pin_factory=pin_factory)
posible_LED_two = LED(4, pin_factory=pin_factory)
Up_Arrow = Button(17, pin_factory=pin_factory)
Down_Arrow = Button(27, pin_factory=pin_factory)
Left_Arrow = Button(22, pin_factory=pin_factory)
Right_Arrow = Button(23, pin_factory=pin_factory)
Confirm_Button = Button(24, pin_factory=pin_factory)
Back_Button = Button(25, pin_factory=pin_factory)
# Create a servo object on GPIO pin 17
"my_servo = Servo(16, pin_factory=pin_factory)"
#create Picamera2 object for camera functionality
"""picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)"""

buttons = [Up_Arrow, Down_Arrow, Left_Arrow, Right_Arrow, Confirm_Button, Back_Button]

class Button:
    def __init__(self, pin, pin_factory=pin_factory):
        self.pin = pin
        self.pin_factory = pin_factory
        self.is_pressed = False

    def when_pressed(self):
        self.is_pressed = True
        pass

    def when_released(self):
        self.is_pressed = False
        pass

class Figurine:
    def __init__(self, name, fig_number, UID):
        self.name = name
        self.fig_number = fig_number
        self.UID = UID

    def placed(self):
        # Code to switch screen based on the figurine placed
        pass

class Furniture:
    def __init__(self, name, image, furniture_type, price):
        self.name = name
        self.image = image
        self.furniture_type = furniture_type
        self.price = price

    def place(self, position):
        # Code to place the furniture at the specified position
        pass
    def remove(self):
        # Code to remove the furniture from the scene
        pass
    def obtain(self):
        # Code to obtain the furniture (e.g., add it to inventory)
        pass
    def sell(self):
        # Code to sell the furniture (e.g., remove it from inventory and add currency)
        pass

class FurnitureType:

    def __init__(self, name, position, size):
        self.name = name
        self.position = position
        self.size = size

class Clothing:
    def __init__(self, name, image, clothing_type, price):
        self.name = name
        self.image = image
        self.clothing_type = clothing_type
        self.price = price

class ClothingType:

    def __init__(self, name, position, size):
        self.name = name
        self.position = position
        self.size = size

    def wear(self):
        # Code to wear the clothing item
        pass
    def remove(self):
        # Code to remove the clothing item
        pass
    def obtain(self):
        # Code to obtain the clothing item (e.g., add it to inventory)
        pass
    def sell(self):
        # Code to sell the clothing item (e.g., remove it from inventory and add currency)
        pass

class Music:
    def __init__(self, name, audio_file):
        self.name = name
        self.audio_file = audio_file

    def play(self):
        # Code to play the music
        pass
    def stop(self):
        # Code to stop the music
        pass

class Camera:
    def __init__(self, name, overlay_image):
        self.name = name
        self.overlay_image = overlay_image

    def take_photo(self):
        # Code to take a photo with the overlay image
        pass

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
    elif button == Back_Button:
        print("Back Button pressed")
        Back_Button_pressed()

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
    Confirm_Button.when_pressed = Confirm_Button_pressed
    # Confirm Button pressed

def Back_Button_pressed():
    print("Back Button pressed")
    Back_Button.when_pressed = Back_Button_pressed
    # Back Button pressed

def check_uid_and_switch_screen(uid):
    fig1_UID = [0x04, 0xA2, 0xB3, 0xC4]  # Example UID for fig1
    fig2_UID = [0x05, 0xD5, 0xE6, 0xF7]  # Example UID for fig2
    fig3_UID = [0x06, 0xF8, 0xF9, 0xFA]  # Example UID for fig3
    fig4_UID = [0x07, 0xFB, 0xFC, 0xFD]  # Example UID for fig4

    if uid == fig1_UID:
        print("Switching to fig1 screen...")
        fig1_screen()  # Call the function to switch to fig1 screen
    elif uid == fig2_UID:
        print("Switching to fig2 screen...")
        fig2_screen()  # Call the function to switch to fig2 screen
    elif uid == fig3_UID:
        print("Switching to fig3 screen...")
        fig3_screen()  # Call the function to switch to fig3 screen
    elif uid == fig4_UID:
        print("Switching to fig4 screen...")
        fig4_screen()  # Call the function to switch to fig4 screen
    else:
        print("Unknown UID. No action taken.")

def fig1_screen():
    print("You're on Fig_1 Screen")
    # Code to display fig1 screen with buttons for Dressup, Bedroom, Music, and Camera
    #if dressup button is clicked, call dressup_screen(fig1)
    #if bedroom button is clicked, call bedroom_screen(fig1)
    #if music button is clicked, call music_screen(fig1)
    #if camera button is clicked, call camera_screen(fig1)

    #code for testing purposes
    user_input = int(input("Type '1' for dressup, '2' for bedroom, '3' for music, '4' for camera, and '5' to go back to main screen: "))
    if user_input == 1:
        dressup_screen("fig1")
    elif user_input == 2:
        bedroom_screen("fig1")
    elif user_input == 3:
        music_screen("fig1")
    elif user_input == 4:
        camera_screen("fig1")
    elif user_input == 5:
        main()
    else:
        print("I didn't quite get that.")
        fig1_screen()
    
def fig2_screen():
    print("You're on Fig_2 Screen")
    # Code to display fig2 screen with buttons for Dressup, Bedroom, Music, and Camera
    #if dressup button is clicked, call dressup_screen(fig2)
    #if bedroom button is clicked, call bedroom_screen(fig2)
    #if music button is clicked, call music_screen(fig2)
    #if camera button is clicked, call camera_screen(fig2)
    user_input = int(input("Type '1' for dressup, '2' for bedroom, '3' for music, '4' for camera, and '5' to go back to main screen: "))
    if user_input == 1:
        dressup_screen("fig2")
    elif user_input == 2:
        bedroom_screen("fig2")
    elif user_input == 3:
        music_screen("fig2")
    elif user_input == 4:
        camera_screen("fig2")
    elif user_input == 5:
        main()
    else:
        print("I didn't quite get that.")
        fig2_screen()

def fig3_screen():
    print("You're on Fig_3 Screen")
    # Code to display fig3 screen with buttons for Dressup, Bedroom, Music, and Camera
    #if dressup button is clicked, call dressup_screen(fig3)
    #if bedroom button is clicked, call bedroom_screen(fig3)
    #if music button is clicked, call music_screen(fig3)
    #if camera button is clicked, call camera_screen(fig3)
    user_input = int(input("Type '1' for dressup, '2' for bedroom, '3' for music, '4' for camera, and '5' to go back to main screen: "))
    if user_input == 1:
        dressup_screen("fig3")
    elif user_input == 2:
        bedroom_screen("fig3")
    elif user_input == 3:
        music_screen("fig3")
    elif user_input == 4:
        camera_screen("fig3")
    elif user_input == 5:
        main()
    else:
        print("I didn't quite get that.")
        fig3_screen()

def fig4_screen():
    print("You're on Fig_4 Screen")
    # Code to display fig4 screen with buttons for Dressup, Bedroom, Music, and Camera
    #if dressup button is clicked, call dressup_screen(fig4)
    #if bedroom button is clicked, call bedroom_screen(fig4)
    #if music button is clicked, call music_screen(fig4)
    #if camera button is clicked, call camera_screen(fig4)
    user_input = int(input("Type '1' for dressup, '2' for bedroom, '3' for music, '4' for camera, and '5' to go back to main screen: "))
    if user_input == 1:
        dressup_screen("fig4")
    elif user_input == 2:
        bedroom_screen("fig4")
    elif user_input == 3:
        music_screen("fig4")
    elif user_input == 4:
        camera_screen("fig4")
    elif user_input == 5:
        main()
    else:
        print("I didn't quite get that.")
        fig4_screen()

def dressup_screen(fig):
    print(f"your on dressup_screen for {fig}")
    # Code to display dressup screen with options for different outfits and accessories

    user_input = input("type 'back' to go back")

    if user_input == "back":
        if fig == "fig1":
            fig1_screen()
        elif fig == "fig2":
            fig2_screen()
        elif fig == "fig3":
            fig3_screen()
        else:
            fig4_screen()
    else: 
        dressup_screen(fig)

    pass

def bedroom_screen(fig):
    print(f"your on bedroom_screen for {fig}")
    # Code to display bedroom screen with options for different furniture and accessories

    user_input = input("type 'back' to go back")

    if user_input == "back":
        if fig == "fig1":
            fig1_screen()
        elif fig == "fig2":
            fig2_screen()
        elif fig == "fig3":
            fig3_screen()
        else:
            fig4_screen()
    else: 
        bedroom_screen(fig)
    
def music_screen(fig):
    print(f"your on music_screen for {fig}")

    # Code to display music screen with options to play music, spin record image, and spin fig
    # Start music when play button is clicked and start spinning the record image and fig(motor)
    # if start_button.clicked, call music.play() and start spinning motor
    input("Press Enter to start music")
    while True:
        user_input = input("Press Enter to stop music")
        if user_input == "":
            break
        move_servo()  # Call the function to move the servo
        print("Music is playing and fig is spinning")

    user_input = input("Press Enter to start muisc, and type 'back' to go back")

    if user_input == "":
        music_screen(fig)
    else:
        if fig == "fig1":
            fig1_screen()
        elif fig == "fig2":
            fig2_screen()
        elif fig == "fig3":
            fig3_screen()
        else:
            fig4_screen()

def camera_screen(fig):
    print(f"your on camera_screen for {fig}")

    # Code to display camera screen with options to take photos with fig specific overlay
    # Code to look through photos
    photos_taken = 0

    #Code for testing purposes will be user_input, for final project, will be Back_Button, and use camera to take photos with fig specific overlay
    user_input = input("Press Enter to take a photo or type 'back' to go back")
    while user_input != "back":
        print("Taking photo with figure specific overlay")
        photos_taken += 1
        user_input = input("Press Enter to take another photo or type 'back' to go back")

    if fig == "fig1":
        fig1_screen()
    elif fig == "fig2":
        fig2_screen()
    elif fig == "fig3":
        fig3_screen()
    else:
        fig4_screen()

    #Code for testing purposes will be user_input, for final project, will be Back_Button
    """user_input = input("Press Enter to take a photo or type 'back' to go back")
    while user_input != "back":
        picam2.start_preview(Preview.QTGL)
        picam2.start()
        picam2.capture_file(f"photo_{photos_taken}.jpg")
        photos_taken += 1
        print(f"Photo {photos_taken} taken.")
        user_input = input("Press Enter to take another photo or type 'back' to go back")"""

    """picam2.start_preview(Preview.QTGL)
    picam2.start()
    while Back_Button is not pressed:
        #Will be button later, for testing purposes, will be user_input
        user_input = input("Press Enter to take a photo")
        picam2.capture_file("test.jpg")
        photos_taken += 1"""

def main():
    # Initialize the game window and set up the main loop

    # Initialize the initial idle y2k themed screen
    # Display the initial screen

    # if fig1 is placed, call fig1_screen()
    # if fig2 is placed, call fig2_screen()
    # if fig3 is placed, call fig3_screen()
    # if fig4 is placed, call fig4_screen()
    # Initialize NFC reader to detect fig placement

    #Code for testing purposes will be user_input, for final project, will be NFC reader
    if __name__ == '__main__':
        user_input = input("Type 1 for fig1_screen, 2 for fig2_screen, 3 for fig3_screen, 4 for fig4_screen, or q to quit: ")
        if user_input == "1":
            fig1_screen()
        elif user_input == "2":
            fig2_screen()
        elif user_input == "3":
            fig3_screen()
        elif user_input == "4":
            fig4_screen()
        elif user_input == "q":
            print("Quitting the program.")
            quit()

    """if __name__ == '__main__':
        try:
            pn532 = PN532_SPI(debug=False, reset=20, cs=4)

            ic, ver, rev, support = pn532.get_firmware_version()
            print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

            # Configure PN532 to communicate with MiFare cards
            pn532.SAM_configuration()

            print('Waiting for RFID/NFC card...')
            while True:
                # Check if a card is available to read
                uid = pn532.read_passive_target(timeout=0.5)
                print('.', end="")
                # Try again if no card is available.
                if uid is None:
                    continue
                print('Found card with UID:', [hex(i) for i in uid])
                check_uid_and_switch_screen(uid)  # Call the function to check UID and switch screen
        except Exception as e:
            print(e)
        finally:
            GPIO.cleanup()"""

    # else idle y2k themed screen, with ability to look through photos

main()


#Pseudo Code for the final project
#When fig1 is placed, it will switch to fig1 screen, and so on for fig2, fig3, and fig4.
#On each screen, there will be a 4 buttons to switch to respective screens, themed based off of the fig placed
#Dressup Button: Switch to screen where you will be able to dress up character with different outfits and accessories
#Bedroom Button: Switch to screen where you will be able to decorate the bedroom with different furniture and accessories
#Music Button: Switch to screen where you will be able to play music, record image will spin, and fig will spin
#Camera Button: Switch to screen where you will be able to take photos with fig specific overlay