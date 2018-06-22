from data import Scenario1
from classes.scenario import Scenario

class Bot(object):

    START_BOT = 'Bot> %s'

    """ Class for the Bot will initiate scenarii"""
    def __init__(self, mode = 'cli'):
        self.first_input = input('Me> ')
        self.mode = mode
        self.inputs = []
        if self.first_input == 'hello':
            Scenario(self, Scenario1)
        else:
            _fallback()

    def intention_detector(self,input):
        if 'hello' in self.first_input.lower():
            Scenario(self, Scenario1)

    def _fallback(self):
        print('Sorry')

    def output_message(self, message):
        print(Bot.START_BOT % (message))

    def output_image_with_url(self, image):
        message_show = '(sending image : %s )' % (image)
        print(Bot.START_BOT % (message_show))

    def get_new_message(self):
        new_input = input('Me>')
        self.inputs.append(new_input)
        return new_input
