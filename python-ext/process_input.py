
from mycroft_bus_client import MessageBusClient, Message

from mycroft.skills.audioservice import AudioService

from pytube import YouTube, Search
import os

print('Setting up client to connect to a local mycroft instance')
client = MessageBusClient()

def initialize(self):
    self.audio_service = AudioService(self.bus)

def search_and_get_video_url(name):
    s = Search(name)
    # link of 1st result
    return s.results[0].watch_url

def play_audio_prompt(path):
    # Send a message to the audio service to play a prompt
    client.emit(Message('mycroft_audio_play', data={'file': path}))


def process_utterance(message):
    # print('User said "{}"'.format(message.data))
    print('User said "{}"'.format(message.data.get('utterances')))

# if (user_input == '')

    user_input = message.data.get('utterances')

    video_url = search_and_get_video_url(user_input[0])

    download_directory = '/var/www/html/data/CavalryHill/files/'

    # NOPE

    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution audio stream
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    # Download the audio stream and convert it to MP3
    downloaded_file = audio_stream.download(download_directory)

    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)

    mp3_path = os.path.join(download_directory, new_file)

    print(mp3_path)

    play_audio_prompt(mp3_path)


    






print('Registering handler for speak message...')
client.on('recognizer_loop:utterance', process_utterance)

client.run_forever()
