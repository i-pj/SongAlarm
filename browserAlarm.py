import time
import webbrowser
import random
import os
import pyautogui

def initialize_playlist():
    if not os.path.isfile("SongList.txt"):
        return None
    
    with open("SongList.txt", "r") as file:
        playlist = file.readlines()
    
    return playlist

def wait_until_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            return

def play_random_song(playlist):
    random_song = random.choice(playlist).strip()
    webbrowser.open(random_song)
    time.sleep(5)  # Wait for the webpage to load
    pyautogui.press("space")  # Simulate pressing the spacebar

def main():
    playlist = initialize_playlist()
    if playlist is not None:
        alarm_time = "6:00"
        wait_until_alarm(alarm_time)
        play_random_song(playlist)

if __name__ == "__main__":
    main()