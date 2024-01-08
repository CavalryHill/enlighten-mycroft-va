from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
from mycroft_bus_client import MessageBusClient, Message
import threading

app = Flask(__name__, template_folder='templates', static_folder='templates/static')
socketio = SocketIO(app)

# Create a global variable to store the Mycroft utterance
mycroft_responses = []

def print_utterance(message):
    global mycroft_responses
    mycroft_utterance = message.data.get('utterance')
    print('Mycroft said "{}"'.format(mycroft_utterance))
    mycroft_responses.append(mycroft_utterance)
    # For Data Change Detection
    socketio.emit('mycroft_response', {'utterance': mycroft_utterance})

def socket_input(message): 
    user_input = message.data.get('utterances')
    print('User said "{}"'.format(user_input))
    socketio.emit('user_input', {'utterance': user_input[0]})

# Set up Mycroft client
client = MessageBusClient()
client.on('speak', print_utterance)

client.on('recognizer_loop:utterance', socket_input)

client.run_in_thread()

mycroft_thread = threading.Thread(target=client.run_forever)
mycroft_thread.start()

@app.route('/')
def index():
    return render_template('index.html', mycroft_responses=mycroft_responses)

@app.route('/api/output', methods=['GET'])
def get_mycroft_output():
    global mycroft_responses
    return jsonify({'utterances': mycroft_responses})

# @app.route('/api/output', methods=['POST'])
# def set_output():
#     if request.method == 'POST':
#         data = request.get_json()
#         user_input = data.get('input')
#         if user_input:
#             # Send the user input to Mycroft
#             client.emit(Message('speak', data={'utterance': user_input}))
#             return jsonify({'status': 'success', 'message': 'User input sent to Mycroft'})
#         else:
#             return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

@app.route('/api/input', methods=['POST'])
def set_input():
    if request.method == 'POST':

        # Clear the History
        global mycroft_responses; mycroft_responses = []; 

        data = request.get_json()
        user_input = data.get('input')
        if user_input:
            # Inject the utterance into the recognizer loop
            client.emit(Message("recognizer_loop:utterance", {'utterances': [user_input], 'lang': 'en-us'}))
            return jsonify({'status': 'success', 'message': 'Utterance injected'})
        else:
            return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
