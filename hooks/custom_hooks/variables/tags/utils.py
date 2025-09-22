from os import getcwd
from os.path import join
from glob import glob
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

def get_tags(paths):
    cwd = getcwd()
    file_paths = []
    all_tags = []

    for p in paths:
        full_path = join(cwd, p)
        file_paths.extend(list(set(glob(f"{full_path}/**/*.md", recursive=True))))

    for f in file_paths:
        with open(f, 'r') as file:
            metadata = get_metadata(file)
            if 'tags' in metadata:
                all_tags.extend(metadata['tags'])
    
    return list(set(all_tags))
