# actions/__init__.py

from actions.PrintAction import PrintAction
from actions.HTTPRequestAction import HTTPRequestAction
from actions.exceptions import ActionError


actionTypeMap = {
    "PrintAction": PrintAction,
    "HTTPRequestAction": HTTPRequestAction
}

def getActionTypeClass(typeString):
    if typeString in actionTypeMap:
        return actionTypeMap[typeString]
    raise ActionError(f"Unknown action type: {typeString}")