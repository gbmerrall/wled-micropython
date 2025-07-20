# WLED MicroPython Library

A MicroPython library for controlling WLED devices over the JSON API.

This library is designed to be compatible with MicroPython and provides a simple interface for controlling your WLED devices.

## Installation

1.  Copy the `wled.py` file to your MicroPython device.
2.  Ensure you have the `urequests` library installed. You can install it using `upip`:

```bash
import upip
upip.install('micropython-urequests')
```

Note that as of April 20254 urequests is now requests but urequests still works until removed
some time in the future. 

## Usage

Here's a basic example of how to use the library:

```python
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

        print("Setting color to red...")
        wled.color((255, 0, 0))
        time.sleep(1)

        print("Turning WLED off...")
        wled.off()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

## WLED Class

The `WLED` class is the main entry point for controlling your WLED device.

### `__init__(self, ip)`

Initializes a new WLED device.

-   `ip` (str): The IP address of the WLED device.

### `update(self)`

Fetches the latest state and info from the WLED device. This should be called before accessing the `state`, `info`, `effects`, or `palettes` attributes.

### `on(self)`

Turns the WLED device on.

### `off(self)`

Turns the WLED device off.

### `toggle(self)`

Toggles the power state of the WLED device.

### `brightness(self, value)`

Sets the brightness of the WLED device.

-   `value` (int): The brightness value (0-255).

### `transition(self, value)`

Sets the transition time for state changes.

-   `value` (int): The transition time in 100ms units.

### `preset(self, preset_id)`

Loads a preset.

-   `preset_id` (int): The ID of the preset to load.

### `save_preset(self, preset_id)`

Saves the current state to a preset.

-   `preset_id` (int): The ID of the preset to save.

### `playlist(self, playlist_id)`

Loads a playlist.

-   `playlist_id` (int): The ID of the playlist to load.

### `reboot(self)`

Reboots the WLED device.

### `set_live(self, live)`

Sets the live mode.

-   `live` (bool): `True` to enable live mode, `False` to disable.

### `set_time(self, time)`

Sets the time on the WLED device.

-   `time` (int): The Unix timestamp.

### `set_main_segment(self, segment_id)`

Sets the main segment.

-   `segment_id` (int): The ID of the segment to set as the main segment.

### `color(self, rgb)`

Sets the color of the main segment.

-   `rgb` (tuple): A tuple of RGB values (e.g., `(255, 0, 0)`).

### `effect(self, effect_id=None, effect_name=None)`

Sets the effect of the main segment.

-   `effect_id` (int): The ID of the effect.
-   `effect_name` (str): The name of the effect.

### `palette(self, palette_id=None, palette_name=None)`

Sets the palette of the main segment.

-   `palette_id` (int): The ID of the palette.
--   `palette_name` (str): The name of the palette.

### `segments`

A property that returns a list of `Segment` objects.

## Segment Class

The `Segment` class represents a single segment on the WLED device.

### `on(self)`

Turns the segment on.

### `off(self)`

Turns the segment off.

### `toggle(self)`

Toggles the power state of the segment.

### `brightness(self, value)`

Sets the brightness of the segment.

-   `value` (int): The brightness value (0-255).

### `color(self, rgb, secondary_rgb=None, tertiary_rgb=None)`

Sets the color of the segment.

-   `rgb` (tuple): A tuple of RGB values for the primary color.
-   `secondary_rgb` (tuple): A tuple of RGB values for the secondary color.
-   `tertiary_rgb` (tuple): A tuple of RGB values for the tertiary color.

### `effect(self, effect_id=None, effect_name=None)`

Sets the effect of the segment.

-   `effect_id` (int): The ID of the effect.
-   `effect_name` (str): The name of the effect.

### `palette(self, palette_id=None, palette_name=None)`

Sets the palette of the segment.

-   `palette_id` (int): The ID of the palette.
-   `palette_name` (str): The name of the palette.

### `set_speed(self, speed)`

Sets the effect speed.

-   `speed` (int): The speed value (0-255).

### `set_intensity(self, intensity)`

Sets the effect intensity.

-   `intensity` (int): The intensity value (0-255).

### `set_cct(self, cct)`

Sets the color temperature.

-   `cct` (int): The color temperature value.

### `set_grouping(self, grouping)`

Sets the grouping of LEDs.

-   `grouping` (int): The grouping value.

### `set_spacing(self, spacing)`

Sets the spacing between LEDs.

-   `spacing` (int): The spacing value.

### `set_offset(self, offset)`

Sets the offset of the segment.

-   `offset` (int): The offset value.

### `freeze(self)`

Freezes the effect on the segment.

### `unfreeze(self)`

Unfreezes the effect on the segment.

### `select(self)`

Selects the segment.

### `deselect(self)`

Deselects the segment.

### `reverse(self)`

Reverses the direction of the effect.

### `unreverse(self)`

Sets the effect direction to normal.

### `mirror(self)`

Mirrors the effect on the segment.

### `unmirror(self)`

Disables mirroring on the segment.

## Acknowledgements

This library was developed by referencing the [wled-json-api-library](https://github.com/paul-fornage/wled-json-api-library) Rust library by paul-fornage.
