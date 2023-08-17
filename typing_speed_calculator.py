# -*- coding: utf-8 -*-
"""typing speed calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m2K-YsLaVj62vHhyc5iD9oSgnbEnD8-4
"""

## typing speed calculator

import time

def calculate_typing_speed(text, time_elapsed):
    words = text.split()
    word_count = len(words)
    wpm = (word_count / time_elapsed) * 60
    return wpm

def main():
    print("Welcome to the Typing Speed Calculator!")
    input("Press Enter when you're ready to start typing...")

    start_time = time.time()

    text = "The quick brown fox jumps over the lazy dog."  # You can replace this with your own text
    print(f"Type the following text:\n{text}\n")

    typed_text = input("Start typing here: ")

    end_time = time.time()
    time_elapsed = end_time - start_time

    wpm = calculate_typing_speed(typed_text, time_elapsed)
    print(f"\nYour typing speed: {wpm:.2f} words per minute")

if __name__ == "__main__":
    main()