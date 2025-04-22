from utils import checkArguments, readStoryFile
import pytest
import json
import os

def testValidArgv():
    checkArguments(["script.py", "story.json"])

def testInvalidArgv():
    with pytest.raises(ValueError):
        checkArguments(["script.py"])
    with pytest.raises(ValueError):
        checkArguments(["script.py", "story.json", "bedtime.json"])

def testMissingFile():
    with pytest.raises(FileNotFoundError, match = "File 'nonexistent.json' not found."):
        readStoryFile("nonexistent.json")

def testInvalidFile(tmp_path):
    with pytest.raises(json.JSONDecodeError, match = "Failed to parse JSON"):
        path = tmp_path/"story.json"
        path.write_text("This file is not json")
        readStoryFile(str(path))

def testValidFile(tmp_path):
    text = {
        "actions":[
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
    
    path = tmp_path/"story.json"
    path.write_text(json.dumps(text))
    storyDictionary = readStoryFile(str(path))

    assert storyDictionary["actions"][1]["name"] == "greet"
