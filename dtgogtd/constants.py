from enum import Enum
import struct


class Constants:
    HEADER_SIZE = 4
    POINT_FORMAT = "<ddddddddB"
    POINT_PACK_SIZE = struct.calcsize(POINT_FORMAT)


class LocationSource(Enum):
    EUndefined = 0
    EAppleNative = 1
    EWindowsNative = 2
    EAndroidNative = 3
    EGoogle = 4
    ETizen = 5
    EGeoClue2 = 6
    EPredictor = 7
    EUser = 8
