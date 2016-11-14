""" This uses the halobeat lib to drop events to stdout """

import halobeat
import json

halobeat_version = str(halobeat.__version__)
config = halobeat.ConfigHelper(halobeat_version=halobeat_version)
halo_events = halobeat.HaloEvents(config)

while True:
    for event in halo_events:
        print(json.dumps(event))
