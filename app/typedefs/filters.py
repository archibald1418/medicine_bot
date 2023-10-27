from . import MsgFilter

IsAnyMessage: MsgFilter = lambda msg: True
IsTextMessage: MsgFilter = lambda msg: msg.content_type == "text"
BlockHandler: MsgFilter = lambda msg: False
