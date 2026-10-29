"""from picamera2 import Picamera2, Preview
import numpy as np"""
from time import sleep, time
from gpiozero import LED, Button
from gpiozero.pins.mock import MockFactory
from gpiozero import Servo
import threading
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
my_servo = "this_is_a_place_holder"
"my_servo = Servo(16, pin_factory=pin_factory)"
#create Picamera2 object for camera functionality
"""picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)"""

buttons = [Up_Arrow, Down_Arrow, Left_Arrow, Right_Arrow, Confirm_Button, Back_Button]

#Turn Power_LED on When code starts up
Power_LED.on()

class Figurine:
    def __init__(self, name, fig_number, UID, screen):
        self.name = name
        self.fig_number = fig_number
        self.UID = UID
        self.screen = screen

    def placed(self):
        # Code to switch screen based on the figurine placed
        pass

fig1 = Figurine('Evangaline', 1, 'UID', 'fig1_screen')
fig2 = Figurine('August', 2, 'UID', 'fig2_screen')
fig3 = Figurine('Elle', 3, 'UID', 'fig3_screen')
fig4 = Figurine('Blythe', 4, 'UID', 'fig4_screen')

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

fig1_basic_Furniture = [
    Furniture('Cherry Bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),
    Furniture('Fluffy Cream Rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),
    Furniture('Cherry Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),
    Furniture('Cherry Tapestry', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),
    Furniture('Cherry Lamp', 'image', FurnitureType('Light', 'pos', 'size'), '7'),
    Furniture('Cherry Sewing Machine', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),
    Furniture('Cream Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),
    Furniture('Dress Form', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Cozy Bean Bag', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Light Wood Flooring', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),
    Furniture('Cream Ribbed Wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),
    Furniture('Box Window with Red Curtains', 'image', FurnitureType('Window', 'pos', 'size'), '15')
]

fig2_basic_Furniture = [
    Furniture('Cozy Bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),
    Furniture('Chai Rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),
    Furniture('Cozy Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),
    Furniture('Cozy Bookshelves', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),
    Furniture('Starry Lamp', 'image', FurnitureType('Light', 'pos', 'size'), '7'),
    Furniture('Basket of Yarn with knit + Crochet needles', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),
    Furniture('Chai Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),
    Furniture('Chai Chair', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Tall Chai Lamp', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Light Wood Flooring', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),
    Furniture('Creamy Leaf Detailed Wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),
    Furniture('Box Window with Cozy Drapes', 'image', FurnitureType('Window', 'pos', 'size'), '15')
]

fig3_basic_Furniture = [
    Furniture('Bubblegum Bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),
    Furniture('Pink Sweet-Heart Rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),
    Furniture('Cream Heart Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),
    Furniture('Pink Posters', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),
    Furniture('Pink Tulip Light', 'image', FurnitureType('Light', 'pos', 'size'), '7'),
    Furniture('Cute Stack of Magazines', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),
    Furniture('Pink Sweet-Heart Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),
    Furniture('Tall Pink Lamp', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Short Pink Bookshelf with fluffy blanket on top', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Fluffy Cream Carpet', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),
    Furniture('Light pink Wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),
    Furniture('Box Window with Pink, Ruffle Curtains', 'image', FurnitureType('Window', 'pos', 'size'), '15')
]

fig4_basic_Furniture = [
    Furniture('Caramel Bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),
    Furniture('Choclate Rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),
    Furniture('Sophisticated Caramel Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),
    Furniture('Sophisticated Painting', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),
    Furniture('Simple Glass Oval Like with Dark wood base', 'image', FurnitureType('Light', 'pos', 'size'), '7'),
    Furniture('Tall Stack of Books', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),
    Furniture('Chocolate Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),
    Furniture('Cozy Reading Chair', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Floor to Ceiling Chocolate Bookshelf', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Dark Oak Flooring', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),
    Furniture('Detailed Coffe Walpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),
    Furniture('Box Window With Chocolate, Silk Drapes', 'image', FurnitureType('Window', 'pos', 'size'), '15')
]

fig1_Furniture = [
    Furniture('Cozy Bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),
    Furniture('Cherry Soda Bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),

    Furniture('Cherry Red Rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),
    Furniture('Cherry Rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),

    Furniture('Cherry Red Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),
    Furniture('Cream Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),

    Furniture('Sewing Sketches', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),
    Furniture('Cherry Record Display', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),

    Furniture('Simple Cozy Light', 'image', FurnitureType('Light', 'pos', 'size'), '7'),
    Furniture('Gummy Bear Chandalier', 'image', FurnitureType('Light', 'pos', 'size'), '7'),

    Furniture('Magazines', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),
    Furniture('Sewing Stuff', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),

    Furniture('Cherry Shaped Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),
    Furniture('Cherry Red Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),

    Furniture('Cherry Lamp', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Cherry Side Table', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Fabric Storage', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Fluffy Chair', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),

    Furniture('Cherry Lamp', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Cherry Side Table', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Fabric Storage', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Fluffy Chair', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),

    Furniture('Fluffy Carpet', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),
    Furniture('Dark Oak Flooring', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),

    Furniture('Cherry Print Wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),
    Furniture('Vine Border Wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),

    Furniture('Charming Arch Window', 'image', FurnitureType('Window', 'pos', 'size'), '15'),
    Furniture('Inticate Frame Window', 'image', FurnitureType('Window', 'pos', 'size'), '15')
]

fig2_Furniture = [
    Furniture('Cozy Bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),
    Furniture('Autumn Bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),

    Furniture('Fluffy Leaf Rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),
    Furniture('Creamy Rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),

    Furniture('Burnt leaves Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),
    Furniture('Cozy Chai Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),

    Furniture('hanging knit', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),
    Furniture('Chai record Display', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),

    Furniture('Autumn glow light', 'image', FurnitureType('Light', 'pos', 'size'), '7'),
    Furniture('Leaf chandalier', 'image', FurnitureType('Light', 'pos', 'size'), '7'),

    Furniture('coffee cup, on top of a notebook', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),
    Furniture('pens/pencils jar etc.', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),

    Furniture('leaf clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),
    Furniture('Cozy Chai Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),

    Furniture('Window bench', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '17'),
    Furniture('Chai Laundry Basket', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('side writing desk', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '7'),
    Furniture('stuffed animal pile', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),

    Furniture('Window bench', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '17'),
    Furniture('Chai Laundry Basket', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('side writing desk', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '7'),
    Furniture('stuffed animal pile', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),

    Furniture('Fluffy carpet', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),
    Furniture('Dark Oak Flooring', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),

    Furniture('leafy wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),
    Furniture('Sophisticated fall wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),

    Furniture('Arch Window', 'image', FurnitureType('Window', 'pos', 'size'), '15'),
    Furniture('Delicate Frame Window', 'image', FurnitureType('Window', 'pos', 'size'), '15')
]

fig3_Furniture = [
    Furniture('Heart Shaped princess bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),
    Furniture('Bubblegum Inset Sofa Bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),

    Furniture('Fluffy pink rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),
    Furniture('Chantilly rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),

    Furniture('pink floor to ceiling closet', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),
    Furniture('cozy chantilly dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),

    Furniture('Lace Doiling Art', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),
    Furniture('Bubblegum Record Display', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),

    Furniture('Pink Bubble Chandalier', 'image', FurnitureType('Light', 'pos', 'size'), '7'),
    Furniture('Pink Glow Gummy Light', 'image', FurnitureType('Light', 'pos', 'size'), '7'),

    Furniture('Makeup Supplies', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),
    Furniture('Digital Camera + Photos', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),

    Furniture('Bubble Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),
    Furniture('Lace Doily Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),

    Furniture('Tall Scarf/Hat Rack', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Bubble lamp', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Giant pink Gummy bear stool', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Cute Shoe rack', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),

    Furniture('Tall Scarf/Hat Rack', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Bubble lamp', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Giant pink Gummy bear stool', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Cute Shoe rack', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),

    Furniture('Light-Wood flooring', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),
    Furniture('Dark Oak Flooring', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),

    Furniture('pink gummy bear wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),
    Furniture('intricate doily wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),

    Furniture('Arch Window', 'image', FurnitureType('Window', 'pos', 'size'), '15'),
    Furniture('Delicate Frame Window', 'image', FurnitureType('Window', 'pos', 'size'), '15')
]

fig4_Furniture = [
    Furniture('Chocolate inset wall bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),
    Furniture('Low Chocolate Coffee twin bed', 'image', FurnitureType('Bed', 'pos', 'size'), '10'),

    Furniture('Chocolate Coffee rug', 'image', FurnitureType('Rug', 'pos', 'size'), '3'),
    Furniture('Sophisiticated tweed rug', 'image', FurnitureType('Rug', 'pos', 'size'), '2'),

    Furniture('Chocolate Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),
    Furniture('Coffee Dresser', 'image', FurnitureType('Dresser', 'pos', 'size'), '5'),

    Furniture('Book posters/collage', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),
    Furniture('Chocolate Record Display', 'image', FurnitureType('Wall Hanging', 'pos', 'size'), '2'),

    Furniture('light', 'image', FurnitureType('Light', 'pos', 'size'), '7'),
    Furniture('light', 'image', FurnitureType('Light', 'pos', 'size'), '7'),

    Furniture('Journaling supplies', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),
    Furniture('Chocolate Caramel Record Player', 'image', FurnitureType('Dresser Acessory', 'pos', 'size'), '2'),

    Furniture('Chocolate Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),
    Furniture('Caramel Clock', 'image', FurnitureType('Clock', 'pos', 'size'), '2'),

    Furniture('Caramel Hat/scarf stand', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Chocolate Hanging chair/reading nook', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Short bookshelf w/blankets on top', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),
    Furniture('Cream/Coffee/Chocolate/Caramel Stuffy basket', 'image', FurnitureType('Side Acessory one', 'pos', 'size'), '4'),

    Furniture('Caramel Hat/scarf stand', 'image', FurnitureType('Side Acessory one', 'pos', 'two'), '4'),
    Furniture('Chocolate Hanging chair/reading nook', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Short bookshelf w/blankets on top', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),
    Furniture('Cream/Coffee/Chocolate/Caramel Stuffy basket', 'image', FurnitureType('Side Acessory two', 'pos', 'size'), '4'),

    Furniture('Light Wood Flooring', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),
    Furniture('Fluffy Carpet', 'image', FurnitureType('Flooring', 'pos', 'size'), '2'),

    Furniture('Dark Oak Paneling', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),
    Furniture('Caramel framed wallpaper', 'image', FurnitureType('Wallpaper', 'pos', 'size'), '2'),

    Furniture('Arch Window', 'image', FurnitureType('Window', 'pos', 'size'), '15'),
    Furniture('Delicate Frame Window', 'image', FurnitureType('Window', 'pos', 'size'), '15')
]

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

fig1_Dressup = [
    Clothing('Sweetheart Tee', 'image', ClothingType('Top', 'pos', 'size'), '5 coins'),
    Clothing('Cherry Tank', 'image', ClothingType('Top', 'pos', 'size'), '4 coins'),
    Clothing('Light Cordoroy Shorts', 'image', ClothingType('Bottoms', 'pos', 'size'), '4 coins'),
    Clothing('Cloudy Ruffle Skirt', 'image', ClothingType('Bottoms', 'pos', 'size'), '5 coins'),
    Clothing('Cherry Mary Janes', 'image', ClothingType('Shoes', 'pos', 'size'), '4 coins'),
    Clothing('Knee High Black Boots', 'image', ClothingType('Shoes', 'pos', 'size'), '5 coins'),
    Clothing('Light Cordoroy Newsboy hat', 'image', ClothingType('Hat', 'pos', 'size'), '5 coins'),
    Clothing('Cherry Headband', 'image', ClothingType('Hat', 'pos', 'size'), '3 coins'),
    Clothing('Sweetheart Necklace', 'image', ClothingType('Acessory', 'pos', 'size'), '2 coins'),
    Clothing('Swan Legwarmers', 'image', ClothingType('Acessory', 'pos', 'size'), '3 coins'),
    Clothing('Cherry Pocket Jeans', 'image', ClothingType('Bottoms', 'pos', 'size'), '4 coins'),
    Clothing('Cherry Tights', 'image', ClothingType('Acessory', 'pos', 'size', '2 coins')),
    Clothing('Darling Cherry Dress', ClothingType('Top', 'pos', 'size', '7 coins'))
]

fig2_Dressup = [
    Clothing('Chai Sweater', 'image', ClothingType('Top', 'pos', 'size'), '5 coins'),
    Clothing('Cozy Tee w/ longsleeves underneath', 'image', ClothingType('Top', 'pos', 'size'), '4 coins'),
    Clothing('Dark Cordoroy Jeans w/ flower embroidery', 'image', ClothingType('Bottoms', 'pos', 'size'), '4 coins'),
    Clothing('Cream Maxi-Skirt', 'image', ClothingType('Bottoms', 'pos', 'size'), '5 coins'),
    Clothing('Chai Sneakers', 'image', ClothingType('Shoes', 'pos', 'size'), '4 coins'),
    Clothing('Chuncky Leather Boots', 'image', ClothingType('Shoes', 'pos', 'size'), '5 coins'),
    Clothing('Dark Cordoroy Newsboy hat', 'image', ClothingType('Hat', 'pos', 'size'), '5 coins'),
    Clothing('Cozy Beanie', 'image', ClothingType('Hat', 'pos', 'size'), '3 coins'),
    Clothing('Chuncky Leather Jacket', 'image', ClothingType('Acessory', 'pos', 'size'), '6 coins'),
    Clothing('Leaf Earings', 'image', ClothingType('Acessory', 'pos', 'size'), '3 coins'),
    Clothing('Leaf Jean Shorts', 'image', ClothingType('Bottoms', 'pos', 'size'), '3 coins'),
    Clothing('Chai Tights', 'image', ClothingType('Acessory', 'pos', 'size'), '2 coins'),
    Clothing('Dreamy Chai Dress', 'image', ClothingType('Top', 'pos', 'size', '7 coins'))
    #cozy = cream/green/yellow/black stripes vibe
]

fig3_Dressup = [
    Clothing('Bubblegum Ruffle Dress', 'image', ClothingType('Top', 'pos', 'size'), '6 coins'),
    Clothing('Chantilly Blouse', 'image', ClothingType('Top', 'pos', 'size'), '4 coins'),
    Clothing('Light-Wash, Mid-Rise, Skinny Jeans', 'image', ClothingType('Bottoms', 'pos', 'size'), '4 coins'),
    Clothing('Bubblegum Ruffle Skirt', 'image', ClothingType('Bottoms', 'pos', 'size'), '5 coins'),
    Clothing('Bubblegum Heels', 'image', ClothingType('Shoes', 'pos', 'size'), '4 coins'),
    Clothing('Mini Carmel Boots', 'image', ClothingType('Shoes', 'pos', 'size'), '5 coins'),
    Clothing('Carmel Ribbon', 'image', ClothingType('Hat', 'pos', 'size'), '5 coins'),
    Clothing('Bow Clips', 'image', ClothingType('Hat', 'pos', 'size'), '3 coins'),
    Clothing('Chantilly Leg-Warmers', 'image', ClothingType('Acessory', 'pos', 'size'), '6 coins'),
    Clothing('Carmel-Ribbon Necklace', 'image', ClothingType('Acessory', 'pos', 'size'), '3 coins'),
    Clothing('Pink Stripes Foldover Shorts', 'image', ClothingType('Bottoms', 'pos', 'size'), '3 coins'),
    Clothing('Bubblegum Tights', 'image', ClothingType('Acessory', 'pos', 'size'), '2 coins'),
    Clothing('Chantilly Dress', 'image', ClothingType('Top', 'pos','size'), '6 coins' )
]

fig4_Dressup = [
    Clothing('Chocolate Waist-Coat, with Cream Blouse', 'image', ClothingType('Top', 'pos', 'size'), '6 coins'),
    Clothing('Carmel Sweater vest, with Coffee Blouse', 'image', ClothingType('Top', 'pos', 'size'), '4 coins'),
    Clothing('Chocolate Midi-Skirt', 'image', ClothingType('Bottoms', 'pos', 'size'), '4 coins'),
    Clothing('Caramel Slacks', 'image', ClothingType('Bottoms', 'pos', 'size'), '5 coins'),
    Clothing('Black Mary-Janes', 'image', ClothingType('Shoes', 'pos', 'size'), '4 coins'),
    Clothing('Knee-High Black Boots', 'image', ClothingType('Shoes', 'pos', 'size'), '5 coins'),
    Clothing('Chocolate Barret', 'image', ClothingType('Hat', 'pos', 'size'), '5 coins'),
    Clothing('Coffe Lace-Ribbon', 'image', ClothingType('Hat', 'pos', 'size'), '3 coins'),
    Clothing('Chocolate Long-Coat', 'image', ClothingType('Acessory', 'pos', 'size'), '6 coins'),
    Clothing('Dark-Chocolate Tights', 'image', ClothingType('Acessory', 'pos', 'size'), '3 coins'),
    Clothing('Chocolate Leather Shorts', ClothingType('Bottoms', 'pos', 'size'), '4 coins'),
    Clothing('Red Wine Tights', ClothingType('Acessory', 'pos', 'size'), '2 coins')
]

#Figure PJ's (What they wear when no Outfit Applied)//No Acessories or hats

fig1_base_outfit = [
    Clothing('Cherry PJ Top', 'image', ClothingType('Top', 'pos', 'size'), 'No Price'),
    Clothing('Cherry PJ Bottoms', 'image', ClothingType('Bottoms', 'pos', 'size'), 'No Price'),
    Clothing('Lace Cherry Socks', 'image', ClothingType('Shoes', 'pos', 'size'), 'No Price')
]

fig2_base_outfit = [
    Clothing('Chai PJ Top', 'image', ClothingType('Top', 'pos', 'size'), 'No Price'),
    Clothing('Chai PJ Bottoms', 'image', ClothingType('Bottoms', 'pos', 'size'), 'No Price'),
    Clothing('Lace Chai Socks', 'image', ClothingType('Shoes', 'pos', 'size'), 'No Price')
]

fig3_base_outfit = [
    Clothing('Bubblegum PJ Top', ClothingType('Top', 'pos', 'size'), 'Top', 'No Price'),
    Clothing('Bubblegum PJ Bottoms', 'image', ClothingType('Bottoms', 'pos', 'size'), 'No Price'),
    Clothing('Lace Chantilly Socks', 'image', ClothingType('Shoes', 'pos', 'size'), 'No Price')
]

fig4_base_outfit = [
    Clothing('Caramel PJ Top', ClothingType('Top', 'pos', 'size'), 'Top', 'No Price'),
    Clothing('Caramel PJ Bottoms', 'image', ClothingType('Bottoms', 'pos', 'size'), 'No Price'),
    Clothing('Lace Chocolate Socks', 'image', ClothingType('Shoes', 'pos', 'size'), 'No Price')
]

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

fig1_song = Music('Cherries', 'audio_file')
fig2_song = Music('My Girl', 'audio_file')
fig3_song = Music('Bubblegum', 'audio_file')
fig4_song = Music('Lofi-Girl Study Beats', 'audio_file')

class Camera:
    def __init__(self, name, overlay_image):
        self.name = name
        self.overlay_image = overlay_image

    def take_photo(self):
        # Code to take a photo with the overlay image
        pass

fig1_overlay = Camera('Cherries', 'image')
fig2_overlay = Camera('Autum Leaves', 'image')
fig3_overlay = Camera('Pink Hearts + Bubbles', 'image')
fig4_overlay = Camera('Books+Quills', 'image')

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

def Up_Arrow_pressed():

    #If on button A:
    # break
    #Elif on button B:
    #  move to button A
    #Elif on button C:
    #   move to button B
    #Elif on button D:
    #   move to button C
    pass

def Down_Arrow_pressed():
    #If on button A:
        # move to button B
        #Elif on button B:
        #  move to button C
        #Elif on button C:
        #   move to button D
        #Elif on button D:
        #   break
    # Down Arrow button pressed
    pass

def Left_Arrow_pressed():
    #If on 'back' button go to button D
    #If on button A-D do nothing
    # Left Arrow button pressed
    pass

def Right_Arrow_pressed():
    #If on button A-D go to 'back'
    #If on 'back' do nothing
    # Right Arrow button pressed
    pass

def Confirm_Button_pressed():
    # Hit Button currently pressed on
    # Confirm Button pressed
    pass

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
    print("\n----------------------------------------------------------------------------------------------\n|                                                                                            |\n|                                                                                            |\n|      --------                                                                              |\n|     | |    | |                 -------------------------------------------------           |\n|     |   |    |                |                   Dress-up                      |          |\n|     | |____| |                |                                                 |          |\n|      --------                  -------------------------------------------------           |\n|        |  |                                                                                |\n|  ------|  |-------             -------------------------------------------------           |\n| |      ----       |           |                    Bedroom                      |          |\n| |                 |           |                                                 |          |\n| |.  |         |.  |            -------------------------------------------------           |\n| |___|         |___|                                                                        |\n| |.  |         |.  |            -------------------------------------------------           |\n| |.  |         |.  |           |                     Music                       |          |\n| |.  |.        |.  |           |                                                 |          |\n| |.  |_________|.  |            -------------------------------------------------           |\n| |___|         |___|                                                                        |\n|.    |.        |                -------------------------------------------------           |\n|.    |.   |.   |               |                     Camera                      |          |\n|.    |.   |.   |               |                                                 |          |\n|.    |.   |.   |                -------------------------------------------------           |\n|     |.   |.   |                                                                            |\n|.    |.   |.   |                                                                            |\n|     |.   |.   |                                                                            |\n|.    |.   |.   |                                                     ------------------     |\n|. ----    |.   ----                                                 |       back       |    |\n| |________|________|                                                 ------------------     |\n----------------------------------------------------------------------------------------------\n")
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
    print("\n----------------------------------------------------------------------------------------------\n|                                                                                            |\n|                                                                                            |\n|      --------                                                                              |\n|     | |    | |                 -------------------------------------------------           |\n|     |   |    |                |                   Dress-up                      |          |\n|     | |____| |                |                                                 |          |\n|      --------                  -------------------------------------------------           |\n|        |  |                                                                                |\n|  ------|  |-------             -------------------------------------------------           |\n| |      ----       |           |                    Bedroom                      |          |\n| |                 |           |                                                 |          |\n| |.  |         |.  |            -------------------------------------------------           |\n| |___|         |___|                                                                        |\n| |.  |         |.  |            -------------------------------------------------           |\n| |.  |         |.  |           |                     Music                       |          |\n| |.  |.        |.  |           |                                                 |          |\n| |.  |_________|.  |            -------------------------------------------------           |\n| |___|         |___|                                                                        |\n|.    |.        |                -------------------------------------------------           |\n|.    |.   |.   |               |                     Camera                      |          |\n|.    |.   |.   |               |                                                 |          |\n|.    |.   |.   |                -------------------------------------------------           |\n|     |.   |.   |                                                                            |\n|.    |.   |.   |                                                                            |\n|     |.   |.   |                                                                            |\n|.    |.   |.   |                                                     ------------------     |\n|. ----    |.   ----                                                 |       back       |    |\n| |________|________|                                                 ------------------     |\n----------------------------------------------------------------------------------------------\n")
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
    print("\n----------------------------------------------------------------------------------------------\n|                                                                                            |\n|                                                                                            |\n|      --------                                                                              |\n|     | |    | |                 -------------------------------------------------           |\n|     |   |    |                |                   Dress-up                      |          |\n|     | |____| |                |                                                 |          |\n|      --------                  -------------------------------------------------           |\n|        |  |                                                                                |\n|  ------|  |-------             -------------------------------------------------           |\n| |      ----       |           |                    Bedroom                      |          |\n| |                 |           |                                                 |          |\n| |.  |         |.  |            -------------------------------------------------           |\n| |___|         |___|                                                                        |\n| |.  |         |.  |            -------------------------------------------------           |\n| |.  |         |.  |           |                     Music                       |          |\n| |.  |.        |.  |           |                                                 |          |\n| |.  |_________|.  |            -------------------------------------------------           |\n| |___|         |___|                                                                        |\n|.    |.        |                -------------------------------------------------           |\n|.    |.   |.   |               |                     Camera                      |          |\n|.    |.   |.   |               |                                                 |          |\n|.    |.   |.   |                -------------------------------------------------           |\n|     |.   |.   |                                                                            |\n|.    |.   |.   |                                                                            |\n|     |.   |.   |                                                                            |\n|.    |.   |.   |                                                     ------------------     |\n|. ----    |.   ----                                                 |       back       |    |\n| |________|________|                                                 ------------------     |\n----------------------------------------------------------------------------------------------\n")
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
    print("\n----------------------------------------------------------------------------------------------\n|                                                                                            |\n|                                                                                            |\n|      --------                                                                              |\n|     | |    | |                 -------------------------------------------------           |\n|     |   |    |                |                   Dress-up                      |          |\n|     | |____| |                |                                                 |          |\n|      --------                  -------------------------------------------------           |\n|        |  |                                                                                |\n|  ------|  |-------             -------------------------------------------------           |\n| |      ----       |           |                    Bedroom                      |          |\n| |                 |           |                                                 |          |\n| |.  |         |.  |            -------------------------------------------------           |\n| |___|         |___|                                                                        |\n| |.  |         |.  |            -------------------------------------------------           |\n| |.  |         |.  |           |                     Music                       |          |\n| |.  |.        |.  |           |                                                 |          |\n| |.  |_________|.  |            -------------------------------------------------           |\n| |___|         |___|                                                                        |\n|.    |.        |                -------------------------------------------------           |\n|.    |.   |.   |               |                     Camera                      |          |\n|.    |.   |.   |               |                                                 |          |\n|.    |.   |.   |                -------------------------------------------------           |\n|     |.   |.   |                                                                            |\n|.    |.   |.   |                                                                            |\n|     |.   |.   |                                                                            |\n|.    |.   |.   |                                                     ------------------     |\n|. ----    |.   ----                                                 |       back       |    |\n| |________|________|                                                 ------------------     |\n----------------------------------------------------------------------------------------------\n")
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

#build actual screen
#----------------------------------------------------------------------------------------------
#|                                                                                            |
#|                                                                                            |
#|      --------                                                                              |
#|     | |    | |                 -------------------------------------------------           |
#|     |   |    |                |                   Dress-up                      |          |
#|     | |____| |                |                                                 |          |
#|      --------                  -------------------------------------------------           |
#|        |  |                                                                                |
#|  ------|  |-------             -------------------------------------------------           |
#| |      ----       |           |                    Bedroom                      |          |
#| |                 |           |                                                 |          |
#| |.  |         |.  |            -------------------------------------------------           |
#| |___|         |___|                                                                        |
#| |.  |         |.  |            -------------------------------------------------           |
#| |.  |         |.  |           |                     Music                       |          |
#| |.  |.        |.  |           |                                                 |          |
#| |.  |_________|.  |            -------------------------------------------------           |
#| |___|         |___|                                                                        |
#|.    |.        |                -------------------------------------------------           |
#|.    |.   |.   |               |                     Camera                      |          |
#|.    |.   |.   |               |                                                 |          |
#|.    |.   |.   |                -------------------------------------------------           |
#|     |.   |.   |                                                                            |
#|.    |.   |.   |                                                                            |
#|     |.   |.   |                                                                            |
#|.    |.   |.   |                                                     ------------------     | 
#|. ----    |.   ----                                                 |       back       |    |
#| |________|________|                                                 ------------------     |
#----------------------------------------------------------------------------------------------

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