import vlc
import schedule
import time
import random
import os

# Set up the list of songs
songs = ["CrazyTrain.mp3"]  # Add your song files here

def play_song():
    song = random.choice(songs)
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(os.path.abspath(song))
    player.set_media(media)
    player.play()

# Schedule the song to play
schedule.every().day.at("22:57").do(play_song)  # Change the time to your desired time

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)