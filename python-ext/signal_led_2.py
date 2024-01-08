from mycroft import MycroftSkill
from mycroft.messagebus.message import Message
import RPi.GPIO as GPIO
import time

# Set up the GPIO pin
LED_PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

class PicroftLED(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        try:
            self.blink_led(1)
        except GPIO.error:
            self.log.warning("Can't initialize GPIO - skill will not load")
            self.speak_dialog("error.initialise")
        finally:
            self.add_event('recognizer_loop:record_begin', self.handle_listener_started)
            self.add_event('recognizer_loop:record_end', self.handle_listener_ended)
            self.add_event('recognizer_loop:utterance', self.handler_utterance)
            self.add_event('recognizer_loop:audio_output_start', self.handler_audio_output_start)
            self.add_event('recognizer_loop:audio_output_end', self.handler_audio_output_end)
            self.add_event('recognizer_loop:wakeword', self.handler_wakeword)
            self.add_event('mycroft.stop', self.handler_mycroft_stop)

    def blink_led(self, n):
        for _ in range(n):
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.5)

    def handler_mycroft_stop(self, message):
        # code to execute when mycroft.stop message detected...
        GPIO.output(LED_PIN, GPIO.LOW)

    def handle_listener_started(self, message):
        # code to execute when active listening begins...
        # light up LED
        GPIO.output(LED_PIN, GPIO.HIGH)

    def handle_listener_ended(self, message):
        GPIO.output(LED_PIN, GPIO.LOW)

    def handler_utterance(self, message):
        self.blink_led(5)

    def handler_audio_output_start(self, message):
        # start fading LED (for simplicity, turning it on)
        GPIO.output(LED_PIN, GPIO.HIGH)

    def handler_audio_output_end(self, message):
        # stop fading LED (for simplicity, turning it off)
        GPIO.output(LED_PIN, GPIO.LOW)

    def handler_wakeword(self, message):
        # code to execute when recognizer_loop:wakeword message
        self.blink_led(1)

def create_skill():
    return PicroftLED()
