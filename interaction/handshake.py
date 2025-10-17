
from spherov2API.spherov2.sphero_edu import SpheroEduAPI

from spherov2API.spherov2 import scanner

from spherov2API.spherov2.types import Color


import time
import pyttsx3
from time import sleep

# --- Draw smile face ---
def draw_smiley(droid):
    yellow = Color(255, 255, 0)  # Yellow smiley face

    # Eyes
    droid.set_matrix_pixel(2, 5, yellow)
    droid.set_matrix_pixel(5, 5, yellow)

    # Mouth (smile curve)
    droid.set_matrix_pixel(2, 2, yellow)
    droid.set_matrix_pixel(3, 1, yellow)
    droid.set_matrix_pixel(4, 1, yellow)
    droid.set_matrix_pixel(5, 2, yellow)

    # Optional: cheeks
    droid.set_matrix_pixel(1, 3, yellow)
    droid.set_matrix_pixel(6, 3, yellow)


# --- Social interaction: handshake detection ---
def shake_interaction(bolt):
    print("BOLT is idle, waiting for a handshake...")

    threshold = 1.5  # lateral acceleration spike threshold
    detected = False
    engine = pyttsx3.init()

    while not detected:
        try:
            x, y, z = bolt.get_acceleration()  # returns [x, y, z]
            # Detect handshake as sudden movement in X or Y
            
            if abs(x) > threshold or abs(y) > threshold:
                
                detected = True
                print("handshake detected!")
                bolt.stop()  # stop any movement
                break
        except:
            pass
        sleep(0.1)

    # Show smile and greet
    draw_smiley(bolt)
    bolt.set_main_led(0, 255, 0)  # green smile
    try:
        engine.say("Hi! Nice to meet you!")
        engine.runAndWait()
    except:
        pass
    sleep(3)

    # Fade to blue and reset
    bolt.set_main_led(0, 0, 255)
    sleep(2)
    bolt.clear_matrix()
    bolt.set_main_led(0, 0, 0)
    print("Interaction complete.")

# --- Main function ---
def main():
    print("Scanning for BOLT devices...")
    devices = scanner.find_toys(toy_names=["SB-1664"], timeout=10)

    if not devices:
        print("No BOLT found. Make sure it’s powered on.")
        return

    toy = devices[0]
    print(f"Found toy: {toy}")

    with SpheroEduAPI(toy) as bolt:
        print("Connected to Sphero!")
        draw_smiley(bolt)
        bolt.scroll_matrix_text("HI I AM BOO", Color(60,206,209),27,True)
        shake_interaction(bolt)

if __name__ == "__main__":
    main()
