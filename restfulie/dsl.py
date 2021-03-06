from processor import *
from parser import Parser

class Dsl:

    def __init__ (self, uri):
        self.uri = uri
        self.processors = [RedirectProcessor(),
                           PayloadMarshallingProcessor(),
                           ExecuteRequestProcessor(),]
        self.headers = {}

    def __getattr__(self, name):
        if self._is_verb(name):
            self.verb = name.upper()
            return self.process_flow
        else:
            raise AttributeError(name)

    def _is_verb(self, name):
        return name in ["get", "delete", "trace", "head", "options", "post", "put", "patch"]

    def use(self, feature):
        self.processors.insert(0, feature)
        return self

    def as_(self, content_type):
        self.headers["Content-Type"] = content_type
        return self

    def accepts(self, content_type):
        self.headers['Accept'] = content_type
        return self

    def process_flow(self, env={}):
        procs = list(self.processors)
        return Parser(procs).follow(self, env)
