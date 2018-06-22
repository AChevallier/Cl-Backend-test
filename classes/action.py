class Action(object):
    """docstring for Action.

     Args:
            param1 (object): Object step link to this action
            param2:"""
    def __init__(self, step ,arg):
        pass
        # self.arg = arg
        # self.step = step
        # self.type = arg.type
        # self.answer_text = arg.answer_text

    def answer(self):
        print(self.answer_text)
        return True
