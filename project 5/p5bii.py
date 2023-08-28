import urllib.request
from html.parser import HTMLParser
import ssl
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# a SSL context is created that doesn't verify certificates
ssl_context = ssl._create_unverified_context()

# this subclass of HTMLParser is created to extract song titles from HTML
# content 
class SongTitleParser(HTMLParser):

# the constructor initalizes the class object, and within it
# the HTMLParser constructor is called to be initalized as well
# an instance of a list called "song_titles" is also created
    def __init__(self):
        super().__init__()
        self.song_titles = []

# this method handles the text in the HTML content when parsing 
# occurs; the updated data (sans surrounding whitespace) is added to 
# the song_titles list 
    def handle_data(self, data):
        self.song_titles.append(data.strip())

# a list called urls is created to store all the urls the user will 
# enter in the following while loop
urls = []

# while the break statement hasn't been activated, the user is prompted
# to enter a url to be processed, or to press enter to activate the break
# staement
while True:
    url = input("Enter a URL (or press Enter to finish): ")
    if not url:
        break

# each url the user enters is added to the urls list using the append feature 
    urls.append(url)

# the following definitions are used to initalize the Spotipy API client:
# the scope of the Spotify API address is defined (to modify public playlists)
scope = 'playlist-modify-public'

# this is the user (my) Spotify username 
username = 'USERNAME'

# these two client variables are unique identifers assigned to my application 
# by the Spotify for Developers platform 
client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'

# this uri is what Spotify uses to redirect the user after they've authorized
# my application
redirect_uri = 'http://127.0.0.1:8080/'

# an instance of the SpotifyOAuth class is created, specifying the access type(public)
# and the username the application is working with 
token = SpotifyOAuth(scope=scope, username=username)

# an instance of the Spotify class is created to work with the Spotify Web API,
# connecting the API with the right authentication
spotifyObject = spotipy.Spotify(auth_manager=token)

# the user is prompted to enter their playlist name and description
playlist_name = input("Enter a playlist name: ")
playlist_description = input("Enter a description: ")

# the user_playlist_create method of the SpotifyObject instance is called to make the 
# user's new playlist
# the playlist is assigned to the user, name, description, and access are passed to the 
# the method's parameters
spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

# a list called list_of_songs is created to store all the song uris found to add the 
# user's playlist 
list_of_songs = []

# for each url of the urls list, 
for url in urls:

# the url is opened and the HTLML content is fetched for
# context is involved with the SSL context to handle not 
# verifying cerificates
    response = urllib.request.urlopen(url, context=ssl_context)

# the HTML content is read from the response 
    html_content = response.read()

# # an instance of the SongTitleParser class is made using the variable parser 
# to extract data from the HTML content, and said content is decoded using
# UTF-8 encoding 
# the parsing process starts here 
    parser = SongTitleParser()
    parser.feed(html_content.decode('utf-8'))

# if a song title could be extratced from the HTML content, 
    if parser.song_titles:

# the first few words of the HTML content (containing the artist and song title) are
# removed from the rest of the obtained HTML content 
        first_song_title = parser.song_titles[0].split('|')[0].strip()

# the program prompts the user with message that their song was added to their playlist 
        print("Adding song:", first_song_title)

# the song title is used to search on Spotify and find a matching track 
        result = spotifyObject.search(q=first_song_title)

# if there's a matching track found, the song's Spotify uri is appeneded to the 
# list_of_songs lsit 
        if 'tracks' in result and 'items' in result['tracks'] and result['tracks']['items']:
            list_of_songs.append(result['tracks']['items'][0]['uri'])

# the user's created playlist is fetched be stored in the prePlaylist variable 
prePlaylist = spotifyObject.user_playlists(user=username)

# the user's playlist ID is extracted from the prePlaylist variable 
playlist = prePlaylist['items'][0]['id']

# the user is prompted with a messgae that all the urls have been processed and added 
# to the playlist 
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs)
print("Songs added to the playlist.")
