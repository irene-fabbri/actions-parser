class ActionError(Exception):
    """Base class for errors raised by actions."""
    def __init__(self, message, action_type=None, action_name=None):
        super().__init__(message)
        self.action_type = action_type
        self.action_name = action_name

    def __str__(self):
        info = f"ActionError"
        if self.action_type or self.action_name:
            info += f" (type: {self.action_type}, name: {self.action_name})"
        return f"{info}: {self.args[0]}"