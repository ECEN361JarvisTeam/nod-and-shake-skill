from mycroft import MycroftSkill, intent_file_handler
import time
import maestro


class NodAndShake(MycroftSkill):
    
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shake.and.nod.intent')
    def handle_shake_and_nod(self, message):
        m = maestro.Controller("/dev/ttyACM0")
        m.setAccel(1, 4)
        m.setSpeed(1, 12)
        # 8000 seems to be the maximum
        m.setTarget(1, 8000)
        while m.getPosition(1) < 8000:
            time.sleep(0.01)
        
        m.setTarget(1, 5500)

        while m.getPosition(1) > 5500:
            time.sleep(0.01)

        m.setTarget(1, 7000)

        while m.getPosition(1) < 7000:
            print(m.getPosition(1))
            time.sleep(0.01)
        
        m.close()
        self.speak_dialog('shake.and.nod')


def create_skill():
    return NodAndShake()

