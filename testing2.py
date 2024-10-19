# pyscreenshot/examples/grabfullscreen.py

"Grab the whole screen"
import pyscreenshot as ImageGrab

# grab fullscreen
im = ImageGrab.grab(bbox=(200, 2600, 3200, 4000))  # X1,Y1,X2,Y2

# save image file
im.save("fullscreen.png")
