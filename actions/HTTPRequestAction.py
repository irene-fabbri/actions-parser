# HTTPRequestAction - make a simple HTTP GET request against a given URL.

# Actions of this type take a single option, url the value of which must be a string.
# Any non-2xx HTTP response or network failure while making a HTTP request should result in immediate termination of the program.
# Only requests against URLs that return JSON bodies are supported. The body is parsed and set as the Action's output.

from json.decoder import JSONDecodeError
from actions.Action import Action
from actions.exceptions import ActionError

import requests

class HTTPRequestAction(Action):
    """
    An Action that performs an HTTP GET request to a specified URL
    and stores the JSON response as part of the event.

    Attributes:
        type (str): The type of action (must be 'HTTPRequestAction').
        name (str): The unique name of the action.
        options (dict): Must contain a single key 'url' with a string value.

    Methods:
        run(input_event):
            Makes the HTTP request to the given URL (after interpolating any placeholders)
            and returns an event that includes the JSON response merged with the input_event.
    """
    
    def __init__(self, type, name, options):
        super().__init__(type,name, options)
        if "url" not in options or not isinstance(options["url"], str):
            raise ActionError("HTTPRequestAction requires a 'url' option as a string.")

    def run(self, input_event):
        # get url
        url = self.options.get("url", "")
        try:
            # make HTTP request
            response = requests.get(url, headers={'accept':'application/json'})
            response.raise_for_status()

            # check for json body
            print(response.headers)
            content_type = response.headers.get("Content-Type", "")
            if "application/json" not in content_type:
                raise ActionError(f"Expected JSON response but got '{content_type}'", action_type=self.type, action_name=self.name)

            # parse json
            data = response.json()

        except JSONDecodeError:
            raise ActionError(
                f"Response from {url} could not be decoded as JSON.",
                action_type=self.type,
                action_name=self.name
            )
        except Exception as exception:
            raise ActionError(str(exception), action_type=self.type, action_name=self.name)
        # add the json response to the event
        input_event[self.name] = data

        return input_event