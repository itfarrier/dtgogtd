from datetime import datetime, timedelta
from constants import LocationSource
from track_point import TrackPoint
import random


def generate():
    # Define the start and end timestamps
    end_timestamp = datetime(2024, 4, 28)  # End timestamp
    start_timestamp = end_timestamp - timedelta(days=7)  # Start timestamp

    # Generate points
    points = []
    current_timestamp = start_timestamp
    while current_timestamp < end_timestamp:
        # Generate random latitude and longitude (for demonstration)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)

        # Generate other random attributes (for demonstration)
        altitude = random.uniform(0, 100)
        speed = random.uniform(0, 30)
        bearing = random.uniform(0, 360)
        horizontal_accuracy = 5
        vertical_accuracy = -1
        source = LocationSource.EAppleNative  # Randomly select source

        # Create the point and append it to the list
        points.append(
            TrackPoint(
                altitude=altitude,
                bearing=bearing,
                horizontalAccuracy=horizontal_accuracy,
                latitude=latitude,
                longitude=longitude,
                source=source,
                speedMpS=speed,
                timestamp=current_timestamp.timestamp(),
                verticalAccuracy=vertical_accuracy,
            )
        )

        # Move to the next second
        current_timestamp += timedelta(seconds=1)

    return points
