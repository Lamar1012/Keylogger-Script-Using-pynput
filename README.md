# Keylogger-Script-Using-pynput
This Python script captures and logs keystrokes using the pynput library. It listens for keypress events and writes each captured keystroke to a text file (keyfile.txt). The script is designed to log both standard characters and handle errors when non-character keys (like function keys) are pressed
Features:
Keystroke Logging: Captures and logs each keystroke in real-time.
Text File Logging: Appends each captured key to keyfile.txt, creating the file if it does not already exist.
Error Handling: Handles exceptions when non-character keys are pressed, ensuring that the script continues to run smoothly.
Requirements:
Python 3.x
pynput library
