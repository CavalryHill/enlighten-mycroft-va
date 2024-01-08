from mycroft import MycroftSkill

class ListenForMessageSkill(MycroftSkill):
  def initialize(self):  
      self.add_event('recognizer_loop:record_begin',  
                    self.handle_listener_started)  
      self.add_event('recognizer_loop:record_end',  
                    self.handle_listener_ended)

  def handle_listener_started(self, message):  
      print('REC-Started'); 

  def handle_listener_ended(self, message):  
      print('REC-Ended'); 

def create_skill():
    return ListenForMessageSkill()
