from classes.action import Action
from classes.connection import Connection

class Step(object):
    """docstring for Step.

     Args:
            param1 (object): Object step link to this connection
            param2:"""
    def __init__(self, scenario, data_step):
        self.scenario = scenario
        self.id = data_step.get('id')
        self.name = data_step.get('name')
        print('loaded '+self.name)
        if 'actions' in data_step:
            self.actions = self._load_actions(data_step.get('actions'))
        if 'connections' in data_step:
            self.connections = self._load_connections(data_step.get('connections'))

    def _load_actions(self, data):
        list_initialised_actions = []
        for action in data:
            list_initialised_actions.append(Action(self,action))

    def _load_connections(self, data):
        list_initialised_connections = []
        for connection in data:
            list_initialised_connections.append(Connection(self,connection))
