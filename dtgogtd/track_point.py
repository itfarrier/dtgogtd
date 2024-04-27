from collections import namedtuple


TrackPoint = namedtuple(
    "TrackPoint",
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
