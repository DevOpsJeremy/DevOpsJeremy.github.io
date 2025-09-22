from .utils import get_tags

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

tech = get_tags(categories['tech'])
photography = get_tags(categories['photography'])
