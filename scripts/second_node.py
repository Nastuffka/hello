#!/usr/bin/env python3

import time
from datetime import datetime

while True:
	
	current_time = datetime.now().time()
	print(current_time)
	time.sleep(5)

