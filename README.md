# Console AI Agent – Phase 1

## Project Overview

Phase 1 of the Console AI Agent focuses on building the **core voice and text processing system**.

The system allows a user to interact with the program through:

* Text input
* Voice input through a microphone

All user inputs are converted into **audio files automatically**.
The system also supports **multiple languages**, meaning users can speak or type in almost any language.

This phase establishes the **foundation for Phase 2**, where the agent will become fully conversational.

---

# Key Features

### 1. Text to Audio

Users can type any text in the console and the system will:

* Detect the language automatically
* Convert the text into speech
* Save it as an MP3 audio file

---

### 2. Voice to Text to Audio

Users can speak through their microphone and the system will:

1. Record the speech
2. Convert speech to text
3. Display the recognized text in the console
4. Convert the text into an audio file

---

### 3. Automatic Language Detection

The system uses language detection to support multiple languages automatically.

Examples:

| Input Language | Output                                 |
| -------------- | -------------------------------------- |
| English        | English speech                         |
| Hindi          | Hindi speech                           |
| Mixed Language | Mixed speech (best possible detection) |

---

### 4. Audio Storage System

All generated audio files are saved automatically in the project directory.

Each file has a **timestamp-based unique filename**.

Example:

```
output_20260224_114512.mp3
```

---

# Project Structure

```
PROJECT - F/
│
├── phase_one/
│   │
│   ├── audio/
│   │   Stores all generated audio files
│   │
│   ├── modules/
│   │   │
│   │   ├── audio_to_text.py
│   │   │   Handles microphone recording
│   │   │   Converts speech to text
│   │   │
│   │   ├── text_to_audio.py
│   │   │   Converts text into speech
│   │   │   Detects language automatically
│   │
│   ├── launch.py
│       Main controller of the system
```

---

# Libraries Used

### speech_recognition

Used to capture voice from the microphone and convert it into text.

### gTTS (Google Text To Speech)

Used to convert text into realistic speech audio.

### langdetect

Automatically detects the language of the provided text.

### playsound3

Plays generated audio files directly from Python.

### datetime

Creates unique timestamps for audio filenames.

### os

Handles file paths and directory management.

---

# How the System Works

### Step 1 – User Selects Mode

When the program starts, the user chooses:

```
1 Text to Audio
2 Voice to Audio
0 Stop Input
```

---

# Mode 1 – Text to Audio

Flow:

```
User types text
      ↓
Language detected
      ↓
Text converted to speech
      ↓
Audio saved in /audio folder
```

Example:

```
Enter text: Hello world
```

Output:

```
Text converted successfully into audio.
```

---

# Mode 2 – Voice to Audio

Flow:

```
User speaks
      ↓
Microphone records audio
      ↓
Speech converted to text
      ↓
Text displayed in console
      ↓
Text converted to audio
```

Example:

```
Press ENTER to start recording
Listening...
You said:
Hello AI
```

---

# Audio Playback System

After stopping input, the user can choose:

```
1 Play all audio files
2 Play last generated audio
```

Option Details:

| Option    | Function                                            |
| --------- | --------------------------------------------------- |
| Play all  | Plays every audio file generated during the session |
| Play last | Plays only the most recent audio file               |

---

# Installation Guide

### Step 1 – Install Python

Recommended version:

```
Python 3.10+
```

---

### Step 2 – Install Required Libraries

Run:

```
pip install gtts
pip install langdetect
pip install playsound3
pip install SpeechRecognition
pip install pyaudio
```

If `pyaudio` fails:

```
pip install pipwin
pipwin install pyaudio
```

---

# Running the Project

Navigate to the phase_one folder and run:

```
python launch.py
```

---

# Example Console Session

```
Select Mode:
1 Text to Audio
2 Voice to Audio
0 Stop Input

Enter choice: 1
Enter text: Hello this is my AI agent

Text converted successfully into audio.
```

Voice Example:

```
Press ENTER to start recording
Listening...

You said:
Hello how are you
```

---

# Error Handling

The system automatically handles:

* Microphone errors
* Speech recognition failures
* Language detection failures

Fallback language is set to **English** if detection fails.

---

# Why Phase 1 Matters

Phase 1 builds the **core AI interaction pipeline**:

```
User Input
     ↓
Speech / Text Processing
     ↓
Language Detection
     ↓
Audio Generation
     ↓
Playback System
```

This pipeline will be used directly in **Phase 2 AI conversations**.

---

# Future Development (Phase 2)

Phase 2 will introduce:

* AI-generated responses
* Real-time conversation system
* API or RAG-based intelligence
* Faster response generation
* Fully interactive voice assistant

---

# Author

Project developed as part of an experimental **Console AI Agent System** focusing on speech interaction, language flexibility, and modular architecture.
