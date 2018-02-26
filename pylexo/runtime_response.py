from schematics import types

from .base import PyLexObject, GenericAttachmentsProperty


class ResponseCardRuntimeProperty(PyLexObject):
    version = types.StringType('')
    contentType = types.StringType('application/vnd.amazonaws.card.generic')
    genericAttachments = types.ListType(types.ModelType(GenericAttachmentsProperty))
    """ :type : List[GenericAttachmentsProperty] """


class MessageFormats:
    PlainText = 'PlainText'
    CustomPayload = 'CustomPayload'
    SSML = 'SSML'
    Composite = 'Composite'


class DialogStates:
    ElicitIntent = 'ElicitIntent'
    ConfirmIntent = 'ConfirmIntent'
    ElicitSlot = 'ElicitSlot'
    Fulfilled = 'Fulfilled'
    ReadyForFulfillment = 'ReadyForFulfillment'
    Failed = 'Failed'


class LexPostTextResponse(PyLexObject):
    intentName = types.StringType(default='')
    slots = types.DictType(types.StringType())
    sessionAttributes = types.DictType(types.StringType())
    message = types.StringType(default='')
    messageFormat = types.StringType(default='')
    dialogState = types.StringType(default='')
    slotToElicit = types.StringType(default='')
    responseCard = types.ModelType(ResponseCardRuntimeProperty, serialize_when_none=False,
                                   default=ResponseCardRuntimeProperty())

    def is_plain_text(self):
        return self.messageFormat == MessageFormats.PlainText

    def is_ssml(self):
        return self.messageFormat == MessageFormats.SSML

    def is_composite(self):
        return self.messageFormat == MessageFormats.Composite

    def is_custom_payload(self):
        return self.messageFormat == MessageFormats.CustomPayload

    def is_elicit_intent(self):
        return self.dialogState == DialogStates.ElicitIntent

    def is_confirm_intent(self):
        return self.dialogState == DialogStates.ConfirmIntent

    def is_elicit_slot(self):
        return self.dialogState == DialogStates.ElicitSlot

    def is_fulfilled(self):
        return self.dialogState == DialogStates.Fulfilled

    def is_ready_for_fulfillment(self):
        return self.dialogState == DialogStates.ReadyForFulfillment

    def is_failed(self):
        return self.dialogState == DialogStates.Failed
