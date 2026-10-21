

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


def fig1_screen():
    # Code to display fig1 screen with buttons for Dressup, Bedroom, Music, and Camera
    #if dressup button is clicked, call dressup_screen(fig1)
    #if bedroom button is clicked, call bedroom_screen(fig1)
    #if music button is clicked, call music_screen(fig1)
    #if camera button is clicked, call camera_screen(fig1)
    pass

def fig2_screen():
    # Code to display fig2 screen with buttons for Dressup, Bedroom, Music, and Camera
    #if dressup button is clicked, call dressup_screen(fig2)
    #if bedroom button is clicked, call bedroom_screen(fig2)
    #if music button is clicked, call music_screen(fig2)
    #if camera button is clicked, call camera_screen(fig2)
    pass

def fig3_screen():
    # Code to display fig3 screen with buttons for Dressup, Bedroom, Music, and Camera
    #if dressup button is clicked, call dressup_screen(fig3)
    #if bedroom button is clicked, call bedroom_screen(fig3)
    #if music button is clicked, call music_screen(fig3)
    #if camera button is clicked, call camera_screen(fig3)
    pass

def fig4_screen():
    # Code to display fig4 screen with buttons for Dressup, Bedroom, Music, and Camera
    #if dressup button is clicked, call dressup_screen(fig4)
    #if bedroom button is clicked, call bedroom_screen(fig4)
    #if music button is clicked, call music_screen(fig4)
    #if camera button is clicked, call camera_screen(fig4)
    pass

def dressup_screen(fig):
    # Code to display dressup screen with options for different outfits and accessories
    pass

def bedroom_screen(fig):
    # Code to display bedroom screen with options for different furniture and accessories
    pass

def music_screen(fig):
    # Code to display music screen with options to play music, spin record image, and spin fig
    # Start music when play button is clicked and start spinning the record image and fig(motor)
    # if start_button.clicked, call music.play() and start spinning motor
    pass

def camera_screen(fig):
    # Code to display camera screen with options to take photos with fig specific overlay
    # Code to look through photos
    
    pass

def main():
    # Initialize the game window and set up the main loop
    # Initialize camera, music, furniture, and clothing objects
    # Initialize NFC reader to detect fig placement
    # Initialize LED's and buttons and speaker for user interaction
    # Initialize the initial screen with options to place fig1, fig2, fig3, or fig4
    # Display the initial screen
    # if fig1 is placed, call fig1_screen()
    # if fig2 is placed, call fig2_screen()
    # if fig3 is placed, call fig3_screen()
    # if fig4 is placed, call fig4_screen()
    # else idle y2k themed screen, with ability to look through photos
    pass

#Pseudo Code for the final project
#When fig1 is placed, it will switch to fig1 screen, and so on for fig2, fig3, and fig4.
#On each screen, there will be a 4 buttons to switch to respective screens, themed based off of the fig placed
#Dressup Button: Switch to screen where you will be able to dress up character with different outfits and accessories
#Bedroom Button: Switch to screen where you will be able to decorate the bedroom with different furniture and accessories
#Music Button: Switch to screen where you will be able to play music, record image will spin, and fig will spin
#Camera Button: Switch to screen where you will be able to take photos with fig specific overlay