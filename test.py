# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import youtube_dl
import os
import subprocess
subprocess.call(['dir'], shell=True)

# %%


def test():
    # Ask the user for the video they want to download
    video_url = input("Please enter the YouTube Video URL: ")
    # Download and convert to mp3 and store in downloads folder
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    vedio_title = video_info['title']
    filename = f"{vedio_title}.mp3"

    path_to_save = input(
        r"Enter where the file is to be saved or leave empty if you want it to be saved in the current directory: ")
    if path_to_save == "":
        where_to_save = os.getcwd()
    else:
        where_to_save = f"{path_to_save}"
    options = {
        'yesplaylist': True,
        # reduces the several line of output to bearest mininimal
        'quiet': True,
        'format': 'bestaudio/best',
        'keepvideo': False,
        # f"{where_to_save}\\{filename}"
        'outtmpl': os.path.join(where_to_save, filename),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    # Open the file once it has been downloaded (on Mac os)
    try:
        subprocess.call(["open", filename])
    except FileNotFoundError:
        # this will take care of the windows part
        subprocess.call(('cmd', '/C', 'start', '', filename))


if __name__ == '__main__':
    test()

# %%
