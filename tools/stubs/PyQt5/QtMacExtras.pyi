# The PEP 484 type hints stub file for the QtMacExtras module.
#
# Generated by SIP 5.0.0
#
# Copyright (c) 2019 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtGui
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QMacPasteboardMime(sip.simplewrapper):

    class QMacPasteboardMimeType(int): ...
    MIME_DND = ... # type: 'QMacPasteboardMime.QMacPasteboardMimeType'
    MIME_CLIP = ... # type: 'QMacPasteboardMime.QMacPasteboardMimeType'
    MIME_QT_CONVERTOR = ... # type: 'QMacPasteboardMime.QMacPasteboardMimeType'
    MIME_QT3_CONVERTOR = ... # type: 'QMacPasteboardMime.QMacPasteboardMimeType'
    MIME_ALL = ... # type: 'QMacPasteboardMime.QMacPasteboardMimeType'

    @typing.overload
    def __init__(self, t: int) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QMacPasteboardMime') -> None: ...

    def count(self, mimeData: QtCore.QMimeData) -> int: ...
    def convertFromMime(self, mime: str, data: typing.Any, flav: str) -> typing.List[QtCore.QByteArray]: ...
    def convertToMime(self, mime: str, data: typing.Iterable[typing.Union[QtCore.QByteArray, bytes, bytearray]], flav: str) -> typing.Any: ...
    def flavorFor(self, mime: str) -> str: ...
    def mimeFor(self, flav: str) -> str: ...
    def canConvert(self, mime: str, flav: str) -> bool: ...
    def convertorName(self) -> str: ...


class NSToolbar(sip.simplewrapper): ...


class QMacToolBar(QtCore.QObject):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, identifier: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def nativeToolbar(self) -> NSToolbar: ...
    def detachFromWindow(self) -> None: ...
    def attachToWindow(self, window: QtGui.QWindow) -> None: ...
    def allowedItems(self) -> typing.List['QMacToolBarItem']: ...
    def setAllowedItems(self, allowedItems: typing.Iterable['QMacToolBarItem']) -> None: ...
    def items(self) -> typing.List['QMacToolBarItem']: ...
    def setItems(self, items: typing.Iterable['QMacToolBarItem']) -> None: ...
    def addSeparator(self) -> None: ...
    def addAllowedItem(self, icon: QtGui.QIcon, text: str) -> 'QMacToolBarItem': ...
    def addItem(self, icon: QtGui.QIcon, text: str) -> 'QMacToolBarItem': ...


class NSToolbarItem(sip.simplewrapper): ...


class QMacToolBarItem(QtCore.QObject):

    class StandardItem(int): ...
    NoStandardItem = ... # type: 'QMacToolBarItem.StandardItem'
    Space = ... # type: 'QMacToolBarItem.StandardItem'
    FlexibleSpace = ... # type: 'QMacToolBarItem.StandardItem'

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def activated(self) -> None: ...
    def nativeToolBarItem(self) -> NSToolbarItem: ...
    def setIcon(self, icon: QtGui.QIcon) -> None: ...
    def icon(self) -> QtGui.QIcon: ...
    def setText(self, text: str) -> None: ...
    def text(self) -> str: ...
    def setStandardItem(self, standardItem: 'QMacToolBarItem.StandardItem') -> None: ...
    def standardItem(self) -> 'QMacToolBarItem.StandardItem': ...
    def setSelectable(self, selectable: bool) -> None: ...
    def selectable(self) -> bool: ...


class QtMac(sip.simplewrapper):

    def isMainWindow(self, window: QtGui.QWindow) -> bool: ...
    def badgeLabelText(self) -> str: ...
    def setBadgeLabelText(self, text: str) -> None: ...


def qRegisterDraggedTypes(types: typing.Iterable[str]) -> None: ...
