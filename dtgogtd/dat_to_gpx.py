from gpx import GPXTrack
from medat import load_from_dat_file


def dat_to_gpx(input_file, output_file):
    with open(input_file, "rb") as inputfile:
        points = load_from_dat_file(inputfile)

    with open(output_file, "w") as outputfile:
        GPXTrack(*points).write(outputfile, True)
