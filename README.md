# 🧩 Actions Parser

A simple Python tool that runs a sequence of **actions** defined in a JSON file. Actions currently supported include:

- `PrintAction`: Print a message to the console.
- `HTTPRequestAction`: Make an HTTP GET request and extract data from the response.

## 📁 Project Structure

```
actions-parser/
├── __main__.py             # Entry point (run with `-m`)
├── actions/                # All supported action classes
├── schemas/                # JSON schema for story validation
├── tests/                  # Unit tests
├── utils.py                # Shared utility functions
├── Story.py                # Main Story runner
└── README.md               # This file
```

---

## 🧪 Example Story File

Create a JSON file like this:

```json
{
  "actions": [
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
  ]
}
```

---

## 🚀 How to Run

From the root folder:

```bash
python -m actions_parser path/to/story.json
```

If the JSON is invalid, the program will exit with an error.

---

## 🧩 Supported Actions

### 🔸 PrintAction

Prints a string to the console, with support for template interpolation using `{{key.value}}`.

### 🔸 HTTPRequestAction

Sends a GET request to the specified `url`, expects a JSON response, and saves the result into the event context.

---

## ✅ Tests

Run all tests using:

```bash
pytest
```

Tests are stored in the `tests/` folder and organized by module. The project uses `pytest` and includes validation for:
- Schema parsing
- Input argument errors
- File reading
- Each individual action
- Full story execution

---

## 📐 Validation

Before executing, each story is validated against a schema (`schemas/story_schema.json`) using `jsonschema`.

---

## 🛠️ Development Notes

- Python 3.10+ recommended.
- Pure standard library + `requests` + `jsonschema`.
- Extendable: just add your new action class and register it in `actions/__init__.py`.

---

## 📄 License
This project is intendend for educational purposes and that is why contribution are not accepted. However, if you have suggestions on how to make the project better, feel free to reach out and give me suggestions.

This project is licensed under the This project is licensed under the [MIT License](./LICENSE).

---