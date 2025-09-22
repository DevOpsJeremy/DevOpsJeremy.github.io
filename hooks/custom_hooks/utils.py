from yaml import safe_load
import re

def get_metadata(file):
    text = file.read()

    if not text.startswith('---'):
        return {}
    
    pattern = r'(^-{3}\n([^\n]*\n)+)(?:-{3})'
    compile = re.compile(pattern, re.MULTILINE)

    matches = compile.match(text)

    if not matches:
        return {}

    metadata_string = matches.group(1)

    try:
        return safe_load(metadata_string)
    except:
        return {}
