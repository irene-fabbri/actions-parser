# actions/__init__.py

from .PrintAction import PrintAction
from .HTTPRequestAction import HTTPRequestAction

actionTypeMap = {
    "PrintAction": PrintAction,
    "HTTPRequestAction": HTTPRequestAction
}

def getActionTypeClass(typeString):
    if typeString in actionTypeMap:
        return actionTypeMap[typeString]
    raise ValueError(f"Unknown action type: {typeString}")