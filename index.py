import time
import keyboard
from PIL import ImageGrab, Image
import geo


def main():
    print("Press Shift + I to capture a screenshot and identify the image.")
    while True:
        if keyboard.is_pressed("shift") and keyboard.is_pressed("i"):
            print("Capturing...")

            # Capture the screen.
            screenshot = ImageGrab.grab(bbox=(114, 89, 1335, 957))

            print("captured")
            print("Identifying...")

            # Call the geo.identify() function with the captured image.
            result = geo.identify(screenshot, 5)



            # Print the result.
            geo.print_results(result)
            print("Identified!")
            # Add a delay to prevent continuous captures on a single keypress.
            time.sleep(1)


if __name__ == "__main__":
    main()
