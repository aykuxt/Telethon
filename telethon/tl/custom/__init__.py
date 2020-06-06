"""
The `telethon.tl.custom` package contains custom classes that the library
uses in order to make working with Telegram easier. Only those that you
are supposed to use will be documented here. You can use undocumented
ones at your own risk.

More often than not, you don't need to import these (unless you want
type hinting), nor do you need to manually create instances of these
classes. They are returned by client methods.
"""
from .adminlogevent import AdminLogEvent
from .draft import Draft
from .dialog import Dialog
from .inputsizedfile import InputSizedFile
from .messagebutton import MessageButton
from .forward import Forward
from .message import Message
from .button import Button
from .inlinebuilder import InlineBuilder
from .inlineresult import InlineResult
from .inlineresults import InlineResults
from .conversation import Conversation
from .qrlogin import QRLogin
