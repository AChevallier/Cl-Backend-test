from classes.action import Action
from classes.connection import Connection


class Step(object):

    def __init__(self, scenario, data_step):
        self.scenario = scenario
        self.id = data_step.get('id')
        self.name = data_step.get('name')
        self.actions = None
        self.connections = None
        #Loading data
        if 'actions' in data_step:
            self.actions = self._load_actions(data_step.get('actions'))
        if 'connections' in data_step:
            self.connections = self._load_connections(
                data_step.get('connections'))

    def launch_actions(self):
        '''
        launch each action one by one
        and then launch the connections
        '''
        for action in self.actions:
            action.answer()
        if self.connections:
            self.launch_connections()
    def launch_connections(self):
        '''
        Get the message from user
        and launch the connection
        '''
        input = self.scenario.bot.get_new_message()
        for connection in self.connections:
            connection.launch_connection(input)

    def _load_actions(self, data):
        list_initialised_actions = []
        for action in data:
            list_initialised_actions.append(Action(self, action))
        return list_initialised_actions

    def _load_connections(self, data):
        list_initialised_connections = []
        for connection in data:
            list_initialised_connections.append(Connection(self, connection))
        return list_initialised_connections
