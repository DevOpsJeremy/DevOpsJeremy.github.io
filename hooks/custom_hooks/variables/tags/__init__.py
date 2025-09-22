from .utils import get_tags

docs_root = 'docs'
tech_dirs = [
    f"{docs_root}/documentation",
    f"{docs_root}/blog",
    f"{docs_root}/drafts"
]
photography_dirs = [
    f"{docs_root}/other/Photography"
]

tech = get_tags(tech_dirs)
photography = get_tags(photography_dirs)
