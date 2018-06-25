from data import Scenario1, Scenario2
from classes.scenario import Scenario
from classes.action_cli import ActionCLI
from classes.action_http import ActionHTTP

class Bot(object):

    START_BOT = 'Bot> %s'

    """ Class for the Bot will initiate scenarii"""

    def __init__(self, mode='cli'):
        self.first_input = input('Me> ')
        self.mode = mode
        self.inputs = []
        #select the mode of answers
        if mode == 'http':
            self.object_mode = ActionHTTP()
        else:
            self.object_mode = ActionCLI()
        self.intention_detector()

    def intention_detector(self):
        '''
            check the first input of the user and choose the right scenario
            OR use _fallback
        '''
        if 'hello' in self.first_input.lower():
            Scenario(self, Scenario1)
        elif 'hi' in self.first_input.lower():
            Scenario(self, Scenario2)
        else:
            self._fallback()

    def get_new_message(self):
        '''
            ask new input to the user
        '''
        new_input = input('Me>')
        self.inputs.append(new_input)
        return new_input

    def _fallback(self):
        print('Sorry')

    def action_switcher(self, type, data):
        '''
        choose which type of action for answer
        '''
        {
            'text': self.object_mode.output_message,
            'image': self.object_mode.output_image
        }.get(type)(data)
