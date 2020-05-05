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

print(json.dumps(datadog_monitors, indent=2, sort_keys=False))


