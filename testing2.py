# pyscreenshot/examples/grabfullscreen.py

"Grab the whole screen"
import pyscreenshot as ImageGrab

# grab fullscreen
im = ImageGrab.grab(bbox=(200, 300, 3200, 2200))  # X1,Y1,X2,Y2

# save image file
im.save("fullscreen.png")
