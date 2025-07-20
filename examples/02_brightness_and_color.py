
from wled import WLED
import time

# Replace with the IP address of your WLED device
WLED_IP = "192.168.1.10"

def main():
    """
    An example to demonstrate setting brightness and color.
    """
    try:
        wled = WLED(WLED_IP)

        print("Connecting to WLED device...")
        if not wled.update():
            print("Failed to connect to WLED device.")
            return

        wled.on()

        print("Setting brightness to 64...")
        wled.brightness(64)
        time.sleep(2)

        print("Setting color to Red...")
        wled.color((255, 0, 0))
        time.sleep(2)

        print("Setting brightness to 255...")
        wled.brightness(255)
        time.sleep(2)

        print("Setting color to Green...")
        wled.color((0, 255, 0))
        time.sleep(2)

        print("Setting color to Blue...")
        wled.color((0, 0, 255))
        time.sleep(2)

        wled.off()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
