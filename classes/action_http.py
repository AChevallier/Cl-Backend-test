from classes.action_type import ActionType

class ActionHTTP(ActionType):

    def output_message(self, message):
        message_show = '(sending HTTP request {"text" : "%s" })' % (message)
        print(self.START_BOT % (message))

    """
        Should return a url image from the bot to the user
        Depending on the type cli or http (whatever)
    """
    def output_image(self, image):
        message_show = '(sending HTTP request {"image_url" : "%s" })' % (image)
        print(self.START_BOT % (image))
