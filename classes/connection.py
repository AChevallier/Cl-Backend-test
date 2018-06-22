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
    def __init__(self, step ,arg):
        self.step = step
        self.conditions_list = arg

    def check(self):
        for item in self.conditions_list:
            if item.condition in step.input_message:
                print('create step')
