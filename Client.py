import spotipy, os
from spotipy.oauth2 import SpotifyClientCredentials
import urllib.request, re



class Spotify_Client:
    def __init__(self,cli_id, cli_secret):
        self.spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= cli_id, client_secret= cli_secret))

    def getPlaylistName(self, uri):
        return self.spotify.playlist(uri, fields="name")['name']


    def getPlaylistSongs(self, uri):
        Names = []
        
        for item in self.spotify.playlist_tracks(uri)['items']:
            track = item['track']
            Names.append(track['artists'][0]['name']+ " - " +track['name'])
        
        return Names

    def getSongName(self, uri):
      track = self.spotify.track(uri)
      return track['artists'][0]['name']+ " - " +track['name']

    def youtubeSearch(self, song_name):
        words = song_name.split()
        url = "http://www.youtube.com/results?search_query="

        for word in words:
            url += word + "+"

        return url    

    def getVideoID(self, track_name):
        html = urllib.request.urlopen(self.youtubeSearch(track_name))
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        
        return video_ids[0]
