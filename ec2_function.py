#!/usr/bin/env python3

import pandas as pd
import math
import random
import json
import sys

# Read the JSON-encoded request body from standard input
request_body = sys.stdin.read()

# If the request body is empty, return a simple response to indicate that the function is running
if not request_body:
    # Output HTTP header
    print("Content-Type: text/plain")
    print()

    # Output response body
    print("Function is running...")
    sys.exit(0)

# Decode the JSON-encoded request body to get the payloads list
payloads = json.loads(request_body)
 
#events = json.loads(event.get('body'))
var95s = []
var99s = []

for payload in payloads:
	#print(payload)
	# generate much larger random number series with same broad characteristics
	simulated = [random.gauss(payload['key1'], payload['key2']) for x in range(payload['key3'])]
	# sort and pick 95% and 99%  - not distinguishing long/short risks here
	simulated.sort(reverse=True)
	var95 = simulated[int(len(simulated)*0.95)]
	#print(var95)
	var99 = simulated[int(len(simulated)*0.99)]
	#print(var99)
	var95s.append(var95)
	var99s.append(var99)
df = pd.DataFrame({'val95s': var95s, 'val99s': var99s})

response_body= json.dumps(df.to_json())

# Output HTTP header
print('Content-Type: application/json')
print()

# Output response body
print(response_body)


