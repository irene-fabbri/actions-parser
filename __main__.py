import sys
import json
from . import Story
from .actions.exceptions import ActionError
from .utils import validateStorySchema

if __name__ == "__main__":
    # check arguments
    if len(sys.argv) != 2:
        print("Usage: python -m actions_parser <story.json>")
        sys.exit(1)
    
    try:
        # read story from file
        with open(sys.argv[1], 'r') as file:
            storyDictionary = json.load(file)
        # validate story schema
        validateStorySchema(storyDictionary)

        # run story
        myStory = Story(storyDictionary)
        myStory.run()

    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as error:
        print(f"Error: Failed to parse JSON - {error}")
        sys.exit(1)
    except ActionError as error:
        print(f"Action failed: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)