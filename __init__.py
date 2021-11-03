from mycroft import MycroftSkill, intent_file_handler


class NodAndShake(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shake.and.nod.intent')
    def handle_shake_and_nod(self, message):
        self.speak_dialog('shake.and.nod')


def create_skill():
    return NodAndShake()

