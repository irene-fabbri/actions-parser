# An Action is described in the Story file by an object with the keys type , name and options

# An Action's name is a string (that must itself be a valid JSON key) and its options are a collection of key/value pairs that depend on the Action type (a string).

from abc import ABC, abstractmethod
from actions.exceptions import ActionError

class Action(ABC):
    """
    Abstract base class for all Action types.
    Subclasses must implement the `run(input_event)` method.
    """
    def __init__(self, type, name, options):
        """
        :param type: The type of the action (e.g., 'PrintAction').
        :param name: A unique name for the action, used in the event output.
        :param options: A dictionary of configuration values for the action.
        """

        self.type = type
        self.name = name
        self.options = options

    # TYPE getter and setter: only allowed types
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if not isinstance(value, str):
            raise ActionError("Action 'type' must be a string.")
        self._type = value

    # NAME getter and setter: only strings
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ActionError("Action 'name' must be a string.")
        self._name = value

    # OPTIONS getter and setter: only dictionaries
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if not isinstance(value, dict):
            raise ActionError("Action 'options' must be a dictionary.")
        self._options = value

    @abstractmethod
    def run(self, input_event):
        pass