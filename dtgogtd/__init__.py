import argparse

from dat_to_gpx import dat_to_gpx
from gpx_to_dat import gpx_to_dat


def main():
    parser = argparse.ArgumentParser(
        description="Convert Organic Maps gps_track.dat file to GPX or vice versa."
    )

    parser.add_argument(
        "input_file",
        help="Input file (Organic Maps gps_track.dat)",
        metavar="IN",
    )

    parser.add_argument(
        "output_file",
        help="Output file (GPX format)",
        metavar="OUT",
    )

    args = parser.parse_args()

    if args.input_file.endswith("gpx"):
        gpx_to_dat(args.input_file, args.output_file)
    else:
        dat_to_gpx(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
