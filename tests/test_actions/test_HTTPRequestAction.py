import pytest
from actions.HTTPRequestAction import HTTPRequestAction
from actions.exceptions import ActionError


def testSingleEvent():
    action = HTTPRequestAction("HTTPRequest", "location", {"url":"http://free.ipwhois.io/json/"})
    result = action.run({"personal": {"name": "Alice"}})
    
    assert result["location"]["continent"] == "Europe"
    assert result["location"]["country_code"] == "IT"

def testInvalidUrl():
    with pytest.raises(ActionError):
        action = HTTPRequestAction("HTTPRequest", "location", {"url":"http://dummywebsite.io/json/"})
        result = action.run({"personal": {"name": "Alice"}})

def testMissingURL():
    with pytest.raises(ActionError, match="HTTPRequestAction requires a 'url' option as a string."):
        HTTPRequestAction("HTTPRequest", "location", {"urlo":"http://free.ipwhois.io/json/"})
    with pytest.raises(ActionError, match = "HTTPRequestAction requires a 'url' option as a string."):
        HTTPRequestAction("HTTPRequest", "location", {})

def testInvalidFormat():
    # get request to a API that does not return json
    with pytest.raises(ActionError, match="Expected JSON response"):
        HTTPRequestAction("HTTPRequest", "imageAPI", {"url":"https://api.dicebear.com/6.x/pixel-art/svg"}).run({})