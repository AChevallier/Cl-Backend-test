class Action(object):
    """docstring for Action.

     Args:
            param1 (object): Object step link to this action
            param2:"""
    def __init__(self, step ,data):
        self.step = step
        self.type = data.get('type')
        self.data = data.get('data')


    def answer(self):
        if self.type == 'text':
            self.step.scenario.bot.output_message(self.data)
        elif self.type == 'image':
            self.step.scenario.bot.output_image_with_url(self.data)
        if self.step.connections:
            self.step.launch_connections()
