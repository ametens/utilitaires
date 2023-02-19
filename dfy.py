from pytube import YouTube, Playlist
import PySimpleGUI as gui

#
# draw the layout of the window
#
frame_layout_1 = [[gui.In(font='NewsGothicMT 16'),gui.Push()]]
frame_layout_2 = [[gui.Radio('a playlist', 'RADIO1', default=True,font='NewsGothicMT 16'),gui.Radio('a single song', 'RADIO1', default=False, key="-SONG-",font='NewsGothicMT 16'),gui.Push()]]
frame_layout_3 = [
    [
        gui.In(font='NewsGothicMT 16', key='-PLAYLIST-'),
        
        #Set inital_folder if you want the browse folder start the search in a specific folder
        gui.FolderBrowse(button_text='Browse',key='-BROWSE-',font='NewsGothicMT 14',size=9, initial_folder=''), 
        
        gui.Push()]
]
frame_layout_4 = [
    [gui.Push(),gui.Output(size=(70, 10),font='NewsGothicMT 12'),gui.Push()],
    [gui.Push(),
        gui.B('Download',font='NewsGothicMT 14',size=9),
        gui.B('Cancel',font='NewsGothicMT 14',size=9),
        gui.B('Close',font='NewsGothicMT 14',size=9),
        gui.Push()]]

#
# main layout
#
layout = [    
    [gui.Frame('Paste a url from Youtube', frame_layout_1,relief='flat', font='NewsGothicMT 16')],
    [gui.Frame('What are you downloading?', frame_layout_2,relief='flat', font='NewsGothicMT 16')],
    [gui.Frame('Select a destination folder', frame_layout_3,relief='flat', font='NewsGothicMT 16')],
    [gui.Frame('', frame_layout_4,relief='ridge', font='NewsGothicMT 16')],
]

#
# start drawing the window
#
window = gui.Window('Download an audio playlist/song/podcast from YouTube', layout)


while True:

    event, values = window.read()  

    #listen for specials events
    #(by example, push a particular button)
    #
    if event in (gui.WIN_CLOSED, 'Cancel') :
        break   

    elif event in (gui.WIN_CLOSED, 'Close') :
        window.close()

    elif values['-SONG-'] == False: #Is it a playlist or single song/podcast/audio file?       
        
        #
        #start evaluating the download of PLAYLIST
        #
        try:
            oplaylist = Playlist(values[0])
        except:
            print('Reading Error!')
            window.refresh() 
            
        else:
            print('\r','*'*3,'Playlist','*'*3)
            
            print('1. Number of titles:',oplaylist.length)
            print('2. Name of the playlist:', oplaylist.title)        
            print('3. URL of the playlist:', oplaylist.playlist_url)
            print('4. Directory of the playlist:', values['-PLAYLIST-'])     

            try:
                vl = oplaylist.trimmed(oplaylist.playlist_url)
                c = 0
                r = str()
            except:
                print("Extraction error!")
                window.refresh()
            else:
                print('5. Content of the playlist:')
                window.refresh()#display the message in real time
                
                
                for i in vl:
                    c = c + 1
                    i_yt = YouTube(i)

                    for s in i_yt.streams.filter(only_audio=True):
                        try:
                            #
                            #choose the highest quality for AUDIO FILE (video excluded!)
                            #
                            stream_to_dwnld = i_yt.streams.get_by_itag(140)
                            stream_to_dwnld.download(output_path=values['-PLAYLIST-'])
                                                            
                        except:                            
                            print(f'MP4 version is not available.\rTrying to download a downgrade one...')
                            window.refresh()                          
                            
                            try:
                                stream_to_dwnld = i_yt.streams.get_by_itag(251)
                                stream_to_dwnld.download(output_path=values['-PLAYLIST-'])

                            except:
                                print(f'WEBM (160Kbps) version is not available.\rTrying to download a downgrade one...')
                                window.refresh()                               

                                try:
                                    stream_to_dwnld = i_yt.streams.get_by_itag(250)
                                    stream_to_dwnld.download(output_path=values['-PLAYLIST-'])

                                except:
                                    print(f'WEBM (70Kbps) version is not available.\rTrying to download a downgrade one...')
                                    window.refresh() 

                                    try:
                                        stream_to_dwnld = i_yt.streams.get_by_itag(249)
                                        stream_to_dwnld.download(output_path=values['-PLAYLIST-'])

                                    except:
                                        print(f'WEBM (50Kbps) version is not available.\rTrying to download a downgrade one...')
                                        window.refresh()                                    

                    
                    print(f"{i_yt.title} downloaded with success!")
                    window.refresh()
                
                window.close()
    else:
        #
        #start evaluating the download of SINGLE AUDIO FILE
        #
        try:
            osingle = YouTube(values[0])
        except:
            print('Exception raised when reading the single file.')
            window.refresh()
        else:
            print('\r','+'*3,'Single song','+'*3)            
            print('Title:',osingle.title)       
            print('Directory of the file:', values['-PLAYLIST-'])    
            window.refresh()
            try:
                print('\nDownload the file...')    
                window.refresh()
                stream_to_dwnld = osingle.streams.get_by_itag(140)
                stream_to_dwnld.download(output_path=values['-PLAYLIST-'])
            except:
                print(f'MP4 version is not available.')
                window.refresh()
            else:
                print(f"Downloaded with success!")
                window.refresh()

        
