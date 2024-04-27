# Adapted from https://gist.github.com/lambdaupb/21bfa917292d45c9b4fef4964799b3d4
from collections import namedtuple
import struct
from constants import LocationSource
from constants import Constants


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
    return Point(*raw_point[:-1], source=LocationSource(raw_point[-1]))


def load_from_dat_file(filehandle):
    data_input = filehandle.read()
    data_len = len(data_input) - Constants.HEADER_SIZE
    start = Constants.HEADER_SIZE
    end = Constants.HEADER_SIZE + (Constants.POINT_PACK_SIZE * data_len)
    raw_points = data_input[start:end]
    points = map(make_point, struct.iter_unpack(Constants.POINT_FORMAT, raw_points))

    return points
