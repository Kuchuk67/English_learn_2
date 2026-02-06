import pyttsx3
from setting import SPEED

def voice(text,example=None):

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the speed and volume of the voice
    engine.setProperty('rate', SPEED)  # 150 words per minute
    engine.setProperty('volume', 0.8)  # 80% volume

    # Get the text to voice from the user
    #
    
    if example:
        text_for_sound = f"{text}, , , , ,{example}"
    else:
        text_for_sound = text
    # Convert the text to speech
    engine.say(text_for_sound)
    # engine.save_to_file("Текст", "out.wav")
    engine.runAndWait()
