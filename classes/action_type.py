class ActionType(object):
    START_BOT = 'Bot> %s'
    """
        Should return a text message from the bot to the user
        Depending on the type cli or http (whatever)
    """
    def output_message(self, message):
        raise NotImplementedError( "Should have implemented this" )

    """
        Should return a url image from the bot to the user
        Depending on the type cli or http (whatever)
    """
    def output_image(self, message):
        raise NotImplementedError( "Should have implemented this" )
