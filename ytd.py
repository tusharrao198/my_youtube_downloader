import subprocess

print("If you are on :- \n 1. Linux \n 2. Windows")
op_system = int(input("Choose Which Operating System you are using:- "))
if op_system == 1:
    op = False
if op_system == 2:
    op = True

#  python program to download the playlist or video from YOUTUBE by the use of youtube-dl

while True:
    print(
        """ 1. If you want to download Playlist\n 2. If you want to download a single video \n 3. exit"""
    )
    n = int(input("Choose options:- "))

    if n == 1:
        playlist_url = input("Paste Playlist Url: ")
        print(
            "in order will be given to every video in both cases. \n Do you want to download whole Playlist or from Between \n 1. Full \n 2. Edit \n 3. Single video from the playlist"
        )
        xx = int(input("choose options for playlist :"))
        if xx == 1:
            subprocess.run(
                [
                    "youtube-dl",
                    "-o",
                    "%(playlist_index)s-%(title)s.%(ext)s",
                    "-f",
                    "best",
                    playlist_url,
                ],
                shell=op,
            )
            print("T")
        elif xx == 2:
            start = int(
                input(
                    "Enter Starting No. of video from where you want to start download :"
                )
            )
            end = int(input("Enter index of upto which video: "))
            subprocess.run(
                [
                    "youtube-dl",
                    "-o",
                    "%(playlist_index)s-%(title)s.%(ext)s",
                    "-f",
                    "best",
                    "-ci",
                    "--playlist-start",
                    str(start),
                    "--playlist-end",
                    str(end),
                    playlist_url,
                ],
                shell=op,
            )
        elif xx == 3:
            start = int(
                input(
                    "Specify the NO./Index of video You want to download from the Playlist:- "
                )
            )
            subprocess.run(
                [
                    "youtube-dl",
                    "-o",
                    "%(playlist_index)s-%(title)s.%(ext)s",
                    "-f",
                    "best",
                    "-ci",
                    "--playlist-start",
                    str(start),
                    "--playlist-end",
                    str(start),
                    playlist_url,
                ],
                shell=op,
            )

    if n == 2:
        video_url = input("Enter Video URL:")
        print("Type Y, If You want to get format\n For best video-format click Enter :")
        if input("Enter Choice:") == "Y":
            subprocess.run(["youtube-dl", "-F", video_url], shell=op)
            print("Select which format do u want to download: ")
            format_value = input("Enter Format(INteger Value): ")
            subprocess.run(["youtube-dl", "-f", format_value, video_url], shell=op)

        else:
            print("downloading the best quality available i.e. format : 'best'")
            subprocess.run(["youtube-dl", "-f", "best", video_url], shell=op)

    if n == 3:
        break
