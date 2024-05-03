"""
A script to tell me the current time in Sydney, Australia.

Author: Matthew Pitkin
Email: m.pitkin@lancaster.ac.uk
Date: 22/06/2020
"""

# import time from gettime
from tell_time import gettime

# use gettime function from tell_time
hour, minute, seconds = gettime()

# get the time in Sydney
sydneyhour = (hour + 9) % 24

print(f"The current time in Sydney is {sydneyhour}:{minute}:{seconds}")
