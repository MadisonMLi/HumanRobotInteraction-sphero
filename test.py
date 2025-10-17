import time
import pyttsx3
from enum import IntEnum
from typing import Callable
from spherov2 import scanner
from spherov2.types import Color

from spherov2.sphero_edu import SpheroEduAPI

#from spherov2.toy import Toy

#from playsound import playsound

def speak_local(text: str, blocking: bool = True):
    """Use computer's TTS to say text."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    if blocking:
        # depending on engine run behavior; sometimes runAndWait blocks
        pass



def main():
    print("Scanning for Sphero BOLT...")
    toy = scanner.find_toy(toy_name="SB-3716")
    

    
    with SpheroEduAPI(toy) as droid:
        print("✅ Connected to Sphero BOLT")
        time.sleep(1)
        

        droid.spin(360,1)  # spin in place
        time.sleep(1)

        # light up main LED
        droid.set_main_led(Color(0,0,255))  # Blue
        time.sleep(0.5)
        droid.set_main_led(Color(0,255,0))  # Green
        time.sleep(0.5)
        droid.set_main_led(Color(255,0,0))  # Red
        time.sleep(0.5)



        # Scroll a word
        droid.scroll_matrix_text("HI I AM BOO", Color(60,206,209),27,True)  # Green text
        time.sleep(1)
   
        # “Speak” using your computer
        speak_local("Hi, I AM BOO", True)  # Speak text
        droid.spin(360,1)

        time.sleep(1)






        # Turn off LED at the end
        droid.set_main_led(Color(0,0,0))
        print("Done.")




if __name__ == "__main__":
    main()

