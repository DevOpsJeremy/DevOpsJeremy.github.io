# Reference documentation for MkDocs plugins: https://www.mkdocs.org/dev-guide/plugins/

import logging
from mkdocs.plugins import BasePlugin

log: logging.Logger = logging.getLogger("mkdocs")

class CustomHooksPlugin(BasePlugin):
    pass
