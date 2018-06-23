from data import Scenario1, Scenario2
from classes.scenario import Scenario


class Bot(object):

    START_BOT = 'Bot> %s'

    """ Class for the Bot will initiate scenarii"""

    def __init__(self, mode='cli'):
        self.first_input = input('Me> ')
        self.mode = mode
        self.inputs = []
        self.intention_detector()

    def intention_detector(self):
        if 'hello' in self.first_input.lower():
            Scenario(self, Scenario1)
        elif 'hi' in self.first_input.lower():
            Scenario(self, Scenario2)
        else:
            self._fallback()

    def get_new_message(self):
        new_input = input('Me>')
        self.inputs.append(new_input)
        return new_input

    def _fallback(self):
        print('Sorry')

    def action_switcher(self, type, data):
        REPLY_MODE = {
            'cli':
                {
                    'text': self.output_message,
                    'image': self.output_image_with_url
                },
            'http':
            {
                'text': self.output_message_http,
                'image': self.output_image_with_url_http
            }
        }
        REPLY_MODE[self.mode][type](data)

    #######
    # CLI #
    #######
    def output_message(self, message):
        print(Bot.START_BOT % (message))

    def output_image_with_url(self, image):
        message_show = '(sending image : %s )' % (image)
        print(Bot.START_BOT % (message_show))

    ########
    # HTTP #
    ########
    def output_message_http(self, message):
        message_show = '(sending HTTP request {"text" : "%s" })' % (message)
        print(Bot.START_BOT % (message))

    def output_image_with_url_http(self, image):
        message_show = '(sending HTTP request {"image_url" : "%s" })' % (image)
        print(Bot.START_BOT % (image))
