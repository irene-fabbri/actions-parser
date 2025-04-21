# A Story file contains a single JSON object.

# That object has a single key actions, mapping to an array of Actions.

class Story:

    def __init__(self, storyDictionary):
        # TODO: action dictionary to action array in constructor
        self.actionArray = []
        self.resultSet = {}

    def run(self):
        # TODO: run all the actions in the action array 
        pass