# PrintAction - print a given message to STDOUT.

# Actions of this type takes a single option message, the value of which must be a string.

from .Action import Action

class PrintAction(Action):
    """
    An Action that prints a formatted message to standard output.

    Attributes:
        type (str): The type of action (must be 'PrintAction').
        name (str): The unique name of the action.
        options (dict): Must contain a single key 'message' with a string value.

    Methods:
        run(input_event):
            Interpolates the message string using values from the input_event
            and prints the result to STDOUT. Returns the input_event unchanged.
    """
    def __init__(self, type, name, options):
        super().__init__(type,name, options)
        if "message" not in options or not isinstance(options["message"], str):
            raise ValueError("PrintAction requires a 'message' option as a string.")

    def run(self, input_event):
        # TODO
        pass