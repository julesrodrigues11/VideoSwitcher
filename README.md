There are three scripts in this repository - main.py, vlcplayer.py and seek.py

main.py - Prototype script using pygame and moviepy to render the videos and event handling. Not to be used anymore
vlcplayer.py - Second prototype using python-vlc to render the videos. Renders the videos with a better frame rate when compared to pygame. Has latency when switching between videos, however due to handling them from different videos
seek.py - Final prototype (currently being used) using python-vlc to render the videos. However, it only uses one video and does not switch between videos. Instead, it loops between portions of the same video. The video should be named "video.mp4"

Before running the program, it is important to install the requirements.txt using the command "pip install -r requirements.txt"

As this is to be run on the Raspberry Pi, the first step would be to create a virtual environment
If not already installed, run "sudo apt install python-venv" to install the virtual environment library
Then create a virtual environment by running "python3 -m venv switcher" which creates a virtual environment named switcher
Then activate the virtual environment by running "source switcher/bin/activate"
Run "pip install -r requirements.txt" to install the dependencies from requirements.txt

Every time a new terminal is opened, you would have to activate the virtual environment again by running "source switcher/bin/activate"

The script uses the keyboard library which requires the user to be in superuser state. Run "sudo su" before activating the virtual environment to run the script

To run the script, run the command "python seek.py" as superuser once the virtual environment has been enabled