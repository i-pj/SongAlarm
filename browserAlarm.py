import schedule
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

def play_random_song(playlist):
    random_song = random.choice(playlist).strip()
    webbrowser.open(random_song)
    time.sleep(5)  # Wait for the webpage to load
    pyautogui.press("space")  # Simulate pressing the spacebar

def main():
    playlist = initialize_playlist()
    if playlist is not None:
        schedule.every().day.at("06:00").do(play_random_song, playlist)  # Schedule the task to run at 6:00 AM every day

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()