"""
Opens the terminal.
"""
import os
from Speech import speak

def terminal():
    """
    Opens the terminal.
    """
    speak("You are into the terminal now."
        "Type 'exit' when you want to quit.")
    while True:
        command = raw_input('\033[1m' + 'Suman: ' + '\033[0m')
        if command.lower() == "exit":
            speak("Quit terminal.")
            return
        else:
            os.system(command)
