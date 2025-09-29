# Reference documentation for MkDocs plugins: https://www.mkdocs.org/dev-guide/plugins/

from mkdocs.plugins import BasePlugin

log: logging.Logger = logging.getLogger("mkdocs")

class CustomHooksPlugin(BasePlugin):
	def on_files(self, files, config):
        for f in files:
            log.info(f"File: {[i for i in dir(f) if not i.startswith('_')]}")
