import json
import socket
import requests
from mycroft import MycroftSkill, intent_file_handler

from mycroft.util.log import getLogger

LOGGER = getLogger(__name__)


def get_json(uri):
    result = requests.get(
            uri,
            headers={'content-type': 'application/json'})
    return result.json()

class PeopleInSpace(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('number.of.people.in.space.intent')
    def handle_number_of_people_in_space(self, message):
        result = get_json("http://api.open-notify.org/astros.json")
        number_of_people_in_space = result['number']
        self.speak_dialog('number.of.people.in.space', {'number': number_of_people_in_space})

    @intent_file_handler('who.is.in.space.intent')
    def handle_who_is_in_space(self, message):
        result = get_json("http://api.open-notify.org/astros.json")
        names = []
        for item in result['people']:
            names.append(item['name'])
        people_in_space = " ".join(names)
        self.speak_dialog('who.is.in.space', {'names': people_in_space})

def create_skill():
    return PeopleInSpace()

