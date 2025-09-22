from . import utils

__version__ = '0.0.1'

docs_root = 'docs'

categories = {
    'tech': [
        f"{docs_root}/documentation",
        f"{docs_root}/blog",
        f"{docs_root}/drafts"
    ],
    'photography': [
        f"{docs_root}/other/Photography"
    ]
}

tags_tech = utils.get_tags(categories['tech'])
tags_photography = utils.get_tags(categories['photography'])
