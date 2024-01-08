from mycroft import MycroftSkill

class ListenForMessageSkill(MycroftSkill):
  def initialize(self):  
    self.add_event('recognizer_loop:record_begin',  self.handle_listener_started)  
    self.add_event('recognizer_loop:record_end',  self.handle_listener_ended), 
    self.add_event('recognizer_loop:utterance', self.handler_utterance)
    self.add_event('recognizer_loop:audio_output_start', self.handler_audio_output_start)
    self.add_event('recognizer_loop:audio_output_end', self.handler_audio_output_end)
    self.add_event('recognizer_loop:wakeword', self.handler_wakeword)
    self.add_event('mycroft.stop', self.handler_mycroft_stop)

  def handle_listener_started(self, message):  
      print('REC-Started'); 

  def handle_listener_ended(self, message):  
      print('REC-Ended'); 

def create_skill():
    return ListenForMessageSkill()
