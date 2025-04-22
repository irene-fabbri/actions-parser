import pytest
from actions.PrintAction import PrintAction
from actions.exceptions import ActionError


def testSingleEvent():
    action = PrintAction("PrintAction", "greet", {"message": "Hello, {{personal.name}}!"})
    result = action.run({"personal": {"name": "Alice"}})
    
    assert result["greet"] == "Hello, Alice!"

def testMultipleEvents():
    action = PrintAction("PrintAction", "greet", {"message": "Hello, {{personal.name}}! You are my favourite person in {{location.name}}, {{location.country}}."})
    result = action.run({
        "personal":{"name": "Alice", "surname":"Persichetti", "nickname": "Lilli"},
        "location":{"name": "Rome", "country": "Italy"}
        })
    
    assert result["greet"] == "Hello, Alice! You are my favourite person in Rome, Italy."

def testMissingAttribute():
    action = PrintAction("PrintAction", "greet", {"message": "Hello, {{personal.name}}! You are my favourite person in {{location.latitude}}, {{location.country}}."})
    result = action.run({
        "personal":{"name": "Alice", "surname":"Persichetti", "nickname": "Lilli"},
        "location":{"name": "Rome", "country": "Italy"}
        })
    
    assert result["greet"] == "Hello, Alice! You are my favourite person in , Italy."

def testMissingMessage():
    with pytest.raises(ActionError, match="PrintAction requires a 'message' option as a string."):
        PrintAction("PrintAction", "fail", {})
    with pytest.raises(ActionError, match="PrintAction requires a 'message' option as a string."):
        PrintAction("PrintAction", "greet", {"massage": "Hello, {{personal.name}}!"})