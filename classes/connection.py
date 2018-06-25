class Connection(object):

    def __init__(self, step, data_connection):
        self.step = step
        self.conditions_list = data_connection

    def launch_connection(self, input_user):
        '''
            launch the connection, do the check in _unpack_and_check_condition
            and check in steps list where is the next step to do
        '''
        next_step_id = self._unpack_and_check_condition(input_user)
        # to launch the next step
        for step in self.step.scenario.steps:
            if step.id == next_step_id:
                step.launch_actions()
                break

    def _unpack_and_check_condition(self, input_user):
        '''
            check the input of the user with the condition in the Connection
            and get the id of the next step to launch
        '''
        condition = self.conditions_list.get('condition')
        if type(condition) == list:
            for c in condition:
                if input_user == c or c in input_user:
                    return self.conditions_list.get('next_step')
                    break
        else:
            if input_user == condition or condition in input_user:
                return self.conditions_list.get('next_step')
