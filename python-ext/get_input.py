
from mycroft_bus_client import MessageBusClient, Message

print('Setting up client to connect to a local mycroft instance')
client = MessageBusClient()

def print_utterance(message):
    print('Mycroft said "{}"'.format(message.data))
    print('Mycroft said "{}"'.format(message.data.get('utterances')))




print('Registering handler for speak message...')
client.on('recognizer_loop:utterance', print_utterance)

client.run_forever()
