import pytest
from actions import getActionTypeClass
from actions.exceptions import ActionError

from Story import Story

def testValid():
    storyDictionary = {"actions":[
        {
            "type": "HTTPRequestAction",
            "name": "location",
            "options": {
                "url": "http://free.ipwhois.io/json/"
            }
        },
        {
            "type": "PrintAction",
            "name": "greet",
            "options": {
                "message": "You are my favourite person in {{location.country}}"
            }
        }
    ]}

    story = Story(storyDictionary)
    story.run()
    
    assert story.event["location"]["continent"] == "Europe"
    assert story.event["greet"] == "You are my favourite person in Italy"

def testInvalidAction():
    with pytest.raises(ActionError, match="Failed to create action"):
        storyDictionary = {"actions":[
        {
            "type": "HTTPRequestAction",
            "name": "location",
            "options": {
                "url": "http://free.ipwhois.io/json/"
            }
        },
        {
            "type": "HappinessAction",
            "name": "greet",
            "options": {
                "message": "You are my favourite person in {{location.country}}"
            }
        }
        ]}

        story = Story(storyDictionary)