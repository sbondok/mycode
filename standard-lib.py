#!/usr/bin/env python3

import urllib.request
import json

URL = "https://api-web.nhle.com/v1/standings/now" 

# Get request to a url
resp = urllib.request.urlopen(URL)

# All byte - not readable!
content = resp.read()

print(type(content))

#Let us decode it -JSON to Python
#final = json.loads(content.decode("utf-8"))

#print(final)
