
from wled import WLED
import time
import random

# Replace with the IP address of your WLED device
WLED_IP = "192.168.1.10"

def main():
    """
    An example to demonstrate controlling palettes.
    """
    try:
        wled = WLED(WLED_IP)

        print("Connecting to WLED device...")
        if not wled.update():
            print("Failed to connect to WLED device.")
            return

        wled.on()
        wled.effect(effect_name="Chase") # An effect that shows palettes well

        # Set a specific palette by name
        print("Setting palette to 'Ocean'...")
        wled.palette(palette_name="Ocean")
        time.sleep(3)

        # Cycle through a few random palettes
        print("Cycling through random palettes...")
        for _ in range(5):
            palette_name = random.choice(wled.palettes)
            print(f"  - Setting palette to '{palette_name}'")
            wled.palette(palette_name=palette_name)
            time.sleep(4)

        wled.off()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
