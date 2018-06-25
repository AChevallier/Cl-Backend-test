from classes.action_type import ActionType

class ActionCLI(ActionType):

    def output_message(self, message):
        print(self.START_BOT % (message))

    def output_image(self, image):
        message_show = '(sending image : %s )' % (image)
        print(self.START_BOT % (message_show))
