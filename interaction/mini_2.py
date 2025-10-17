
import time
import pyttsx3
from spherov2 import scanner
from spherov2.types import Color
from spherov2.sphero_edu import SpheroEduAPI

def draw_sad(droid):
    yellow = Color(255, 255, 0)  # Yellow face
    face_blue = Color(30, 100, 180)
    white = Color(255, 255, 255)
    tear = Color(0, 170, 255)
    dark = Color(0, 30, 70)

    droid.clear_matrix()
    droid.set_main_led(face_blue)


    # eyes (white with dark pupils)
    droid.set_matrix_pixel(2, 5, yellow)
    droid.set_matrix_pixel(5, 5, yellow)
    droid.set_matrix_pixel(2, 5, yellow)   # small pupil (overwrites center for wet look)
    droid.set_matrix_pixel(5, 5, yellow)

    # Mouth (sad curve)
    droid.set_matrix_pixel(2, 1, yellow)
    droid.set_matrix_pixel(3, 2, yellow)
    droid.set_matrix_pixel(4, 2, yellow)
    droid.set_matrix_pixel(5, 1, yellow)
     # tears under each eye
    droid.set_matrix_pixel(2, 4, tear)
    droid.set_matrix_pixel(5, 4, tear)
    droid.set_matrix_pixel(2, 3, tear) 

    # Optional: cheeks
    droid.set_matrix_pixel(1, 3, yellow)
    droid.set_matrix_pixel(6, 3, yellow)

STEPS = 10
SPEED = 100
SLEEP_TIME = 0.1

def make_a_step(droid, current_angle):
    droid.roll(current_angle, SPEED, SLEEP_TIME)
    time.sleep(SLEEP_TIME)
    droid.stop_roll()


def make_a_circle(droid, steps):
    rotate_by = 360 // steps
    current_angle = 0
    for _ in range(steps):
        make_a_step(droid, current_angle % 360)
        current_angle += rotate_by

def main():
    print("Scanning for Sphero BOLT...")
    toy = scanner.find_toy(toy_name="SB-1664")

    engine = pyttsx3.init()



    with SpheroEduAPI(toy) as droid:
 
       
        # replace existing simple LED sequence / spin with energetic routine
        make_a_circle(droid, STEPS)
        time.sleep(1)

        # Scroll a word   
        text = "TRY AGAIN"
        scroll_speed = 28  # adjust: larger -> faster (SDK-specific)
        droid.scroll_matrix_text(text, Color(60, 206, 209), scroll_speed, True)
        # wait for the scroll to finish (approximate; increase if it still cuts off)
        wait_seconds = max(2.0, len(text) * 0.45 + 0.8)
        time.sleep(wait_seconds)
        droid.clear_matrix()
        # droid.scroll_matrix_text("TRY AGAIN", Color(60,206,209),28,True)  # Green text
        time.sleep(1)
    

        # Show sad face
       # droid.clear_matrix()
        draw_sad(droid)
        time.sleep(2)


        # Turn off LEDs after done
        droid.set_main_led(Color(0, 0, 0))
        droid.clear_matrix()
        print("done!")


if __name__ == "__main__":
    main()
