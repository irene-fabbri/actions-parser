from .actions import getActionTypeClass
# A Story file contains a single JSON object.

# That object has a single key actions, mapping to an array of Actions.

class Story:

    def __init__(self, storyDictionary):
        # turn action dictionary into action array
        self.actionArray = []

        for action in storyDictionary["actions"]:
            # get parameters
            type = action.get("type")
            name = action.get("name")
            options = action.get("options")

            # select the appropriate action class
            actionClass = getActionTypeClass(type)
            # create an instance of that class
            actionInstance = actionClass(type, name, options)
            # add instance to the actions array
            self.actionArray.append(actionInstance)
    def run(self):
        # run all the actions in the action array
        event = {}
        for action in self.actionArray:
            event = action.run(event)
        return event