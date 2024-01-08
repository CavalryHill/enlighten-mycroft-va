from mycroft import MycroftSkill
from mycroft.messagebus import Message

class GenerateMessageSkill(MycroftSkill):
  def some_method(self):  
    self.bus.emit(Message("recognizer_loop:utterance",  
                          {'utterances': ["the injected utterance"],  
                            'lang': 'en-us'}))  

def create_skill():
    return GenerateMessageSkill()