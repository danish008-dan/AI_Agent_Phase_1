"""
File Name: text_to_audio.py
Purpose:
Convert text into audio using gTTS with automatic language detection.
This ensures the system works with any language.
"""

# Import OS module
import os

# Import datetime for unique filenames
from datetime import datetime

# Import Google Text-to-Speech
from gtts import gTTS

# Import language detection
from langdetect import detect


def convert_text_to_audio(text):
    """
    Convert user text into an MP3 audio file using gTTS.

    Parameters:
    text (str): Input text

    Returns:
    str: Path of saved audio file
    """

    # Detect language automatically
    try:
        language = detect(text)
    except:
        # Default language if detection fails
        language = "en"

    # Define correct audio folder path
    base_dir = os.path.dirname(os.path.dirname(__file__))
    audio_folder = os.path.join(base_dir, "audio")

    # Create folder if it doesn't exist
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    # Create unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{timestamp}.mp3"

    # Create full path
    audio_path = os.path.join(audio_folder, filename)

    # Generate speech using gTTS
    tts = gTTS(text=text, lang=language)

    # Save audio file
    tts.save(audio_path)

    # Return path
    return audio_path