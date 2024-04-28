import struct
from constants import Constants
from generate_points import generate
from pack_to_dat import load_from_gpx


def point_to_raw(point):
    raw_point = (*point[:-1], point.source.value)
    return struct.pack(Constants.POINT_FORMAT, *raw_point)


def write_to_dat_file(points, filehandle):
    raw_data = b""
    for point in points:
        raw_data += point_to_raw(point)
    filehandle.write(b"\x01\x00\x00\x00" + raw_data)


def gpx_to_dat(input_file, output_file):
    with open(input_file, "rb") as inputfile:
        points = load_from_gpx(inputfile)

    with open(output_file, "wb") as outputfile:
        write_to_dat_file(generate(), outputfile)
