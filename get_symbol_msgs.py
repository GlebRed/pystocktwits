#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pystocktwits import Streamer
from pystocktwits.utils import *
import sys
sys.path.insert(0, 'pystocktwits')

# Create a Twit Streamer
twit = Streamer()

# Pass in all parameters to query search
raw_json = twit.get_symbol_msgs(sys.argv[1], since=0, max=0, limit=10, callback=None, filter=None)

# # Return raw json as JSON file
# return_json_file(raw_json, "../sample_json_output/get_symbol_msgs.json")

print(raw_json)
