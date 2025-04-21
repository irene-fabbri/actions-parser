# HTTPRequestAction - make a simple HTTP GET request against a given URL.

# Actions of this type take a single option, url the value of which must be a string.
# Any non-2xx HTTP response or network failure while making a HTTP request should result in immediate termination of the program.
# Only requests against URLs that return JSON bodies are supported. The body is parsed and set as the Action's output.

from .Action import Action
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
            raise ValueError("HTTPRequestAction requires a 'url' option as a string.")

    def run(self, input_event):
        # get url
        url = self.options.get("url", "")
        try:
            # make HTTP request
            response = requests.get(url, headers={'accept':'application/json'})
            response.raise_for_status()
        except Exception as exception:
            raise RuntimeError(f"HTTP request failed for action '{self.name}': {exception}")
        # add the json response to the event
        input_event[self.name] = response.json()

        return input_event