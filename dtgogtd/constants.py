import struct


class Constants:
    HEADER_SIZE = 4
    POINT_FORMAT = "<ddddddddB"
    POINT_PACK_SIZE = struct.calcsize(POINT_FORMAT)
