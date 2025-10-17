
from spherov2API.spherov2.sphero_edu import SpheroEduAPI

from spherov2API.spherov2 import scanner

from spherov2API.spherov2.types import Color
import time

# Handler for collision/tap events
def on_collision(api, *args, **kwargs):
    print("Collision detected!", args or "", kwargs or "")
    api.stop_roll()
    api.set_main_led(Color(0, 255, 0))  # green flash
    time.sleep(1.5)
    api.set_main_led(Color(0, 0, 0))

def _enable_collision(api):
    # Try common method names across versions
    for name in ("set_collision_detection", "enable_collision_detection", "start_collision_detection"):
        if hasattr(api, name):
            try:
                getattr(api, name)(True)   # some take a bool
            except TypeError:
                getattr(api, name)()       # some take no args
            return True
    return False

def main():
    toy = scanner.find_toy(toy_name="SB-1664")
    if toy is None:
        print("SB-1664 not found. Make sure it’s awake and Bluetooth is enabled.")
        return

    with SpheroEduAPI(toy) as api:
        print("Connected. Enabling collision detection...")
        enabled = _enable_collision(api)
        print(f"Collision detection enabled: {enabled}")

        # Register handler using a string event key
        try:
            api.register_event("collision", lambda *a, **k: on_collision(api, *a, **k))
            print("Registered collision handler.")
        except Exception as e:
            print(f"register_event failed: {e}")
            print("Tip: your version may not support event keys; use accel polling as a fallback.")

        # Roll forward so collisions can occur; Ctrl+C to stop
        try:
            while True:
                api.roll(0, 60, 0.4)  # heading, speed, duration
                time.sleep(0.45)
        except KeyboardInterrupt:
            print("Stopping...")
        finally:
            api.stop_roll()

if __name__ == "__main__":
    main()
