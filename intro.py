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
    toy = scanner.find_toy(toy_name="SB-3716")

    engine = pyttsx3.init()



    with SpheroEduAPI(toy) as droid:
        print("✅ Connected to Sphero BOLT")   
        make_a_circle(droid, STEPS)
        droid.roll(0,0,0)

        time.sleep(1)     
       


        droid.set_main_led(Color(0,0,255))  # Blue
        time.sleep(0.5)
        droid.set_main_led(Color(0,255,0))  # Green
        time.sleep(0.5)
        droid.set_main_led(Color(255,0,0))  # Red
        time.sleep(0.5)


        # Spin 
        droid.spin(1080, 3)  # 1080 degrees/sec, 3 sec spin
        time.sleep(1)    

        # Scroll a word    
        droid.scroll_matrix_text("HI I AM BOO", Color(60,206,209),27,True)  # Green text
        time.sleep(1)
    
        engine.say("Hi, I am Boo")
        engine.runAndWait()


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
