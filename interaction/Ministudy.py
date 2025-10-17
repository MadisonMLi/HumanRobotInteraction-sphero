
import time
import pyttsx3
from spherov2 import scanner
from spherov2.types import Color
from spherov2.sphero_edu import SpheroEduAPI


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




    


# New: energetic routine - quick spins, rainbow flashes, and forward/back bounce
def energetic_show(droid):
    RAINBOW = [
        Color(255, 0, 0),    # red
        Color(255, 127, 0),  # orange
        Color(255, 255, 0),  # yellow
        Color(0, 255, 0),    # green
        Color(0, 0, 255),    # blue
        Color(75, 0, 130),   # indigo
        Color(148, 0, 211)   # violet
    ]

    # Quick rapid spins
    for _ in range(3):
        droid.spin(1440, 1.0)   # fast spin for 1s
        time.sleep(0.15)

    # Flash rainbow on main LED rapidly
    for _ in range(5):
        for col in RAINBOW:
            droid.set_main_led(col)
            time.sleep(0.07)

    # Energetic bounce forward/backward
    for _ in range(6):
        droid.roll(0, 140, 0.20)   # forward short burst
        time.sleep(0.22)
        droid.stop_roll()
        time.sleep(0.06)
        droid.roll(180, 140, 0.20) # backward short burst
        time.sleep(0.22)
        droid.stop_roll()
        time.sleep(0.06)

    # Finale: spin while cycling LEDs quickly
    droid.spin(1080, 1.5)
    for col in RAINBOW:
        droid.set_main_led(col)
        time.sleep(0.06)

    droid.set_main_led(Color(0, 0, 0))


def main():
    print("Scanning for Sphero BOLT...")
    toy = scanner.find_toy(toy_name="SB-1664")

    engine = pyttsx3.init()



    with SpheroEduAPI(toy) as droid:
 
       
        # replace existing simple LED sequence / spin with energetic routine
        energetic_show(droid)

        # Scroll a word    
        droid.scroll_matrix_text("CONGRATS", Color(60,206,209),25,True)  # Green text
        time.sleep(1)
    


        # Show smiley face
        droid.clear_matrix()
        draw_smiley(droid)
        time.sleep(3)


        # Turn off LEDs after done
        droid.set_main_led(Color(0, 0, 0))
        droid.clear_matrix()
        print("done!")


if __name__ == "__main__":
    main()
