from datetime import datetime
from io import StringIO
from xml.etree import ElementTree as ET
from xml.dom import minidom

NS = "http://www.topografix.com/GPX/1/1"


class GPXTrack(object):

    def __init__(self, *points):
        self.root = ET.Element("gpx", xmlns=NS)
        self.trk = ET.SubElement(self.root, "trk")
        self.track_segment(points)

    def track_segment(self, points):
        if points:
            seg = ET.SubElement(self.trk, "trkseg")
            for p in points:
                self.point(seg, p)

    def point(self, segment, pnt):
        pt = ET.SubElement(
            segment, "trkpt", lat=str(pnt.latitude), lon=str(pnt.longitude)
        )

        course = ET.SubElement(pt, "course")
        course.text = str(pnt.bearing)
        ele = ET.SubElement(pt, "ele")
        ele.text = str(pnt.altitude)
        hdop = ET.SubElement(pt, "hdop")
        hdop.text = str(pnt.horizontalAccuracy)
        speed = ET.SubElement(pt, "speed")
        speed.text = str(pnt.speedMpS)
        time = ET.SubElement(pt, "time")
        time.text = datetime.fromtimestamp(pnt.timestamp).isoformat()
        vdop = ET.SubElement(pt, "vdop")
        vdop.text = str(pnt.verticalAccuracy)

        return pt

    def write(self, filehandle, pretty=False):
        if pretty:
            filehandle.write(self.pretty())
        else:
            ET.ElementTree(self.root).write(
                filehandle,
                encoding="unicode",
            )

    def pretty(self):
        rough_string = StringIO()
        self.write(rough_string)
        # Reset to start of string, so minidom can read it...
        rough_string.seek(0)
        reparsed = minidom.parse(rough_string)

        # remove xml declaration like in here https://stackoverflow.com/a/65516230
        return reparsed.childNodes[0].toprettyxml(indent="  ")
