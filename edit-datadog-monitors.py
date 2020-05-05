#! /usr/bin/env python
#
# Save existing monitors to a file and allow them to be edited in place, before uploading them again.

import json
import os
from datadog import initialize
from dotenv import load_dotenv

load_dotenv()

options = {
    'site': os.getenv("DATADOG_HOST"),
    'api_key': os.getenv("DD_API_KEY"),
    'app_key': os.getenv("DD_APP_KEY")
}

initialize(**options)

from datadog import api

datadog_monitors = api.Monitor.get_all()

# print(json.dumps(datadog_monitors, indent=2, sort_keys=False))

with open('existing_monitors.json', 'w') as outfile:
    json.dump(datadog_monitors, outfile, indent=2, sort_keys=False)

while True:
    wait = input("Edit 'existing_monitors.json', save, then press a key to upload the changes.")
    with open('existing_monitors.json', 'r') as infile:
        try:
            imported_datadog_monitors = json.load(infile)
            break
        except ValueError as err:
            print("Check your json and try again!", err)

for monitor in imported_datadog_monitors:
    print("Uploading " + monitor['name'])
    response = api.Monitor.update(**monitor)
