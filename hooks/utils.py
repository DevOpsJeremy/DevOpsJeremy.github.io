from os import getcwd
from os.path import join
from .custom_hooks.utils import get_metadata
from glob import glob

def get_photos():
    PHOTO_ROOT = 'docs/other/Photography'
    PHOTO_ROOT_FULL = join(getcwd(), PHOTO_ROOT)

    file_paths = list(set(glob(f"{PHOTO_ROOT_FULL}/**/*.md", recursive=True)))

    for file in file_paths:
        with open(file, 'r') as f:
            metadata = get_metadata(f)
        
        if 'photo' not in metadata:
            continue
