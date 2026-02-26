"""
Main controller for Phase One AI Agent
Supports:
1 Text to Audio
2 Voice to Audio
Playback system
"""

# Import OS
import os

# Import time
import time

# Import modules
from modules.text_to_audio import convert_text_to_audio
from modules.audio_to_text import record_from_microphone
from playsound3 import playsound


def play_audio_files(audio_files):

    for audio_path in audio_files:

        # Play audio and wait until it finishes
        playsound(audio_path)


def get_all_audio_files(audio_folder):
    """
    Get all mp3 files
    """

    files = [f for f in os.listdir(audio_folder) if f.endswith(".mp3")]
    files.sort()

    return [os.path.join(audio_folder, f) for f in files]


def show_playback_options(audio_folder, last_audio_path):

    print("\nPlayback Options:")
    print("1 Play all audio files")
    print("2 Play last generated audio")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        files = get_all_audio_files(audio_folder)
        play_audio_files(files)

    elif choice == "2" and last_audio_path:
        play_audio_files([last_audio_path])

    else:
        print("Invalid option.")


def main():

    # Define base directory
    base_dir = os.path.dirname(__file__)

    # Define audio folder
    audio_folder = os.path.join(base_dir, "audio")

    # Last generated audio path
    last_audio_path = None

    while True:

        print("\nSelect Mode:")
        print("1 Text to Audio")
        print("2 Voice to Audio")
        print("0 Stop Input")

        mode = input("Enter choice: ")

        if mode == "0":
            print("\nInput stopped.")
            break

        # TEXT MODE
        if mode == "1":

            user_text = input("Enter text: ")

            last_audio_path = convert_text_to_audio(user_text)

            print("\nText converted successfully into audio.")

        # VOICE MODE
        elif mode == "2":

            spoken_text = record_from_microphone()

            if spoken_text is None:
                print("Speech not understood.")
                continue

            print("You said:")
            print(spoken_text)

            last_audio_path = convert_text_to_audio(spoken_text)

        else:
            print("Invalid mode.")

    # Playback section
    print("\nPlayback Options:")
    print("1 Play all audio files")
    print("2 Play last generated audio")

    choice = input("Enter your choice (1/2): ")

    if os.path.exists(audio_folder):
        all_audio_files = get_all_audio_files(audio_folder)
    else:
        all_audio_files = []

    if choice == "1":
        if all_audio_files:
            play_audio_files(all_audio_files)
        else:
            print("No audio files available.")

    elif choice == "2":
        if last_audio_path:
            play_audio_files([last_audio_path])
        else:
            print("No last audio available.")

    print("\nProgram finished.")


if __name__ == "__main__":
    main()