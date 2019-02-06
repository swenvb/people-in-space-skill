from mycroft import MycroftSkill, intent_file_handler


class PeopleInSpace(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('space.in.people.intent')
    def handle_space_in_people(self, message):
        self.speak_dialog('space.in.people')


def create_skill():
    return PeopleInSpace()

