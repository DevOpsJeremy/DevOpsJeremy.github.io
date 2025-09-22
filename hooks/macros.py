from os import getcwd
from os.path import join
from glob import glob
from custom_hooks.utils import get_metadata

DOCS_ROOT = 'docs'
DOCS_PATH = join(getcwd(), DOCS_ROOT)

class Img:
    def __init__(self, path, alt='', site_uri=''):
        self.site_uri = site_uri
        self.path = path
        self.alt = alt if alt is not None else ''
    
    def to_url(self, path):
        if self.site_uri:
            return join(self.site_uri, path)
        return path
    
    def to_string(self):
        return f'<img class="photo-preview" src="{self.to_url(self.path)}" alt="{self.alt}" />'
    
    def __repr__(self):
        return f'{{path: {self.path}, alt: {self.label}}}'

def get_photos(site_uri=''):
    PHOTOGRAPHY_ROOT = "other/Photography"
    PHOTOGRAPHY_PATH = join(DOCS_PATH, PHOTOGRAPHY_ROOT)
    IMAGES_ROOT = "images"
    IMAGES_PATH = join(PHOTOGRAPHY_PATH, IMAGES_ROOT)
    IMAGES_PATH_SHORT = join(PHOTOGRAPHY_ROOT, IMAGES_ROOT)

    photos = []
    docs = glob(join(PHOTOGRAPHY_PATH, '**', '*.md'), recursive=True)
    for doc in docs:
        with open(doc, 'r') as file:
            metadata = get_metadata(file)
        if 'photo' in metadata:
            photo_path = join(IMAGES_PATH_SHORT, metadata['photo'])
            alt = ''
            if 'title' in metadata:
                alt = metadata['title']
            image = Img(photo_path, alt, site_uri)
            photos.append(image.to_string())
    return photos

def define_env(env):
    env.variables['photos'] = '<br>'.join(get_photos(env.conf.get('site_url', '')))
