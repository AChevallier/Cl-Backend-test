class Connection(object):
    """docstring for Action.

     Args:
            param1 (object): Object step link to this connection
            param2:
            [
                {'condition':'pizza',
                'next_step': 'Step'},
                {'condition':'toto',
                'next_step': 'Step'}
            ]"""

    def __init__(self, step, data_connection):
        self.step = step
        self.conditions_list = data_connection
        self.next_step = None

    def launch_connection(self, input_user):
        self._unpack_and_check_condition(input_user)
        # to launch the next step
        for step in self.step.scenario.steps:
            if step.id == self.next_step:
                step.launch_actions()
                break

    def _unpack_and_check_condition(self, input_user):
        condition = self.conditions_list.get('condition')
        if type(condition) == list:
            for c in condition:
                if input_user == c or c in input_user:
                    self.next_step = self.conditions_list.get('next_step')
                    break
        else:
            if input_user == condition or condition in input_user:
                self.next_step = self.conditions_list.get('next_step')
