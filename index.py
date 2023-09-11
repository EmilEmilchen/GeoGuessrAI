import time
import keyboard
from PIL import ImageGrab, Image
import geo


def main():
    print("Press Shift + I to capture a screenshot and identify the image.")
    while True:
        if keyboard.is_pressed("shift") and keyboard.is_pressed("i"):
            # Wait for the Shift and I keys to be released to avoid multiple captures.
            keyboard.wait("shift+i")

            # Capture the screenshot from coordinates (10, 10) to (100, 100).
            screenshot = ImageGrab.grab(bbox=(10, 10, 100, 100))

            # Call the geo.identify() function with the captured image.
            result = geo.identify(screenshot, 5)

            # Print the result.
            geo.print_results(result)

            screenshot.show()

            # Add a delay to prevent continuous captures on a single keypress.
            time.sleep(1)


if __name__ == "__main__":
    main()
