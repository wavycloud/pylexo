from schematics import models, types


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


class GenericAttachmentButtonProperty(PyLexObject):
    text = types.StringType(default='')
    value = types.StringType(default='')


class GenericAttachmentsProperty(PyLexObject):
    title = types.StringType(default='')
    subTitle = types.StringType(default='')
    imageUrl = types.StringType(default='')
    attachmentLinkUrl = types.StringType(default='')
    buttons = types.ListType(types.ModelType(GenericAttachmentButtonProperty), default=[])
    """ :type : List[GenericAttachmentButtonProperty] """
