# actions/__init__.py

from .PrintAction import PrintAction
from .HTTPRequestAction import HTTPRequestAction
from .exceptions import ActionError


actionTypeMap = {
    "PrintAction": PrintAction,
    "HTTPRequestAction": HTTPRequestAction
}

def getActionTypeClass(typeString):
    if typeString in actionTypeMap:
        return actionTypeMap[typeString]
    raise ActionError(f"Unknown action type: {typeString}")