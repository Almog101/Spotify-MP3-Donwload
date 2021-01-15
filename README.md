# SpotifyToMp3

Download playlists / songs from spotify in mp3 using python 


## Description

If you wanted free and open source way to not pay spotify premium just to download your favorite songs, this is your soulution. with one easy command you can download an entire playlist in a couple of minutes.


## Installation

```console
# clone the repo
$ git clone https://github.com/Almog101/SpotifyToMp3.git

# change the working directory to SpotifyToMp3
$ cd SpotifyToMp3

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage
Add your Client_ID and Client_Secret to config.ini then:

```console
$ python3 main.py -h
SpotifyToMP3 - download entire playlists in one command

 -p  playlist    download entire playlist
 -s  song        download one song

ex. python3 main.py -p spotify:playlist:1XCZZ48KvoPCF3MGPWwxWi

Made by Almog Ben-Akiva
```

