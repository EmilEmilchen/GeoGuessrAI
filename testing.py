from pynput.mouse import Listener


def on_move(x, y):
    print(f"Cursor Position: x={x}, y={y}")


def main():
    print("Press Ctrl + C to exit.")

    with Listener(on_move=on_move) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nProgram exited.")


if __name__ == "__main__":
    main()
