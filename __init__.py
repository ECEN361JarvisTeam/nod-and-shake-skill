from mycroft import MycroftSkill, intent_file_handler
import time
import maestro


class NodAndShake(MycroftSkill):
    #m = maestro.Controller("/dev/ttyACM0")
    
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shake.and.nod.intent')
    def handle_shake_and_nod(self, message):
        m = maestro.Controller("/dev/ttyACM0")
        self.speak_dialog('shake.and.nod')
        m.setAccel(1,1)
        m.setSpeed(1,4)
        m.setTarget(1,5000)
        time.sleep(2)
        m.setTarget(1,4000)
        m.close()

        

def create_skill():
    return NodAndShake()

