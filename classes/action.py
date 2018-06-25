class Action(object):

    def __init__(self, step, data):
        self.step = step
        self.type = data.get('type')
        self.data = data.get('data')

    def answer(self):
        """
            answer the user in a good way (cli/http)
        """
        self.step.scenario.bot.action_switcher(self.type, self.data)
