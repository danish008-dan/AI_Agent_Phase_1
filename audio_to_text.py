"""
File Name: audio_to_text.py
Purpose:
Capture speech from microphone and convert it into text.
"""

# Import speech recognition
import speech_recognition as sr


def record_from_microphone():
    """
    Records voice from microphone and converts to text.

    Returns:
    str: Recognized speech text
    """

    # Create recognizer object
    recognizer = sr.Recognizer()

    # Use microphone as audio source
    with sr.Microphone() as source:

        # Ask user to start speaking
        print("\nPress ENTER to start recording...")
        input()

        print("Listening... Speak now.")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # Record audio
        audio = recognizer.listen(source)

        print("Recording stopped.\n")

    try:
        # Convert speech to text using Google
        text = recognizer.recognize_google(audio)

        # Return detected text
        return text

    except sr.UnknownValueError:
        return None

    except sr.RequestError:
        return None