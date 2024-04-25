from gpx_converter import Converter


def gpx_to_dat(input_file, output_file):
    df = Converter(input_file).gpx_to_dataframe()
    print("df", df)
    print("input_file", input_file)
    print("output_file", output_file)
