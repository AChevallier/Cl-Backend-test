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
        self.check()

    def check(self):
        print(self.conditions_list.get('condition'))
        # for item in self.conditions_list:
            # if item.condition in 'step.input_message':
            # print(item.get('condition'))
