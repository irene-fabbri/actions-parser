from actions import getActionTypeClass
from actions.exceptions import ActionError

# A Story file contains a single JSON object.

# That object has a single key actions, mapping to an array of Actions.

class Story:

    def __init__(self, storyDictionary):
        # turn action dictionary into action array
        self.actionArray = []
        self.event = {}

        actions = storyDictionary.get("actions")       
        for action in actions:
            try:
                # get parameters
                type = action.get("type")
                name = action.get("name")
                options = action.get("options",{})

                # select the appropriate action class
                actionClass = getActionTypeClass(type)
                # create an instance of that class
                actionInstance = actionClass(type, name, options)
                # add instance to the actions array
                self.actionArray.append(actionInstance)
            except Exception as error:
                raise ActionError(f"Failed to create action '{action}'")

    def run(self):
        # run all the actions in the action array
        for action in self.actionArray:
            self.event = action.run(self.event)