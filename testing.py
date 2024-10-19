import evdev
from evdev import InputDevice, ecodes

# Set screen resolution (change according to your screen)
screen_width = 1920
screen_height = 1080

# Start at the middle of the screen
x, y = screen_width // 2, screen_height // 2

# Open the mouse input device
device = InputDevice('/dev/input/event22')  # Replace 'XX' with the correct event number

print(f"Tracking mouse coordinates. Initial position: {x}, {y}")

for event in device.read_loop():
    if event.type == ecodes.EV_REL:
        if event.code == ecodes.REL_X:
            x += event.value
        elif event.code == ecodes.REL_Y:
            y += event.value

        # Ensure the position stays within screen boundaries
        x = max(0, min(screen_width, x))
        y = max(0, min(screen_height, y))

        print(f"Mouse position: ({x}, {y})")
