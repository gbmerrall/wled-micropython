
from wled import WLED
import time
import random

# Replace with the IP address of your WLED device
WLED_IP = "192.168.1.10"

def main():
    """
    An example to demonstrate controlling effects.
    """
    try:
        wled = WLED(WLED_IP)

        print("Connecting to WLED device...")
        if not wled.update():
            print("Failed to connect to WLED device.")
            return

        wled.on()

        # Set a specific effect by name
        print("Setting effect to 'Solid'...")
        wled.effect(effect_name="Solid")
        wled.color((255, 165, 0))  # Orange
        time.sleep(3)

        # Cycle through a few random effects
        print("Cycling through random effects...")
        for _ in range(5):
            effect_name = random.choice(wled.effects)
            print(f"  - Setting effect to '{effect_name}'")
            wled.effect(effect_name=effect_name)
            time.sleep(4)

        wled.off()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
