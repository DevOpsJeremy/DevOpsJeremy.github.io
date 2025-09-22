from os import getcwd
from os.path import join
from glob import glob
from ....custom_hooks.utils import get_metadata

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
