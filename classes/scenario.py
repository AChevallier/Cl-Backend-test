from classes.step import Step


class Scenario(object):
    """docstring for Step.

     Args:
            param1 (object): Bot
            param2:"""

    def __init__(self, bot, data):
        self.bot = bot
        self.name = data.get('name')
        self.steps = self._load_steps(data.get('steps'))
        self.steps[0].launch_actions()

    def _load_steps(self, steps_data):
        list_initialised_step = []
        for step in steps_data:
            list_initialised_step.append(Step(self, step))
        return list_initialised_step
