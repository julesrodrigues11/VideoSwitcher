import vlc
import time
import keyboard
import sys

from variables import *

# Initialize VLC instance
instance = vlc.Instance('--aout=alsa')

# Create VLC media player
player = instance.media_player_new()

# Function to loop a video segment between startTime and endTime
def LoopVideoSegment(video_path):

    global video1StartTime, video1EndTime, video2StartTime, video2EndTime, video3StartTime, video3EndTime, video4StartTime, video4EndTime

    startTime = video1StartTime
    endTime = video1EndTime

    media = instance.media_new(video_path)
    player.set_media(media)
    player.set_fullscreen(True)

    # Start playing the video
    player.play()

    # Allow some time for the video to start
    time.sleep(0.1)

    # Loop the segment indefinitely
    while True:
        
        # Set the player to the start time (in milliseconds)
        player.set_time(startTime)

        # Continuously check the current playback time
        while player.get_time() < endTime:
            time.sleep(0.05)  # Small delay to prevent excessive CPU usage

            if (keyboard.is_pressed(escape)):
                player.stop()
                sys.exit(0)

            elif (keyboard.is_pressed(video1Key)):
                startTime = video1StartTime
                endTime = video1EndTime
                player.set_time(startTime)

            elif (keyboard.is_pressed(video2Key)):
                startTime = video2StartTime
                endTime = video2EndTime
                player.set_time(startTime)
            
            elif (keyboard.is_pressed(video3Key)):
                startTime = video3StartTime
                endTime = video3EndTime
                player.set_time(startTime)

            elif (keyboard.is_pressed(video4Key)):
                startTime = video4StartTime
                endTime = video4EndTime
                player.set_time(startTime)

            elif (keyboard.is_pressed(video5Key)):
                startTime = video5StartTime
                endTime = video5EndTime
                player.set_time(startTime)

        # Once the endTime is reached, the loop resets the video to the startTime
        player.set_time(startTime)

# Loop the video segment from 1 to 3 seconds
LoopVideoSegment(videoPath)
