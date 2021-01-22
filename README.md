# This is a python program to download youtube videos using youtube-dl.

Pros:-

1. Automated using python to download playlist from between/any playlist_index. ( for eg. videos from 3 to 10)
2. Next is simply downloading the single video from youtube.
3. No need to remember the whole cmd command.

Just paste the Youtube url wherever prompted.

# Prerequisites:-

- For windows:- http://ytdl-org.github.io/youtube-dl/download.html
  download youtube-dl.exe file on your pc.

after downloading ,place this .py file and youtube-dl.exe file in one folder and run the program.

- For Linux:-
  install youtube-dl using sudo apt-get install youtube-dl
  then ,just run `ytd.py` file

or, you can download python package on linux or windows using `pip3 install youtube-dl`.

# To run using .py file

simply run ` python3 filename.py`.

# Steps to follow for Windows Users before using exe file to download:-

For downloading full playlist or particular range of videos from a playlist (using indexes present on the youtube playlist)

1. To Open Windows Security or press window + I
2. Go to update Security -> Virus And threat protection.
3. Under Virus And threat protection settings, click on manage settings
4. Under Exclusion click on Add or remove Exclusion and add `C:\Users\<username>\Downloads`
5. If you want to keep exe file in anyother folder just add that folder here as shown in the steps above.

Now before running ytd.exe, download `youtube-dl.exe` file from `https://youtube-dl.org/` and copy in the same directory ytd.exe is present.
Run `ytd.exe` to start program , copy paste url to download.

You can download full playlist.
