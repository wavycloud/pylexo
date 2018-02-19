from schematics import models


class PyLexObject(models.Model):

    def __init__(self, *args, **kwargs):
        super(PyLexObject, self).__init__(*args, **kwargs)
        self.initialize()

    def initialize(self):
        pass


class SlotsProperty(PyLexObject):
    pass


class SessionAttributesProperty(PyLexObject):
    pass
