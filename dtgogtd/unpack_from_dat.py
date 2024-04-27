# Adapted from https://gist.github.com/lambdaupb/21bfa917292d45c9b4fef4964799b3d4

from collections import namedtuple
import struct
from enum import Enum

# Global values, might change if maps.me modifies their format.
POINT_PATTERN = "<ddddddddB"
POINT_PACK_SIZE = struct.calcsize(POINT_PATTERN)
HEADER_SIZE = 4


class PointSource(Enum):
    EUndefined = 0
    EAppleNative = 1
    EWindowsNative = 2
    EAndroidNative = 3
    EGoogle = 4
    ETizen = 5
    EGeoClue2 = 6
    EPredictor = 7
    EUser = 8


Point = namedtuple(
    "Point",
    (
        "timestamp",
        "latitude",
        "longitude",
        "altitude",
        "speedMpS",
        "bearing",
        "horizontalAccuracy",
        "verticalAccuracy",
        "source",
    ),
)


def make_point(raw_point):
    return Point(*raw_point[:-1], source=PointSource(raw_point[-1]))


def load_from_dat_file(filehandle):
    data_input = filehandle.read()
    data_len = len(data_input) - HEADER_SIZE
    start = HEADER_SIZE
    end = HEADER_SIZE + (POINT_PACK_SIZE * data_len) // POINT_PACK_SIZE
    raw_points = data_input[start:end]
    points = map(make_point, struct.iter_unpack(POINT_PATTERN, raw_points))

    return points
