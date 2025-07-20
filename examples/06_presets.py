
from wled import WLED
import time

# Replace with the IP address of your WLED device
WLED_IP = "192.168.1.10"

def main():
    """
    An example to demonstrate saving and loading presets.
    """
    try:
        wled = WLED(WLED_IP)

        print("Connecting to WLED device...")
        if not wled.update():
            print("Failed to connect to WLED device.")
            return

        # Setup a state to save
        print("Setting up a state to save as a preset...")
        wled.on()
        wled.color((128, 0, 128)) # Purple
        wled.effect(effect_name="Fireworks")
        wled.brightness(150)
        time.sleep(2)

        # Save the current state to preset 1
        # Note: This will overwrite any existing preset at this slot.
        PRESET_ID = 1
        print(f"Saving current state to preset {PRESET_ID}...")
        wled.save_preset(PRESET_ID)
        time.sleep(2)

        # Change the state to something different
        print("Changing the state to something different...")
        wled.color((0, 255, 0)) # Green
        wled.effect(effect_name="Solid")
        time.sleep(3)

        # Load the preset
        print(f"Loading preset {PRESET_ID}...")
        wled.preset(PRESET_ID)
        time.sleep(3)

        wled.off()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
