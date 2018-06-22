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
    def __init__(self, step ,data_connection):
        self.step = step
        self.conditions_list = data_connection
        self.next_step = None

    def launch_connection(self, input):
        self._unpack_and_check_condition(input)
        #to fix
        for step in self.step.scenario.steps:
            if step.id == self.next_step:
                step.launch_actions()
                break


    def _unpack_and_check_condition(self, input):
        condition = self.conditions_list.get('condition')
        if type(condition) == list:
            for c in condition:
                if input == c or input in c:
                    self.next_step = self.conditions_list.get('next_step')
        else:
            if input == condition or input in condition:
                self.next_step = self.conditions_list.get('next_step')
