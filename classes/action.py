class Action(object):
    """docstring for Action.

     Args:
            param1 (object): Object step link to this action
            param2:"""

    def __init__(self, step, data):
        self.step = step
        self.type = data.get('type')
        self.data = data.get('data')

    def answer(self):
        """
            
        """
        self.step.scenario.bot.action_switcher(self.type, self.data)
        if self.step.connections:
            self.step.launch_connections()
