"""
timer.py

Allows users to set a short timer in seconds

Created By:
    - MuffinMedic <https://github.com/MuffinMedic>

License:
    GPL v3
"""

import threading

from cloudbot import hook
from cloudbot.util import formatting, web

@hook.command("timer")
def add_timer(chan, text, reply):
    """<seconds> [<reason>] - sets a timer for <seconds> (1-1500) with the optional specified [<reason>]"""
    seconds = float(text.split()[0])
    reason = ' '.join(text.split()[1:])
    if seconds < 1 or seconds > 1500:
        reply("Timer must be between 1 and 1500 seconds.")
    else:
        threading.Timer(seconds, print_timer, [chan, seconds, reply, reason]).start()
        reply("Timer started for {} seconds (Reason: {}).".format(seconds, reason))

def print_timer(chan, seconds, reply, reason):
    reply("Your timer for {} seconds has expired (Reason: {}).".format(seconds, reason))