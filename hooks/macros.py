from os import getcwd
from os.path import join
from glob import glob
from custom_hooks.utils import get_metadata
from dateutil import parser
from datetime import date, datetime

DOCS_ROOT = 'docs'
DOCS_PATH = join(getcwd(), DOCS_ROOT)

class Img:
    def __init__(self, path, alt='', date_val='', site_uri='', class_name='photo'):
        self.site_uri = site_uri
        self.path = path
        if date_val == '' or date_val is None:
            self.date = date.min
        else:
            self.date = date_val if isinstance(date_val, date) else parser.parse(date_val)
        self.alt = alt if alt is not None else ''
        self.class_name = class_name
    
    def to_url(self, path):
        if self.site_uri:
            return join(self.site_uri, path)
        return path
    
    def to_string(self):
        return f'<div class="{self.class_name}"><a class="glightbox" data-type="image" data-width="auto" data-height="auto" href="/{self.path}" data-desc-position="bottom"><img class="photo-preview" loading="lazy" src="/{self.path.replace('images', 'images-resized')}" alt="{self.alt}" /></a></div>'
        return f'<div class="{self.class_name}"><a class="glightbox" data-type="image" data-width="auto" data-height="auto" href="{self.to_url(self.path)}" data-desc-position="bottom"><img class="photo-preview" loading="lazy" src="{self.to_url(self.path.replace('images', 'images-resized'))}" alt="{self.alt}" /></a></div>'
    
    def __repr__(self):
        return f'{{path: {self.path}, alt: {self.alt}, date: {self.date}}}'

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
            date_val = ''
            if 'title' in metadata:
                alt = metadata['title']
            if 'date' in metadata:
                date_val = metadata["date"]['created']
            image = Img(photo_path, alt, date_val, site_uri)
            photos.append(image)
    return sorted(photos, key=lambda e: e.date, reverse=True)

def define_env(env):
    env.variables['photos'] = ''.join([i.to_string() for i in get_photos(env.conf.get('site_url', ''))])
