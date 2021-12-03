from mycroft import MycroftSkill, intent_file_handler
import time
import maestro
import maestro_functions as mf


class NodAndShake(MycroftSkill):
    #m = maestro.Controller("/dev/ttyACM0")
    
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shake.and.nod.intent')
    def handle_shake_and_nod(self, message):
        self.speak_dialog('shake.and.nod', {"action": message.data["utterance"]})
        time.sleep(0.5)

        m = maestro.Controller("/dev/ttyACM0")
        mf.setAllToDefault(m)
        time.sleep(1)

        if message.data["utterance"] == "nod":
            # 8000 seems to be the maximum
            m.setTarget(mf.h_v, 8000)
            while m.getPosition(mf.h_v) < 8000:
                time.sleep(0.01)
        
            m.setTarget(mf.h_v, 5500)

            while m.getPosition(mf.h_v) > 5500:
                time.sleep(0.01)

            m.setTarget(mf.h_v, mf.h_vDefault)

            while m.getPosition(mf.h_v) < mf.h_vDefault:
                time.sleep(0.01)

            m.close()

        elif message.data["utterance"] == "shake":
            # 8000 seems to be the maximum
            m.setTarget(mf.h_r, 8000)
            while m.getPosition(mf.h_r) < 8000:
                time.sleep(0.01)
        
            m.setTarget(mf.h_r, 4000)

            while m.getPosition(mf.h_r) > 4000:
                time.sleep(0.01)

            m.setTarget(mf.h_r, mf.h_rDefault)

            while m.getPosition(mf.h_r) < mf.h_rDefault:
                time.sleep(0.01)

            m.close()

        else:
            # Nod and Shake
            mf.setPositionThread(m, mf.h_v, 8000, 12, 4)
            time.sleep(0.01)
            mf.setPositionThread(m, mf.h_v, 5500, 12, 4)
            time.sleep(0.01)
            mf.setPositionThread(m, mf.h_v, mf.h_vDefault, 12, 4)
            time.sleep(0.01)
            mf.setPositionThread(m, mf.h_r, 8000, 12, 4)
            time.sleep(0.01)
            mf.setPositionThread(m, mf.h_r, 4000, 12, 4)
            time.sleep(0.1)
            mf.setPositionThread(m, mf.h_r, mf.h_rDefault, 12, 4)
            time.sleep(3)
            mf.closeThreadedMaestro(m)

        

def create_skill():
    return NodAndShake()

