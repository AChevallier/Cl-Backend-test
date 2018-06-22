from data import Scenario1
from classes.scenario import Scenario

class Bot(object):
    """ Class for the Bot will initiate scenarii"""
    def __init__(self, mode = 'cli'):
        self.first_input = input('Me> ')
        self.mode = mode
        self.inputs = []
        Scenario(self, Scenario1)

    def intention_detector(self,input):
        if 'hello' in self.first_input.lower():
            Scenario(self, Scenario1)

    def _fallback(self):
        print('Sorry')

    def output_message(self):
        who = 'Bot>' if self.bot_turn else 'Me>'
        message = 'toto'
        print('%s %s' % (who,message))
