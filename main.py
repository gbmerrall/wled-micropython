from wled import WLED
import time

# Replace with the IP address of your WLED device
WLED_IP = "192.168.1.10"

def main():
    try:
        wled = WLED(WLED_IP)
        if not wled.update():
            print("Failed to connect to WLED device.")
            return

        print("Turning WLED on...")
        wled.on()
        time.sleep(1)

        print("Setting brightness to 128...")
        wled.brightness(128)
        time.sleep(1)

        print("Setting transition to 5 seconds...")
        wled.transition(50)
        time.sleep(1)

        print("Setting color to blue...")
        wled.color((0, 0, 255))
        time.sleep(1)

        print("Setting effect to 'Blink'...")
        wled.effect(effect_name="Blink")
        time.sleep(1)

        print("Setting effect speed to 200...")
        wled.segments[0].set_speed(200)
        time.sleep(1)

        print("Setting effect intensity to 150...")
        wled.segments[0].set_intensity(150)
        time.sleep(1)

        print("Setting palette to 'Rainbow'...")
        wled.palette(palette_name="Rainbow")
        time.sleep(1)

        print("Saving current state to preset 1...")
        wled.save_preset(1)
        time.sleep(2)

        print("Loading preset 1...")
        wled.preset(1)
        time.sleep(2)

        segments = wled.segments
        if segments:
            print("Toggling the first segment...")
            segments[0].toggle()
            time.sleep(1)

        print("Turning WLED off...")
        wled.off()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()