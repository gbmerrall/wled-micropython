
from wled import WLED
import time

# Replace with the IP address of your WLED device
WLED_IP = "192.168.1.10"

def main():
    """
    An example to demonstrate working with segments.
    This assumes you have at least two segments configured in WLED.
    """
    try:
        wled = WLED(WLED_IP)

        print("Connecting to WLED device...")
        if not wled.update():
            print("Failed to connect to WLED device.")
            return

        wled.on()
        segments = wled.segments

        if len(segments) < 2:
            print("This example requires at least 2 segments to be configured.")
            wled.off()
            return

        print(f"Found {len(segments)} segments.")

        # Control segment 0
        print("Controlling Segment 0...")
        segment0 = segments[0]
        segment0.on()
        segment0.color((255, 0, 0)) # Red
        segment0.effect(effect_name="Blink")
        time.sleep(3)

        # Control segment 1
        print("Controlling Segment 1...")
        segment1 = segments[1]
        segment1.on()
        segment1.color((0, 0, 255)) # Blue
        segment1.effect(effect_name="Wipe")
        time.sleep(3)

        # Toggle segment 0
        print("Toggling Segment 0 off...")
        segment0.off()
        time.sleep(2)

        print("Toggling Segment 0 on...")
        segment0.on()
        time.sleep(2)

        wled.off()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
