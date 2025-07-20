
from wled import WLED
import time

# Replace with the IP address of your WLED device
WLED_IP = "192.168.1.10"

def main():
    """
    A simple example to turn the WLED device on and off.
    """
    try:
        wled = WLED(WLED_IP)

        print("Connecting to WLED device...")
        if not wled.update():
            print("Failed to connect to WLED device.")
            return

        print("Turning WLED on...")
        wled.on()
        time.sleep(2)

        print("Turning WLED off...")
        wled.off()
        time.sleep(2)

        print("Toggling WLED...")
        wled.toggle()
        time.sleep(2)
        wled.toggle()


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
