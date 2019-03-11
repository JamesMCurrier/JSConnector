"""Calculates PI using Basel method"""

import JSConnector

JSConnector.start()

i = 1
total = 0
while True:
    total += 1/i**2
    i += 1
    PI_estimate = (6*total) ** 0.5
    JSConnector.send(PI_estimate)
