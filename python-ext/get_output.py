from mycroft_bus_client import MessageBusClient, Message

print('Setting up client to connect to a local mycroft instance')
client = MessageBusClient()

def print_utterance(message):
    print('Mycroft said "{}"'.format(message.data.get('utterance')))


print('Registering handler for speak message...')

client.on('speak', print_utterance)

client.run_forever()
