import moviepy.editor as mp
import pygame
import sys

# Initialize Pygame
pygame.init()

# Load two videos
default = mp.VideoFileClip("default.mp4")
video1 = mp.VideoFileClip("video1.mp4")
video2 = mp.VideoFileClip("video2.mp4")
#video2 = video2.resize(newsize=(1920, 1080))

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Set up Pygame display with the size of the first video
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Clock to control frame rate
clock = pygame.time.Clock()

# Function to play the video in a loop and handle video switching
def play_video(video):
    for frame in video.iter_frames(fps=video.fps, dtype="uint8"):
        # Display the frame
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # If key '1' is pressed, switch to video 1
                if event.key == pygame.K_1:
                    return 1
                # If key '2' is pressed, switch to video 2
                elif event.key == pygame.K_2:
                    return 2
                elif event.key == pygame.K_3:
                    return 3
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Control frame rate
        clock.tick(video.fps)

# Main loop
current_video = 1  # Start with the first video
try:
    while True:
        if current_video == 1:
            next_video = play_video(default)
        elif current_video == 2:
            next_video = play_video(video1)
        elif current_video == 3:
            next_video = play_video(video2)
        
        # Update current video based on user input
        if next_video:
            current_video = next_video
except KeyboardInterrupt:
    pygame.quit()
    sys.exit()
