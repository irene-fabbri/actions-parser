import re

def interpolate(input, event):
    # need to interpolate {{ key.value }}
    pattern = re.compile(r"\{\{\s*(\w+\.\w+)\s*\}\}")

    def replace(match):
        try:
            key, value = match.group(1).split('.',1)
            item = event[key][value]
            return str(item)
        except Exception:
            return ''

    return pattern.sub(replace, input)