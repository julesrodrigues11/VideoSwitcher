import vlc
import keyboard
import time
import sys

instance = vlc.Instance()

player = instance.media_player_new()

default_path = 'default.mp4'
video1_path = 'video1.mp4'
video2_path = 'video2.mp4'

defaultVideo = instance.media_new(default_path)
video1 = instance.media_new(video1_path)
video2 = instance.media_new(video2_path)

def PlayVideo(video):
    player.set_media(video)
    player.toggle_fullscreen()
    player.play()

currentVideo = defaultVideo

def HandleKeypress():
    global currentVideo
    while True:
        if keyboard.is_pressed('1'):
            currentVideo = defaultVideo
            PlayVideo(currentVideo)
            time.sleep(0.2)
        
        elif keyboard.is_pressed('2'):
            currentVideo = video1
            PlayVideo(currentVideo)
            time.sleep(0.2)
        
        elif keyboard.is_pressed('3'):
            currentVideo = video2
            PlayVideo(currentVideo)
            time.sleep(0.2)
        
        elif keyboard.is_pressed('esc'):
            player.stop()
            sys.exit(0)
        
        if (player.get_state() == vlc.State.Ended):
            PlayVideo(currentVideo)
        
        time.sleep(0.1)

PlayVideo(currentVideo)
HandleKeypress()