import os
from pytube import YouTube, Playlist

# display colors and text transformations
CBOLD = '\033[1m'
CEND = '\033[0m'

os.system('clear')

# asking informations inputs
ans = input("Paste the url from YouTube:")
plst = 'playlist?'

# choose between playlist or single album
isPlst = ans.find(plst)
if (isPlst > 0):
    # download playlist
    try:
        oplaylist = Playlist(ans)
        vl = oplaylist.trimmed(oplaylist.playlist_url)
        c = 0
        r = str() 
        
        #
        # Change parent_dir variable with your favorite musi base directory!
        #
        parent_dir = '' # <-- paste URI here
        
        
        artist = input("> Artist/author name?")
        playlist_name = input("> Playlist/album name?")
        destination_folder = os.path.join(parent_dir, artist+'/'+playlist_name)
        try:
            # donwload of playlist start!
            os.makedirs(destination_folder)
            os.system('clear')
            teaser = f"\r*** Playlist of {oplaylist.length} songs ***\nName: {CBOLD}{oplaylist.title}{CEND}"
            d = f"\rDestination folder {CBOLD}{destination_folder}{CEND} created!\r"
            print(teaser + d)
            for i in vl:
                c = c + 1
                i_yt = YouTube(i)
                for s in i_yt.streams.filter(only_audio=True):
                    try:
                        stream_to_dwnld = i_yt.streams.get_by_itag(140)
                        stream_to_dwnld.download(output_path=destination_folder)
                    except Exception as e:
                        raise e
                s = f"{c}. {CBOLD}{i_yt.title}{CEND}...\x1b[6;30;42m downloaded successfully! \x1b[0m"
                print(s)
        except Exception as e:
            raise e 
    except Exception as e:
        raise e
else:
    # download single album/file
    try:
        osingle = YouTube(ans)
        
        #
        # Change parent_dir variable with your favorite musi base directory!
        #
        parent_dir = '' # <-- paste URI here
        
        artist = input("> Artist/author name?")
        playlist_name = input("> Playlist/album name?")
        destination_folder = os.path.join(parent_dir, artist+'/'+playlist_name)
        print('\r','*'*3,'One song from',osingle.title, '*'*3)
        try:
            os.makedirs(destination_folder)
            os.system('clear')
            d = f"Destination folder {CBOLD}{destination_folder}{CEND} created!\r"
            print(d)
            stream_to_dwnld = osingle.streams.get_by_itag(140)
            stream_to_dwnld.download(output_path=destination_folder)
            s = f"{CBOLD}{stream_to_dwnld.title}{CEND}...\x1b[6;30;42m downloaded successfully! \x1b[0m"
            print(s)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

# end if
