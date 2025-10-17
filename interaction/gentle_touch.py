
from spherov2API.spherov2.sphero_edu import SpheroEduAPI

from spherov2API.spherov2 import scanner

from spherov2API.spherov2.types import Color
import time

# --- Draw a smile face on the LED matrix ---
def draw_smile(bolt):
    smile_pattern = [
        "00000000",
        "00000000",
        "00100100",
        "00100100",
        "00000000",
        "01000010",
        "00111100",
        "00000000"
    ]
    bolt.display_matrix(smile_pattern)

# --- Main interaction: roll, detect tap, smile and greet ---
def bolt_interaction(bolt):
    print("BOLT is rolling in a circle, waiting for a tap...")

    heading = 0
    speed = 40
    delay = 0.2
    threshold = 1.5  # accelerometer spike threshold
    tapped = False

    while not tapped:
        # Roll in a circle
        bolt.roll(speed, heading, delay)
        heading = (heading + 15) % 360

        # Poll accelerometer for tap
        try:
            x, y, z = bolt.get_acceleration()  # returns [x, y, z]
            if abs(x) > threshold or abs(y) > threshold or abs(z - 1) > threshold:
                tapped = True
                print("Tap detected!")
                bolt.stop()
                break
        except:
            # Skip iteration if sensor read fails
            pass

        time.sleep(delay)

    # Show smile and greet
    draw_smile(bolt)
    bolt.set_main_led(0, 255, 0)  # green smile
    try:
        bolt.say("Nice to meet you!")
    except:
        pass
    time.sleep(3)

    # Fade to blue and end
    bolt.set_main_led(0, 0, 255)
    time.sleep(2)

    # Reset LEDs
    bolt.clear_matrix()
    bolt.set_main_led(0, 0, 0)

def main():
    print("Scanning for BOLT devices...")
    toy = scanner.find_toy(toy_name="SB-1664")

    print(f"Found toy: {toy}")


    with SpheroEduAPI(toy) as bolt:
        print("Connected to Sphero!")
        bolt_interaction(bolt)

if __name__ == "__main__":
    main()
