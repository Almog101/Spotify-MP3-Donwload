from __future__ import unicode_literals
from Client import Spotify_Client
import configparser
import youtube_dl
import sys

class interface:
    def __init__(self):
        pass

    def playlist(self, uri):
        songs = api_client.getPlaylistSongs(uri)
        playlist_name = api_client.getPlaylistName(sys.argv[2]).replace(' ','-')

        for title in songs:
            url = f"https://www.youtube.com/watch?v={api_client.getVideoID(title)}"
            youtube_dl.YoutubeDL( params={'-c': '', '--no-mtime': '', 'outtmpl': f'./output/{playlist_name}/{title}.mp3'} ).download([url])
            

    def song(self, uri):
        song_name = api_client.getSongName(uri)
        url = f"https://www.youtube.com/watch?v={api_client.getVideoID(song_name)}"
        youtube_dl.YoutubeDL( params={'-c': '', '--no-mtime': '', 'outtmpl': f'./output/{song_name}.mp3'} ).download([url])



    def help_(self):
        print("SpotifyToMP3 - download entire playlists in one command")
        print("\n -p  playlist    download entire playlist")
        print(" -s  song        download one song\n")
        print("ex. python3 main.py -p spotify:playlist:1XCZZ48KvoPCF3MGPWwxWi")
        print("\nMade by Almog Ben-Akvia\n")




if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_client = Spotify_Client(config['CLIENT']['CLIENT_ID'], config['CLIENT']['CLIENT_SECRET'])
    ifc = interface()
    
    if len(sys.argv) == 1:
        ifc.help_()
        exit()
    type_ = sys.argv[1]
    
    if type_ == '-p':
        ifc.playlist(sys.argv[2])
    elif type_ == '-s':
        ifc.song(sys.argv[2])
    elif type_ == '-h':
        ifc.help_()
    else:
        print("Invalid Parameter.")
        exit()
    

    
        

    
