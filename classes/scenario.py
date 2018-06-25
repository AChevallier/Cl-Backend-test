from classes.step import Step


class Scenario(object):

    def __init__(self, bot, data):
        '''
            Constructor of scenario
            just loading data and launch the first step
            to launch the scenario
        '''
        self.bot = bot
        self.name = data.get('name')
        self.steps = self._load_steps(data.get('steps'))
        self.steps[0].launch_actions()

    def _load_steps(self, steps_data):
        '''
            loading data from data.py
        '''
        list_initialised_step = []
        for step in steps_data:
            list_initialised_step.append(Step(self, step))
        return list_initialised_step
