import sys
import json
from . import Story
from .actions.exceptions import ActionError
from .utils import validateStorySchema, checkArguments, readStoryFile

if __name__ == "__main__":
    # check arguments
    checkArguments(sys.argv)    
    try:
        # read story from file
        storyDictionary = readStoryFile(sys.argv[1])

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