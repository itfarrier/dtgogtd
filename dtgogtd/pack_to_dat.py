import xml.etree.ElementTree as ET
from datetime import datetime
from track_point import TrackPoint
from constants import LocationSource


def load_from_gpx(gpx_file):
    track_points = []
    tree = ET.parse(gpx_file)
    root = tree.getroot()

    # Namespace for GPX elements
    ns = {"gpx": "http://www.topografix.com/GPX/1/1"}

    # Iterate over track points
    for trkpt in root.findall(".//gpx:trkpt", ns):
        altitude = float(trkpt.find("./gpx:ele", ns).text)
        bearing = float(trkpt.find("./gpx:course", ns).text)
        horizontal_accuracy = float(trkpt.find("./gpx:hdop", ns).text)
        latitude = float(trkpt.attrib["lat"])
        longitude = float(trkpt.attrib["lon"])
        source = LocationSource.EAppleNative  # Not available in GPX
        speed = float(trkpt.find("./gpx:speed", ns).text)
        timestamp = datetime.fromisoformat(
            trkpt.find("./gpx:time", ns).text
        ).timestamp()
        vertical_accuracy = float(trkpt.find("./gpx:vdop", ns).text)

        track_point = TrackPoint(
            timestamp,
            latitude,
            longitude,
            altitude,
            speed,
            bearing,
            horizontal_accuracy,
            vertical_accuracy,
            source,
        )
        track_points.append(track_point)

    return track_points
