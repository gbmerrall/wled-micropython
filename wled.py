import urequests
import ujson

class WLED:
    def __init__(self, ip):
        self.ip = ip
        self.url = f"http://{ip}/json"
        self.state = {}
        self.info = {}
        self.effects = []
        self.palettes = []

    def request(self, data=None):
        try:
            if data:
                response = urequests.post(self.url, json=data)
            else:
                response = urequests.get(self.url)
            
            json_data = response.json()
            response.close()
            return json_data
        except Exception as e:
            print(f"Request failed: {e}")
            return None

    def update(self):
        data = self.request()
        if data:
            self.state = data.get("state", {})
            self.info = data.get("info", {})
            self.effects = data.get("effects", [])
            self.palettes = data.get("palettes", [])
            return True
        return False

    def on(self):
        return self.request({"on": True})

    def off(self):
        return self.request({"on": False})

    def toggle(self):
        return self.request({"on": "t"})

    def brightness(self, value):
        return self.request({"bri": value})

    def transition(self, value):
        return self.request({"transition": value})

    def preset(self, preset_id):
        return self.request({"ps": preset_id})

    def save_preset(self, preset_id):
        return self.request({"psave": preset_id})

    def playlist(self, playlist_id):
        return self.request({"pl": playlist_id})

    def reboot(self):
        return self.request({"rb": True})

    def set_live(self, live):
        return self.request({"live": live})

    def set_time(self, time):
        return self.request({"time": time})

    def set_main_segment(self, segment_id):
        return self.request({"mainseg": segment_id})

    def color(self, rgb):
        return self.request({"seg": [{"col": [rgb]}]})

    def effect(self, effect_id=None, effect_name=None):
        if effect_id is not None:
            return self.request({"seg": [{"fx": effect_id}]})
        elif effect_name is not None:
            if not self.effects:
                self.update()
            if effect_name in self.effects:
                effect_id = self.effects.index(effect_name)
                return self.request({"seg": [{"fx": effect_id}]})
        return None

    def palette(self, palette_id=None, palette_name=None):
        if palette_id is not None:
            return self.request({"seg": [{"pal": palette_id}]})
        elif palette_name is not None:
            if not self.palettes:
                self.update()
            if palette_name in self.palettes:
                palette_id = self.palettes.index(palette_name)
                return self.request({"seg": [{"pal": palette_id}]})
        return None

    @property
    def segments(self):
        if not self.state:
            self.update()
        return [Segment(self, s["id"]) for s in self.state.get("seg", [])]


class Segment:
    def __init__(self, wled, segment_id):
        self.wled = wled
        self.segment_id = segment_id

    def on(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "on": True}]})

    def off(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "on": False}]})

    def toggle(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "on": "t"}]})

    def brightness(self, value):
        return self.wled.request({"seg": [{"id": self.segment_id, "bri": value}]})

    def color(self, rgb, secondary_rgb=None, tertiary_rgb=None):
        colors = [rgb]
        if secondary_rgb:
            colors.append(secondary_rgb)
        if tertiary_rgb:
            colors.append(tertiary_rgb)
        return self.wled.request({"seg": [{"id": self.segment_id, "col": colors}]})

    def effect(self, effect_id=None, effect_name=None):
        if effect_id is not None:
            return self.wled.request({"seg": [{"id": self.segment_id, "fx": effect_id}]})
        elif effect_name is not None:
            if not self.wled.effects:
                self.wled.update()
            if effect_name in self.wled.effects:
                effect_id = self.wled.effects.index(effect_name)
                return self.wled.request({"seg": [{"id": self.segment_id, "fx": effect_id}]})
        return None

    def palette(self, palette_id=None, palette_name=None):
        if palette_id is not None:
            return self.wled.request({"seg": [{"id": self.segment_id, "pal": palette_id}]})
        elif palette_name is not None:
            if not self.wled.palettes:
                self.wled.update()
            if palette_name in self.wled.palettes:
                palette_id = self.wled.palettes.index(palette_name)
                return self.wled.request({"seg": [{"id": self.segment_id, "pal": palette_id}]})
        return None
    
    def set_speed(self, speed):
        return self.wled.request({"seg": [{"id": self.segment_id, "sx": speed}]})

    def set_intensity(self, intensity):
        return self.wled.request({"seg": [{"id": self.segment_id, "ix": intensity}]})

    def set_cct(self, cct):
        return self.wled.request({"seg": [{"id": self.segment_id, "cct": cct}]})

    def set_grouping(self, grouping):
        return self.wled.request({"seg": [{"id": self.segment_id, "grp": grouping}]})

    def set_spacing(self, spacing):
        return self.wled.request({"seg": [{"id": self.segment_id, "spc": spacing}]})

    def set_offset(self, offset):
        return self.wled.request({"seg": [{"id": self.segment_id, "of": offset}]})

    def freeze(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "frz": True}]})

    def unfreeze(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "frz": False}]})

    def select(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "sel": True}]})

    def deselect(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "sel": False}]})

    def reverse(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "rev": True}]})

    def unreverse(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "rev": False}]})

    def mirror(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "mi": True}]})

    def unmirror(self):
        return self.wled.request({"seg": [{"id": self.segment_id, "mi": False}]})