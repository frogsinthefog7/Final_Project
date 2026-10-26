
"""import RPi.GPIO as GPIO

from pn532 import *

#if fig1_UID found: switch to fig1 screen, etc. etc.

def check_uid_and_switch_screen(uid):
    fig1_UID = [0x04, 0xA2, 0xB3, 0xC4]  # Example UID for fig1
    fig2_UID = [0x05, 0xD5, 0xE6, 0xF7]  # Example UID for fig2
    fig3_UID = [0x06, 0xF8, 0xF9, 0xFA]  # Example UID for fig3
    fig4_UID = [0x07, 0xFB, 0xFC, 0xFD]  # Example UID for fig4

    if uid == fig1_UID:
        print("Switching to fig1 screen...")
        # Code to switch to fig1 screen
    elif uid == fig2_UID:
        print("Switching to fig2 screen...")
        # Code to switch to fig2 screen
    elif uid == fig3_UID:
        print("Switching to fig3 screen...")
        # Code to switch to fig3 screen
    elif uid == fig4_UID:
        print("Switching to fig4 screen...")
        # Code to switch to fig4 screen
    else:
        print("Unknown UID. No action taken.")


if __name__ == '__main__':
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
